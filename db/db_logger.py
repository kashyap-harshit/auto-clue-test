from pymongo import MongoClient
from datetime import datetime
from config.settings import MONGO_URI




client = MongoClient(MONGO_URI)

db = client["auto-clue-test"]


def log_api_result(record):
    record.setdefault("timestamp", datetime.utcnow())
    db.api_logs.insert_one(record)


def fetch_recent_logs(limit=100):
    return list(db.api_logs.find().sort("timestamp", -1).limit(limit))