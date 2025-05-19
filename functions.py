FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_weekly_goals(filepath="weekly_goals.txt"):
    with open(filepath, 'r') as file_local:
        weekly_goals_local = file_local.readlines()
    return weekly_goals_local

def write_weekly_goals(weekly_goals_arg, filepath="weekly_goals.txt"):
    with open(filepath, 'w') as file:
        file.writelines(weekly_goals_arg)

def get_overall_goals(filepath="overall_goals.txt"):
    with open(filepath, 'r') as file_local:
        overall_goals_local = file_local.readlines()
    return overall_goals_local

def write_overall_goals(overall_goals_arg, filepath="overall_goals.txt"):
    with open(filepath, 'w') as file:
        file.writelines(overall_goals_arg)
