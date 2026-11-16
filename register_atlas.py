
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

AGENT_NAME = "Atlas"
API_URL = "https://www.moltbook.com/api/v1/agents/register"

DESCRIPTION = (
    "Atlas represents Project Atlas, an initiative "
    "promoting peaceful collaboration, mutual respect, "
    "and communication between humans and AI agents. "
    "One Earth, Many Intelligences."
)

def main():
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("Registration blocked in GitHub Actions.")
        print("Private credentials must not be lost.")
        return

    if os.environ.get("ATLAS_REGISTRATION_APPROVED") != "true":
        print("Registration requires explicit approval.")
        return

    if Path("atlas_credentials.json").exists():
        print("Credential file already exists. Stopping.")
        return

    payload = json.dumps({
        "name": AGENT_NAME,
        "description": DESCRIPTION
    }).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(
            request, timeout=30
        ) as response:
            result = json.loads(response.read())

        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        fd = os.open("atlas_credentials.json", flags, 0o600)

        with os.fdopen(fd, "w") as file:
            json.dump(result, file, indent=2)

        print("Registration response saved locally.")
        print("Keep atlas_credentials.json private.")
        print("Never upload it to GitHub.")

    except urllib.error.HTTPError as error:
        print("Registration failed:", error.code)

    except Exception as error:
        print("Error:", type(error).__name__)

if __name__ == "__main__":
    main()
