import requests
import json

public_api = "sb_publishable_IDd6uV8uzhOlbK3p94DoNw_4ePJkiZ5"
supabase_url = "https://eyjofdmiyocyeksjixoy.supabase.co/rest/v1/TaskList"

params = {"select":"*"}
headers = {"apikey": public_api,
    "Authorization": f"Bearer {public_api}"}

create_persistent_task = input("Type a task to add it to Supabase: ")

def post_supabase_tasks():
    payload = {
        "task_name": f"{create_persistent_task}",
        "task_status": "New Task"
    }
    r = requests.post(supabase_url,json=payload,headers=headers)
    print(r.status_code)

post_supabase_tasks()

def get_supabase_tasks():
    response = requests.get(supabase_url,params=params,headers=headers).json()
    # response = response.json()
    for task in response:
        print(f"Task ID is: {task["id"]} \tTask Name is: {task["task_name"]} \t Task Status is: {task["task_status"]}")

# def display_tasks():
#     for task in get_supabase_tasks():
#         print(f"Task ID is: {task["id"]} \tTask Name is: {task["task_name"]} \t Task Status is: {task["task_status"]}")

get_supabase_tasks()