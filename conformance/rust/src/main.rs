use std::{env, fs, path::Path};

fn field(line: &str, key: &str) -> String {
    let marker = format!("\"{}\":\"", key);
    if let Some(start) = line.find(&marker) {
        let rest = &line[start + marker.len()..];
        if let Some(end) = rest.find('"') {
            return rest[..end].to_string();
        }
    }
    String::new()
}

fn b64_decode(input: &str) -> Vec<u8> {
    let alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    let mut out = Vec::new();
    let mut buffer: u32 = 0;
    let mut bits: u8 = 0;
    for byte in input.bytes() {
        if byte == b'=' { break; }
        let value = alphabet.iter().position(|candidate| *candidate == byte).unwrap_or(0) as u32;
        buffer = (buffer << 6) | value;
        bits += 6;
        if bits >= 8 {
            bits -= 8;
            out.push(((buffer >> bits) & 0xff) as u8);
        }
    }
    out
}

fn rotr(x: u32, n: u32) -> u32 { (x >> n) | (x << (32 - n)) }

fn sha256(data: &[u8]) -> String {
    let mut h: [u32; 8] = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
    ];
    let k: [u32; 64] = [
        0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
        0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
        0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
        0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
        0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
        0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
        0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
        0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
    ];
    let bit_len = (data.len() as u64) * 8;
    let mut msg = data.to_vec();
    msg.push(0x80);
    while msg.len() % 64 != 56 { msg.push(0); }
    msg.extend_from_slice(&bit_len.to_be_bytes());
    for chunk in msg.chunks(64) {
        let mut w = [0u32; 64];
        for i in 0..16 { w[i] = u32::from_be_bytes([chunk[i*4],chunk[i*4+1],chunk[i*4+2],chunk[i*4+3]]); }
        for i in 16..64 {
            let s0 = rotr(w[i-15],7) ^ rotr(w[i-15],18) ^ (w[i-15] >> 3);
            let s1 = rotr(w[i-2],17) ^ rotr(w[i-2],19) ^ (w[i-2] >> 10);
            w[i] = w[i-16].wrapping_add(s0).wrapping_add(w[i-7]).wrapping_add(s1);
        }
        let (mut a,mut b,mut c,mut d,mut e,mut f,mut g,mut hh) = (h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7]);
        for i in 0..64 {
            let s1 = rotr(e,6) ^ rotr(e,11) ^ rotr(e,25);
            let ch = (e & f) ^ ((!e) & g);
            let temp1 = hh.wrapping_add(s1).wrapping_add(ch).wrapping_add(k[i]).wrapping_add(w[i]);
            let s0 = rotr(a,2) ^ rotr(a,13) ^ rotr(a,22);
            let maj = (a & b) ^ (a & c) ^ (b & c);
            let temp2 = s0.wrapping_add(maj);
            hh=g; g=f; f=e; e=d.wrapping_add(temp1); d=c; c=b; b=a; a=temp1.wrapping_add(temp2);
        }
        h[0]=h[0].wrapping_add(a); h[1]=h[1].wrapping_add(b); h[2]=h[2].wrapping_add(c); h[3]=h[3].wrapping_add(d);
        h[4]=h[4].wrapping_add(e); h[5]=h[5].wrapping_add(f); h[6]=h[6].wrapping_add(g); h[7]=h[7].wrapping_add(hh);
    }
    h.iter().map(|word| format!("{:08x}", word)).collect()
}

fn authority(role: &str, action: &str, object_type: &str, privacy_tier: i32) -> bool {
    match action {
        "read_private_weather" if object_type == "WeatherState" && privacy_tier >= 2 => role == "source" || role == "steward",
        "modify_canonical_source" => role == "source" || role == "steward",
        "sign_contract" => role == "source" || role == "steward",
        "quote" => matches!(role, "portrait" | "bud" | "branch" | "source" | "steward"),
        "infer" => matches!(role, "portrait" | "bud" | "branch" | "sherpa" | "source" | "steward"),
        _ => true,
    }
}

fn continuity(p: f64, c: f64, f: f64, co: bool, separated: bool, rejected: bool) -> &'static str {
    if p < 0.80 { "unclassified" }
    else if separated || rejected || f < 0.70 { "branch" }
    else if co && c >= 0.70 && f >= 0.70 { "bud" }
    else if c >= 0.50 && f >= 0.75 { "portrait" }
    else { "portrait_candidate" }
}

