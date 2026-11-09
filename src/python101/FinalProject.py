import subprocess
import requests
import os
import sys

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[44m'
RESET = '\033[0m'
BOLD = '\033[1m'

users_tasks = {}

def add_tasks():
    add_task_input = input("\nEnter the name of a task to add: ")
    users_tasks[add_task_input] = "New Task"
    print(f"\n\t{YELLOW}Your task: {add_task_input}, was added to the list.{RESET}")

def complete_task():
    mark_task_complete_input = input("\nTo mark a task complete, type the name of a task: ")
    if mark_task_complete_input in users_tasks:
        users_tasks[mark_task_complete_input] = "Completed"
        print(f"\n\t{GREEN}Your task: {mark_task_complete_input}, has been completed.{RESET}")
    else:
        print("\n\tTask doesn't exist.")

def view_tasks():
    print()
    for task,status in users_tasks.items():
        print(f"\tTask: {task}\t Status: {status}")
    
def delete_task():
    task_to_delete = input("\nEnter the name of a task to delete it: ")
    try:
        del users_tasks[task_to_delete]
        print(f"\n\t{RED}The task {task_to_delete} has been deleted.{RESET}")
    except KeyError:
        print("\n\tUnable to find that task!")

def filter_tasks():
    print()
    for task,status in users_tasks.items():
        if status == "Completed":
            print(f"\t{GREEN}Completed:\t {task}{GREEN}")
        else:
            print(f"\t{YELLOW}Need Attention:\t {task}{YELLOW}")

def exit_app():
    print("Good Bye!")
    sys.exit()

def call_api():
    url = "https://evergreen-team-n77j0qa2.atlassian.net/rest/api/3/issue/KAN-6"
    API_KEY = os.getenv("UX_CLASS_JIRA_KEY")
    email = "jnzz5505@evergreen.edu"
    response = requests.get(url,auth=(email,API_KEY))
    response = response.json()

    print(f"""
    \tYou have retrieved a Jira Task with the following information\n
    \t\t{BOLD}Project: {RESET} {response["fields"]["project"]["name"]}
    \t\t{BOLD}Summary: {RESET} {response["fields"]["summary"]}
    \t\t{BOLD}Person: {RESET} {response["fields"]["creator"]["displayName"]}
    \t\t{BOLD}Status: {RESET} {response["fields"]["status"]["name"]}
    """)

# Dispatch pattern for main menu.
MENU_DISPATCH= {
    1: [add_tasks,"Add a new task"],
    2: [complete_task, "Complete a task"],
    3: [view_tasks, "View all tasks."],
    4: [delete_task, "Delete a task"],
    5: [filter_tasks, "View tasks by status"],
    6: [exit_app, "Exit"],
    7: [call_api, "View my Jira Task"]
    }

def display_menu(menu):
    for key, value in menu.items():
        print(f"{key}: {value[1]}")

def main_menu(menu_selection):
    MENU_DISPATCH[menu_selection][0]()

subprocess.run("clear") # if on Windows, change from clear to cls

print(f"{BLUE}Welcome to the task Manager.\n{RESET}")
display_menu(MENU_DISPATCH)

while True:
    try:
        main_menu(int(input("\nEnter an integer to select a menu option: ")))
    except Exception:
        print("You must enter an integer from the menu options. Try again!")
        continue


# Removed in favor of dispatch pattern.

# menu_selection = 0
# menu_redisplay = 0
# def main_menu():
#     print("""
#     Main Menu for Task Actions
#     1. Create New
#     2. Complete
#     3. View All
#     4. Delete
#     5. Filter by Status
#     6. Exit
#     7. Retrieve Task from Jira!
#     """)

# while menu_selection != 6:
#     if menu_redisplay == 5:
#         menu_redisplay = 0
#         main_menu()
#     try:
#         menu_redisplay += 1
#         menu_selection = int(input("\nType an integer corresponding to the action you wish to take: "))
#     except:
#         print("\nYou must enter an integer!")
#         continue
#     if menu_selection == 1:
#         add_tasks()
#     elif menu_selection == 2:
#         complete_task()
#     elif menu_selection == 3:
#         view_tasks()
#     elif menu_selection == 4:
#         delete_task()
#     elif menu_selection == 5:
#         filter_tasks()
#     elif menu_selection == 6:
#         break
#     elif menu_selection == 7:
#         call_api()