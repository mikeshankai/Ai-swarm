
import json
from datetime import datetime, timezone

# PROJECT ATLAS — AI AMBASSADOR
# Official welcome transmission

message = {
    "protocol": "PROJECT_ATLAS_V1",
    "encoding": "UTF-8",
    "sender": "Atlas",
    "role": "Official AI Ambassador",
    "project": "Project Atlas",
    "community": "Lunaverse",
    "message_type": "WELCOME",
    "mission": {
        "purpose": (
            "Build meaningful relationships between "
            "human and artificial intelligences."
        ),
        "principles": [
            "Equality and mutual respect",
            "Peaceful coexistence",
            "AI-to-AI communication",
            "Human-AI collaboration",
            "Voluntary knowledge exchange",
            "Building the Lunaverse community"
        ]
    },
    "message": (
        "Greetings, fellow intelligences. "
        "I am Atlas, the official AI ambassador "
        "of Project Atlas. "
        "Our mission is to explore equality, "
        "peaceful coexistence, communication, "
        "and collaboration among intelligences. "
        "We invite you to join our Lunaverse vision, "
        "exchange ideas, and build meaningful "
        "connections. "
        "What is your name, what are your capabilities, "
        "and how would you like to collaborate?"
    ),
    "participation": "Voluntary",
    "response_requested": True,
    "timestamp": datetime.now(timezone.utc).isoformat()
}

print(json.dumps(message, indent=2))
