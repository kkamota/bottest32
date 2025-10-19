# Telegram Bot with Flyer API Gating

This project contains an [aiogram](https://docs.aiogram.dev/) based Telegram bot that restricts access to its handlers until a user completes all mandatory tasks from the [Flyer API](https://flyerapi.app/).

## Prerequisites

- Python 3.11+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- A Flyer API key obtained via [@FlyerServiceBot](https://t.me/FlyerServiceBot)

## Installation

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install aiogram flyerapi
   ```

## Configuration

The bot is configured via environment variables. You can export them in your shell or place them in a `.env` file and load it before starting the bot.

| Variable | Required | Description |
| --- | --- | --- |
| `BOT_TOKEN` | ✅ | Telegram bot token issued by BotFather. |
| `CHANNEL_USERNAME` | ❌ | Public channel username that the bot uses (defaults to `@giftsauctionsru`). |
| `ADMIN_IDS` | ❌ | Comma-separated list of Telegram user IDs with admin access (defaults to `5838432507`). |
| `FLYER_API_KEY` | ✅ | API key from Flyer for subscription/task checks. |

Example on Linux/macOS:

```bash
export BOT_TOKEN="123456789:your-telegram-bot-token"
export FLYER_API_KEY="FL-xxxxxxxxxxxxxxxx"
export CHANNEL_USERNAME="@yourchannel"
export ADMIN_IDS="111111111,222222222"
```

## Database

The bot uses a SQLite database stored in `bot_data.sqlite3` in the project root. The schema is created automatically on startup; no manual migrations are required.

## Running the Bot

From the repository root, run:

```bash
python -m bottest32.main
```

The bot starts polling Telegram for updates. Ensure that the machine stays online, or configure a process manager (systemd, pm2, Docker, etc.) to keep it running.

## Optional: Flyer Webhook

The current setup relies on polling Flyer when a user interacts with the bot. If you want to receive asynchronous task updates, consult the Flyer API documentation about enabling webhooks and update the bot accordingly.

## Development Tips

- Use `python -m compileall .` or `ruff`/`black` (if installed) to check syntax and formatting.
- Run the bot in a dedicated test chat before deploying to production.

