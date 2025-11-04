import requests
from config.settings import BASE_URL

session = requests.Session()

def login(email, password):
    path = "/users/login"
    login_url = f"{BASE_URL}{path}"
    payload = {"email": email, "password": password}
    response = session.post(login_url, json=payload, timeout=10)

    if response.status_code == 200:
        print("Login successful")
        jwt = response.json().get("jwt")
        session.headers.update({"Authorization": f"Bearer {jwt}"})
    else:
        print("Login failed:", response.status_code, response.text)
    return {
        "path": path,
        "status": response.status_code,
        "time": response.elapsed.total_seconds(),
        "body": safe_preview(response),
    }



def call_endpoint(path, method="get", json=None):
    url = f"{BASE_URL}{path}"

    r = session.request(method, url, json=json, timeout=10)
    new_r = {
        "path": path,
        "status": r.status_code,
        "time": r.elapsed.total_seconds(),
        "body": safe_preview(r),
    }
    return new_r


def safe_preview(resp):
    try:
        j = resp.json()
        return {"json_len": len(str(j))}
    except:
        return {"text_len": len(resp.text)}


def get_leaderboard():
    print("hitting /admin/get-leaderboard?page=1")
    return call_endpoint("/admin/get-leaderboard?page=1", method="get", json={})

def get_users_list():
    print("hitting /admin/users-list?page=1")
    return call_endpoint("/admin/users-list?page=1", method="get", json={})

def get_something(): #for 404
    print("hitting a random that doesn't exist")
    return call_endpoint("/doesnotexist", method="get", json={})