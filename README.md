# Auto-Clue Testing

Auto-Clue Testing is an AI-assisted automation framework that uses Selenium, Flask, and Google Gemini to run web tests, log results, and generate intelligent insights and reports automatically.

---

## Features

* AI insights from test logs using Google Gemini
* Automated web testing with Selenium
* Excel-based reporting
* Database logging and traceability
* Configurable scheduling for automated runs

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

Create a `.env` file based on `.env.example` and add your Gemini API key and database URI.

---

## Usage

Run the full workflow:

```bash
python main.py
```

Run AI insights only:

```bash
python -m ai.insight_engine
```

Run tests:

```bash
pytest
```

---

## Requirements

* selenium
* google-generativeai
* flask
* pytest
* pandas
* openpyxl
* python-dotenv
* schedule

---

## License

Apache 2.0 License
