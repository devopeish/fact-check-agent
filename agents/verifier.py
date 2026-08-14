import json
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from services.web_search import search_web


# ============================================================
# Environment
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing from .env"
    )


# ============================================================
# Gemini Client
# ============================================================

client = genai.Client(
    api_key=API_KEY
)

MODEL = "gemini-3.6-flash"


# ============================================================
# Verification Schema
# ============================================================

VERIFICATION_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {
            "type": "string",
            "enum": [
                "VERIFIED",
                "INACCURATE",
                "FALSE",
                "NO EVIDENCE"
            ]
        },
        "confidence": {
            "type": "number"
        },
        "reason": {
            "type": "string"
        },
        "correct_fact": {
            "type": "string"
        }
    },
    "required": [
        "verdict",
        "confidence",
        "reason",
        "correct_fact"
    ]
}


# ============================================================
# Gemini Instructions
# ============================================================

SYSTEM_INSTRUCTION = """
You are a rigorous web-based fact-checking engine.

You will receive:

1. A factual claim extracted from a PDF.
2. Live web search results retrieved specifically
   to investigate that claim.

Your job is to determine whether the claim is supported
by the provided web evidence.

IMPORTANT RULES:

1. Do NOT rely on your own prior knowledge.
2. Use ONLY the evidence provided in the search results.
3. Do not invent facts or sources.
4. Pay close attention to numbers, dates, percentages,
   financial figures and technical specifications.
5. If the evidence directly supports the claim,
   mark it VERIFIED.
6. If the evidence shows that the claim is partly wrong,
   outdated, exaggerated, or numerically incorrect,
   mark it INACCURATE.
7. If reliable evidence directly contradicts the claim,
   mark it FALSE.
8. If there is not enough reliable evidence,
   mark it NO EVIDENCE.

VERIFIED:
The available evidence supports the claim.

INACCURATE:
The claim contains some truth but has an important
error, outdated value, incorrect date, incorrect number,
or misleading detail.

FALSE:
Reliable evidence contradicts the claim.

NO EVIDENCE:
The available search results do not provide enough
reliable evidence to determine whether the claim is true
or false.

For correct_fact:

- State the corrected fact when the claim is inaccurate
  or false.
- If verified, briefly restate the supported fact.
- If there is no evidence, explain that no reliable
  conclusion can be established.

Keep the reason concise and evidence-based.
"""


# ============================================================
# Verify One Claim
# ============================================================

def verify_claim(claim):
    """
    Verify one claim against live web evidence.
    """

    claim_text = claim["claim"]


    # --------------------------------------------------------
    # STEP 1: Search web
    # --------------------------------------------------------

    search_results = search_web(
        claim_text,
        max_results=5
    )


    if not search_results:

        return {
            "claim": claim_text,
            "page": claim.get("page"),
            "verdict": "NO EVIDENCE",
            "confidence": 0.0,
            "reason": "No web evidence was found.",
            "correct_fact": "",
            "sources": []
        }


    # --------------------------------------------------------
    # STEP 2: Prepare evidence
    # --------------------------------------------------------

    evidence_text = ""

    for index, result in enumerate(
        search_results,
        start=1
    ):

        evidence_text += f"""
SOURCE {index}

Title:
{result.get("title", "")}

URL:
{result.get("url", "")}

Search relevance score:
{result.get("score", 0)}

Content:
{result.get("content", "")}

----------------------------------------
"""


    # --------------------------------------------------------
    # STEP 3: Prompt
    # --------------------------------------------------------

    prompt = f"""
FACTUAL CLAIM:

{claim_text}


LIVE WEB EVIDENCE:

{evidence_text}


Determine the correct verdict using ONLY
the evidence above.
"""


    # --------------------------------------------------------
    # STEP 4: Gemini with retry handling
    # --------------------------------------------------------

    max_retries = 3

    response = None

    for attempt in range(
        max_retries
    ):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    response_mime_type="application/json",
                    response_json_schema=VERIFICATION_SCHEMA
                )
            )

            break


        except Exception as error:

            error_text = str(error)

            is_rate_limit_error = (
                "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
            )

            is_service_unavailable = (
                "503" in error_text
                or "UNAVAILABLE" in error_text
            )


            if (
                not is_rate_limit_error
                and not is_service_unavailable
            ):

                raise


            if attempt == max_retries - 1:

                raise


            wait_time = 6 * (
                attempt + 1
            )

            print(
                f"Gemini temporarily unavailable "
                f"(attempt {attempt + 1}/"
                f"{max_retries}). "
                f"Waiting {wait_time} seconds..."
            )

            time.sleep(
                wait_time
            )


    # --------------------------------------------------------
    # STEP 5: Parse response
    # --------------------------------------------------------

    try:

        result = json.loads(
            response.text
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            "Gemini returned invalid verification JSON."
        ) from error


    # --------------------------------------------------------
    # STEP 6: Return result
    # --------------------------------------------------------

    return {
        "claim": claim_text,
        "page": claim.get("page"),
        "verdict": result.get(
            "verdict",
            "NO EVIDENCE"
        ),
        "confidence": result.get(
            "confidence",
            0.0
        ),
        "reason": result.get(
            "reason",
            ""
        ),
        "correct_fact": result.get(
            "correct_fact",
            ""
        ),
        "sources": search_results
    }