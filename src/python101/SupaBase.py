import requests
import json

public_api = "sb_publishable_IDd6uV8uzhOlbK3p94DoNw_4ePJkiZ5"
supabase_api = "https://eyjofdmiyocyeksjixoy.supabase.co/rest/v1/TaskList"

params = {"select":"*"}
headers = {"apikey": public_api,
    "Authorization": f"Bearer {public_api}"}

# r = requests.get(supabase_api,params=params,headers=headers)
# print(r.json())

# r = json.dumps(r.json(),indent=4)
# print(r)

# payload = {
#     "task_name": "Do a thing...",
#     "task_status": "New Task"
# }

# r = requests.post(supabase_api,json=payload,headers=headers)
# print(r)

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[44m'
RESET = '\033[0m'
BOLD = '\033[1m'

# color_mode = globals().get((input("Type RED or GREEN to change the output color.")))

def get_supabase_tasks():
    response = requests.get(supabase_api,params=params,headers=headers).json()
    # response = response.json()
    for task in response:
        print(f"Task ID is: {task["id"]} \tTask Name is: {task["task_name"]} \t Task Status is: {task["task_status"]}")

# def display_tasks():
#     for task in get_supabase_tasks():
#         print(f"Task ID is: {task["id"]} \tTask Name is: {task["task_name"]} \t Task Status is: {task["task_status"]}")

get_supabase_tasks()