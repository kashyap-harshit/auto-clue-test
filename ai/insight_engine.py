import google.generativeai as genai
from config.settings import GEMINI_API_KEY
from db.db_logger import fetch_recent_logs


def provide_insights():

    print("Generating insights...")
    genai.configure(api_key=GEMINI_API_KEY)

    results = fetch_recent_logs()

    prompt = f"""
    These are the results : ${results}

    According to the results answer these few questions:
        Average response time for all endpoints.
        Which API endpoint is most prone to errors?
        Any unusual pattern in scores or latency?

    If you have something more to say go ahead.

    Be really precise, write only what is necessary.

    """


    model = genai.GenerativeModel("gemini-2.5-flash")

    return model.generate_content(prompt).candidates[0].content.parts[0].text.strip()
