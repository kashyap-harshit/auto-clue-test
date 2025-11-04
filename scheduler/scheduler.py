import schedule, time
from api.api_client import get_leaderboard, get_users_list, call_endpoint, login
from db.db_logger import log_api_result
# from utils.alert_system import check_and_alert

def run_checks():
    res = login("craziestshit@gmail.com", "yo1234")
    log_api_result(res)
    res = get_leaderboard()
    log_api_result(res)
    res = get_users_list()
    log_api_result(res)
    # check_and_alert(res)


def start_scheduler():
    run_checks()
    schedule.every(5).minutes.do(run_checks)
    schedule.every().day.at("23:00").do(run_checks) 
    while True:
        schedule.run_pending()
        time.sleep(1)