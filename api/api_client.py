import requests
from config.settings import BASE_URL

session = requests.Session()

def login(email, password):
    login_url = f"{BASE_URL}/users/login"
    payload = {"email": email, "password": password}
    response = session.post(login_url, json=payload, timeout=10)

    if response.status_code == 200:
        print("Login successful")
        jwt = response.json().get("jwt")
        session.headers.update({"Authorization": f"Bearer {jwt}"})
    else:
        print("Login failed:", response.status_code, response.text)
    return response


def call_endpoint(path, method="get", json=None):
    url = f"{BASE_URL}{path}"

    r = session.request(method, url, json=json, timeout=10)
    return {
        "path": path,
        "status": r.status_code,
        "time": r.elapsed.total_seconds(),
        "body": safe_preview(r),
    }


def safe_preview(resp):
    try:
        j = resp.json()
        return {"json_len": len(str(j))}
    except:
        return {"text_len": len(resp.text)}


def get_leaderboard():
    return call_endpoint("/admin/get-leaderboard?page=1", method="get", json={})

def get_users_list():
    return call_endpoint("/admin/users-list?page=1", method="get", json={})