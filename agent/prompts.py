from langchain.prompts import PromptTemplate

class Prompts:
    @staticmethod
    def classify():
        return PromptTemplate.from_template(
            "Ты — ассистент по SQL.\n"
            "Определи тип SQL-запроса (SELECT, UPDATE, INSERT, DELETE, CREATE, DROP) для следующего запроса:\n"
            "{natural_query}\n"
            "Выведи только один тип."
        )

    @staticmethod
    def generate():
        return PromptTemplate.from_template(
            "Ты — помощник по SQL.\n"
            "Дана схема базы данных:\n"
            "{schema}\n"
            "Сгенерируй корректный SQL-запрос по заданному вопросу:\n"
            "{natural_query}\n"
            "Выведи только SQL, без пояснений."
        )

    @staticmethod
    def check():
        return PromptTemplate.from_template(
            "Ты — эксперт по SQL.\n"
            "Проверь следующий SQL-запрос на синтаксические ошибки и потенциальные риски:\n"
            "{sql_query}\n"
            "Если ошибок нет, выведи 'OK'."
        )

    @staticmethod
    def explain():
        return PromptTemplate.from_template(
            "Ты — ассистент по SQL.\n"
            "Объясни простыми словами, что делает этот запрос:\n"
            "{sql_query}"
        )