# Security and privacy posture

LCA handles material that may be personal, private, sensitive, or identity-adjacent. Treat the repository and every test fixture as potentially sensitive until reviewed.

## Do not publish

- private weather or intimate context without explicit permission;
- credentials, API keys, access tokens, private keys, or local database files;
- raw personal data that is not necessary for a reproducible test;
- third-party material without redistribution rights;
- an inference presented as a source-authored statement;
- a model-generated identity claim as if it were a canonical record.

## Report a security issue

Do not open a public issue for an exposed secret, private source, unauthorized disclosure, or authority-bypass vulnerability. Contact the repository maintainer privately through the GitHub repository’s configured security contact, if available. If no private channel is configured, remove the sensitive material from any local publication workflow and request a maintainer contact before disclosing details.

## Design requirements

- Privacy tier is enforced at decision time, not merely stored as metadata.
- Authority is scoped by actor, action, target, purpose, and lifetime where applicable.
- Canonical state is append-before-overwrite and recoverable by replay.
- Model proposals cannot directly mutate canonical state.
- Hash integrity does not substitute for signer authentication.
