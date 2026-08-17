import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Environment

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing from .env"
    )

# Gemini Client

client = genai.Client(
    api_key=API_KEY
)

MODEL = "gemini-3.6-flash"


# Claim Extraction Schema

CLAIM_SCHEMA = {
    "type": "object",
    "properties": {
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim_id": {
                        "type": "integer"
                    },
                    "claim": {
                        "type": "string"
                    },
                    "claim_type": {
                        "type": "string",
                        "enum": [
                            "STATISTIC",
                            "DATE",
                            "FINANCIAL",
                            "TECHNICAL",
                            "HISTORICAL",
                            "COMPANY",
                            "PRODUCT",
                            "COMPARISON",
                            "OTHER"
                        ]
                    },
                    "page": {
                        "type": "integer"
                    }
                },
                "required": [
                    "claim_id",
                    "claim",
                    "claim_type",
                    "page"
                ]
            }
        }
    },
    "required": [
        "claims"
    ]
}


# Gemini Instructions

SYSTEM_INSTRUCTION = """
You are a factual claim extraction system.

Your task is to identify claims from a document that can be
verified against public information on the live web.

Extract factual claims involving things such as:

- numbers
- statistics
- percentages
- dates
- financial figures
- company facts
- product facts
- technical specifications
- historical statements
- comparisons
- measurable statements

Do NOT extract:

- opinions
- subjective statements
- marketing slogans
- vague promotional language
- questions
- instructions
- ordinary sentences with no independently verifiable fact

IMPORTANT:

1. Preserve the meaning of the original claim.
2. Do not change numbers.
3. Do not change dates.
4. Do not invent information.
5. Every claim must correspond to the document.
6. Preserve the original page number.
7. If a sentence contains multiple independent factual claims,
   split them into separate claims.

Return only structured JSON matching the provided schema.
"""


# Main Function

def extract_claims(pages):
    """
    Extract independently verifiable factual claims.

    Args:
        pages: List of dictionaries containing page and text.

    Returns:
        List of structured claim dictionaries.
    """

    document_text = ""

    for page in pages:

        document_text += (
            f"\n\n--- PAGE {page['page']} ---\n"
            f"{page['text']}"
        )

    prompt = f"""
Analyze the following document and extract all independently
verifiable factual claims.

DOCUMENT:

{document_text}
"""

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_json_schema=CLAIM_SCHEMA
            )
        )

    except Exception as error:

        error_text = str(error)

        if (
            "429" in error_text
            or "RESOURCE_EXHAUSTED" in error_text
        ):

            raise RuntimeError(
                "Gemini API quota has been reached "
                "while extracting claims."
            ) from error

        if (
            "503" in error_text
            or "UNAVAILABLE" in error_text
        ):

            raise RuntimeError(
                "Gemini is temporarily unavailable "
                "while extracting claims."
            ) from error

        raise

    try:

        result = json.loads(
            response.text
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            "Gemini returned invalid JSON "
            "while extracting claims."
        ) from error

    return result.get(
        "claims",
        []
    )