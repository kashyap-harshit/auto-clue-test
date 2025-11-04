import requests
from config.settings import BASE_URL


def call_endpoint(path, method='get', json=None):
    url = f"{BASE_URL}{path}"
    r = requests.request(method, url, json=json, timeout=10)
    return {"path": path, "status": r.status_code, "time": r.elapsed.total_seconds(), "body": safe_preview(r)}



def safe_preview(resp):
    try:
        j = resp.json()
        return {"json_len": len(str(j))} 
    except:
        return {"text_len": len(resp.text)}