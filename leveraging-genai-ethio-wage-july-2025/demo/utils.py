import json
import re


def parse_json(content: str, begin="```json", end="```"):
    if begin in content and re.search(rf"{end}(?!json)", content):
        json_text = content.removeprefix("```json").removesuffix("```")
        return json.loads(json_text)
    raise ValueError("Not properly formatted content.")
