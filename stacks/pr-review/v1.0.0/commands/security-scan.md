---
description: 'Deep security audit: OWASP Top 10, secrets, auth, dependencies'
---

Perform a security-focused audit of the selected code. Assume an attacker will read this code to find vulnerabilities.

Checklist:

1. **Injection** — SQL, NoSQL, OS command, LDAP, XPath injection vectors
2. **Broken Auth** — Weak passwords, session fixation, JWT issues, MFA gaps
3. **Sensitive Data Exposure** — Plaintext secrets, weak encryption, PII leakage
4. **XXE / SSRF** — XML parsing, server-side request forgery
5. **Access Control** — Missing authorization checks, IDOR, privilege escalation
6. **Security Misconfig** — Default creds, verbose errors, missing headers
7. **XSS** — Reflected, stored, DOM-based XSS
8. **Deserialization** — Untrusted data deserialization
9. **Components** — Known vulnerable dependencies, outdated libraries
10. **Logging** — Insufficient logging, log injection

Output:
```
SECURITY AUDIT RESULT
===================
Risk Level: LOW / MEDIUM / HIGH / CRITICAL

Findings:
1. [SEVERITY] File:Line — Description
   Fix: [corrected code]

2. ...

Passed Checks: X/10
```

If CRITICAL findings exist, recommend blocking merge until resolved.
