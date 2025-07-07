from .functions import classify_query_fn, generate_sql_fn, check_sql_fn, explain_sql_fn, parse_sql_check_result
from langchain.callbacks import get_openai_callback
from datetime import datetime
import json

def main(natural_query: str, schema: str):
    with get_openai_callback() as cb:
        query_type = classify_query_fn(natural_query)  # это уже строка
        sql = generate_sql_fn(natural_query, schema)   # строка
        check_result = check_sql_fn(sql)               # строка
        parsed_check = parse_sql_check_result(check_result)

        if not parsed_check["ok"]:
            return {"error": f"SQL ошибка: {parsed_check['error']}"}

        explanation = explain_sql_fn(sql)  # строка

        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": natural_query,
            "query_type": query_type,
            "sql": sql,
            "check": check_result,
            "explanation": explanation,
            "metrics": {
                "total_tokens": cb.total_tokens,
                "prompt_tokens": cb.prompt_tokens,
                "completion_tokens": cb.completion_tokens,
                "total_cost_usd": cb.total_cost,
            }
        }
        with open("sql_agent_run_log.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(log, ensure_ascii=False) + "\n")

        return {
            "query_type": query_type,
            "sql": sql,
            "check": check_result,
            "explanation": explanation
        }