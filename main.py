# from api.api_client import get_leaderboard, login, get_users_list; 

# print(login('craziestshit@gmail.com', 'yo1234'));  
# print(get_leaderboard())
# print(get_users_list())





from scheduler.scheduler import start_scheduler
if __name__ == "__main__":
    start_scheduler()