Reflected XSS Automated Scanner
🛡️ Overview
As part of Orion Health Systems' routine internal application security audits, this automated vulnerability scanner was developed to identify potential reflected Cross-Site Scripting (XSS) flaws in our patient access web search portal.

Building upon previous experience with automated security tooling (such as login form auditing), this script programmatically tests target search endpoints with a curated suite of XSS payloads, inspects HTTP response bodies for unescaped reflection, and provides clear, actionable reporting to assist developers in remediation.

✨ Features
Automated Payload Delivery: Seamlessly submits multiple standard and edge-case XSS payloads via HTTP GET/POST requests.

Reflection Analysis: Parses server responses to determine whether malicious scripts are reflected back into the document body unescaped.

Robust Error & Exception Handling: Gracefully manages network errors, connection timeouts, and broken URLs without crashing.

Clear Reporting: Outputs distinct, color-coded or clearly formatted logs indicating whether a tested endpoint is vulnerable or secure.

PEP 8 Compliant: Written following Python enhancement proposal standards to ensure clean, maintainable, and readable code.

🛠️ Prerequisites & Dependencies
Ensure you have the following installed on your local development environment:

Python 3.8+

pip (Python package manager)