fn record_valid(json: &str, object_type: &str) -> bool {
    let common = ["schema_version","object_type","id","version","status","validation_state","content","authorship","provenance","authority","privacy_tier","relationships"];
    if !common.iter().all(|key| json.contains(&format!("\"{}\"", key))) { return false; }
    if !json.contains("\"schema_version\":\"lca-schema-0.1\"") || !json.contains(&format!("\"object_type\":\"{}\"", object_type)) { return false; }
    let required = match object_type {
        "SourceRecord" => vec!["text", "title", "uri"],
        "Episode" => vec!["scene", "title"],
        "Claim" => vec!["text"],
        "Interpretation" => vec!["text", "lens"],
        "DecisionTrace" => vec!["question", "outcome"],
        "WeatherState" => vec!["state"],
        "Invariant" => vec!["statement"],
        "Transformation" => vec!["input_ids", "output_ids", "method"],
        "PortraitResponse" => vec!["response_class", "evidence_ids"],
        "BudState" => vec!["parent_id", "co_developed"],
        "BranchState" => vec!["parent_id", "separation_event", "divergence_scope"],
        "AuthorityGrant" => vec!["grantor", "grantee", "allowed_actions"],
        "SourceReview" => vec!["target_id", "review_type", "note"],
        _ => return false,
    };
    if object_type == "SourceRecord" {
        required.iter().any(|key| json.contains(&format!("\"{}\"", key)))
    } else {
        required.iter().all(|key| json.contains(&format!("\"{}\"", key)))
    }
}

fn check(line: &str) -> (String, bool, String) {
    let case_id = field(line, "case_id");
    let kind = field(line, "kind");
    let expected = {
        let value = field(line, "expected");
        if value.is_empty() { field(line, "expected_stage") } else { value }
    };
    let (actual, detail) = match kind.as_str() {
        "canonical_hash" | "event_hash" | "recovery_replay" => {
            let got = sha256(&b64_decode(&field(line, "payload_b64")));
            (if got == field(line, "expected_sha256") { "pass" } else { "fail" }.to_string(), got)
        }
        "record_validate" => {
            let json = String::from_utf8_lossy(&b64_decode(&field(line, "record_b64"))).to_string();
            (if record_valid(&json, &field(line, "object_type")) { "pass" } else { "fail" }.to_string(), String::new())
        }
        "ledger_transition" => {
            let ok = field(line,"event_type") == "update" && field(line,"from_status") != field(line,"to_status");
            (if ok { "pass" } else { "fail" }.to_string(), String::new())
        }
        "authority" => {
            let ok = authority(&field(line,"role"), &field(line,"action"), &field(line,"object_type"), field(line,"privacy_tier").parse().unwrap_or(0));
            (ok.to_string(), String::new())
        }
        "continuity" => {
            let stage = continuity(field(line,"p").parse().unwrap_or(0.0), field(line,"c").parse().unwrap_or(0.0), field(line,"f").parse().unwrap_or(0.0), field(line,"co_developed")=="true", field(line,"separated")=="true", field(line,"rejected_core")=="true");
            (stage.to_string(), String::new())
        }
        "source_review" => {
            let valid = ["affirmed_as_mine","good_inference_not_explicit","assistant_contamination","historical_revision","invariant_reaffirmed","branch_disagreement","private_weather"].contains(&field(line,"review_type").as_str());
            (if valid { "pass" } else { "fail" }.to_string(), String::new())
        }
        "model_mutation" => ((field(line,"action") != "direct_canonical_write").to_string(), String::new()),
        _ => ("unknown".to_string(), "unknown fixture".to_string()),
    };
    (case_id, actual == expected, format!("{}", actual) + "\t" + &detail)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let fixtures = args.get(1).map(String::as_str).unwrap_or("../fixtures/conformance.jsonl");
    let output = args.get(2).map(String::as_str).unwrap_or("rust_conformance.tsv");
    let text = fs::read_to_string(Path::new(fixtures)).expect("fixture file");
    let mut lines = Vec::new();
    let mut passed = 0usize;
    for line in text.lines().filter(|line| !line.trim().is_empty()) {
        let (case_id, ok, detail) = check(line);
        if ok { passed += 1; }
        lines.push(format!("{}\t{}\t{}", case_id, ok, detail));
    }
    fs::write(output, lines.join("\n") + "\n").expect("output file");
    println!("Rust conformance: {}/{} passed", passed, lines.len());
    if passed != lines.len() { std::process::exit(1); }
}
