"""Reflected XSS vulnerability scanner.

This script submits a series of test payloads to a target search
endpoint and checks whether each payload is reflected, unescaped,
in the HTTP response body. This kind of check is a common first
step application security teams use to flag candidate reflected
XSS issues for follow-up manual review.
"""

import requests

BASE_URL = "http://127.0.0.1:5000/search"

payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(2)>",
    "<svg/onload=alert(3)>",
]

TIMEOUT_SECONDS = 5


def test_payload(payload):
    """Submit a single payload and report whether it is reflected.

    Returns True if the payload appears unescaped in the response
    body (a potential reflected XSS), False if no reflection was
    found, and None if the request could not be completed or the
    server responded with a non-200 status code.
    """
    try:
        response = requests.get(
            BASE_URL, params={"q": payload}, timeout=TIMEOUT_SECONDS
        )
    except requests.exceptions.Timeout:
        print(f"[x] Request timed out for payload: {payload}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"[x] Could not connect to the server for payload: {payload}")
        return None
    except requests.exceptions.RequestException as exc:
        print(f"[x] Request failed for payload: {payload} ({exc})")
        return None

    if response.status_code != 200:
        print(
            f"[x] Non-200 response ({response.status_code}) "
            f"for payload: {payload}"
        )
        return None

    if payload in response.text:
        print(f"[!] Potential XSS vulnerability detected with payload: {payload}")
        return True

    print(f"[\u2713] No reflection found for payload: {payload}")
    return False


def main():
    print("\n[+] Starting reflected XSS test...\n")

    for payload in payloads:
        test_payload(payload)


if __name__ == "__main__":
    main()
