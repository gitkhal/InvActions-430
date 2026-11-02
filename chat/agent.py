import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from .tools import get_item


load_dotenv()


def ask_agent(message):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=message,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an AI inventory agent. "
                "Use the inventory tool when asked about an inventory item. "
		"Respond in plain text only. Do not use Markdown, asterisks, headings, or bullet formatting. "
                "You may calculate prices, totals, VAT, percentages, and quantities. "
                "Never invent inventory values."
            ),
            tools=[get_item],
        ),
    )

    return response.text