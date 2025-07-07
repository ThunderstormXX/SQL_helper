# SQL_helper

Telegram-бот для генерации SQL-запросов с помощью LLM.

## Структура проекта

```
SQL_helper/
├── agent/
│   ├── client.py              # OpenAI client
│   ├── prompts.py             # SQL-промпты
│   ├── functions.py           # Функции генерации SQL
│   └── pipeline.py            # Основной пайплайн
├── telegram_bot/
│   └── bot.py                 # Telegram-бот
├── data/
│   └── sample_data.py         # Пример схемы БД
├── requirements.txt
└── README.md
```

## Запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Укажите токен Telegram-бота в `telegram_bot/bot.py`

3. Запустите бота:
   ```bash
   python telegram_bot/bot.py
   ```