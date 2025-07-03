
# News_Bot-AI-Agent

This project is an **automated news summarizer and notifier** that:

✅ Fetches latest Indian news headlines (via NewsData.io)  
✅ Summarizes them using an LLM (OpenRouter / LLaMA)  
✅ Sends the summaries directly to your Telegram account  

---

## 🌟 Features

- 🇮🇳 Focus on India-based news in English  
- Automated daily summaries using AI  
- Clean Telegram delivery with Markdown formatting  
- Secrets and keys safely kept in `.env` (not in repo)

---

## ⚙️ How It Works

1. Pulls top news headlines via NewsData.io API  
2. Summarizes each article using OpenRouter's LLaMA model  
3. Sends the summary to a Telegram chat via Telegram Bot API  

---

## 🛠️ Installation

1. Clone this repo:

```bash
git clone https://github.com/YOUR-USERNAME/News_Bot-AI-Agent.git
cd News_Bot-AI-Agent

2. Install dependencies:
```bash
pip install -r requirements.txt

3.Create a .env file in the project root:
```bash
OPENROUTER_API_KEY=your_openrouter_api_key
NEWSDATA_API_KEY=your_newsdata_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

4. Run the bot:
```bash
python "news bot.py"

