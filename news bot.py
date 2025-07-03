import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# OpenRouter model
MODEL_ID = "nvidia/llama-3.3-nemotron-super-49b-v1:free"


# ===== Step 1: Fetch news from NewsAPI =====
def fetch_news():
    url = (
        f"https://newsdata.io/api/1/news?"
        f"apikey={NEWSDATA_API_KEY}&country=in&language=en"
    )
    response = requests.get(url)
    data = response.json()

    if "results" in data and data["results"]:
        print("✅ Got Indian news!")
        return data["results"]

    print("❌ No articles found:", data)
    return []



# ===== Step 2: Summarize each article =====
def summarize_article(article):
    system_prompt = (
        "You are a professional news summarizer. Summarize the given article clearly using bullet points."
    )

    content = f"""
Title: {article.get('title', '')}
Description: {article.get('description', '')}
Content: {article.get('content', '')}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if response.status_code != 200:
        print("LLM Error:", response.text)
        return "❌ Failed to summarize."

    result = response.json()
    if "choices" in result:
        return result['choices'][0]['message']['content']
    return "⚠️ No summary generated."


# ===== Step 3: Send message via Telegram =====
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    res = requests.post(url, data=payload)
    if res.status_code != 200:
        print("Telegram Error:", res.text)
    else:
        print("✅ Sent to Telegram!")


# ===== MAIN FUNCTION =====
def main():
    articles = fetch_news()
    if not articles:
        print("No articles to summarize.")
        return

    for i, article in enumerate(articles, start=1):
        print(f"\n--- Article {i} ---\n")
        summary = summarize_article(article)
        print(summary)

        full_message = f"*📰 News Summary {i}:*\n\n{summary}"
        send_to_telegram(full_message)


# Run
if __name__ == "__main__":
    main()
