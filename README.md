# 🤖 WikipediaBot

Telegram-бот на [aiogram 3](https://docs.aiogram.dev/), который ищет статьи на русском языке в Википедии по тексту, отправленному пользователем.

## 🚀 Возможности

- Обработка сообщений пользователя
- Поиск соответствующей статьи на Википедии
- Отправка краткой информации (первый абзац статьи)
- Устойчивость к ошибкам
- Разделение секретов через `.env`

---

## 🔧 Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/IBakuda/WikiParser_Bot.git
cd WikiParser_Bot
```

2. Docker 

```bash
docker build . -t bot_wiki
docker run --rm --name tg_bot -e TG_BOT_TOKEN= bot_wiki
```
TG_BOT_TOKEN - ваш токен полученный от BotFather 