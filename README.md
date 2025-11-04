# Auto-Clue Testing

Auto-Clue Testing is an automation tool that integrates with your existing backend to test APIs, log data in MongoDB, and generate AI-powered insights using Google Gemini. It simplifies backend testing and reporting for monitoring systems.

---

## Features

* Automated API calls for performance and leaderboard data
* AI-based insights using Google Gemini
* Generate reports (eg., sheets)
* MongoDB logging for all API results
* Scheduled execution using `schedule`
* Lightweight and configurable with `.env`

---


---

## Installation

```bash
git clone https://github.com/<your-username>/auto-clue-testing.git
cd auto-clue-testing
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and set the following:

```
GEMINI_API_KEY=<your_gemini_api_key>
MONGO_URI=<your_mongo_connection_string>
BASE_URL=<your_backend_base_url>
```

---

## Usage

Run the main automation workflow:

```bash
python main.py
```

This will:

1. Fetch recent API data.
2. Log results to MongoDB.
3. Generate AI insights using Gemini.
4. Schedule future runs automatically.
5. Generate reports (eg., sheets)

---

## Requirements

```
google-generativeai
requests
python-dotenv
pymongo
pandas
schedule
```

---

