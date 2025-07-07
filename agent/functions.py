from .client import client
from .prompts import Prompts
import re

def classify_query_fn(natural_query: str) -> str:
    response = (Prompts.classify() | client).invoke({"natural_query": natural_query})
    return response.content

def generate_sql_fn(natural_query: str, schema: str) -> str:
    response = (Prompts.generate() | client).invoke({
        "natural_query": natural_query,
        "schema": schema
    })
    return response.content

def check_sql_fn(sql_query: str) -> str:
    response = (Prompts.check() | client).invoke({"sql_query": sql_query})
    return response.content

def explain_sql_fn(sql_query: str) -> str:
    response = (Prompts.explain() | client).invoke({"sql_query": sql_query})
    return response.content


def parse_sql_check_result(check_result: str) -> dict:
    result = {"ok": False, "warning": None, "error": None}
    text = check_result.lower()
    if "ok" in text:
        result["ok"] = True
    if "warning" in text:
        match = re.search(r"warning: ?(.+)", check_result, re.IGNORECASE)
        if match:
            result["warning"] = match.group(1).strip()
    if not result["ok"]:
        result["error"] = check_result.strip()
    return result