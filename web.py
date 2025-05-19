import streamlit as st
import functions

todos = functions.get_todos()
weekly_goals = functions.get_weekly_goals()
overall_goals = functions.get_overall_goals()

# Function to add a new todo
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

# Function to add a new weekly goal
def add_weekly_goal():
    new_goal = st.session_state["new_weekly_goal"] + "\n"
    weekly_goals.append(new_goal)
    functions.write_weekly_goals(weekly_goals)

# Function to add a new overall goal
def add_overall_goal():
    new_goal = st.session_state["new_overall_goal"] + "\n"
    overall_goals.append(new_goal)
    functions.write_overall_goals(overall_goals)

# Main app
st.title("My Productivity App")
st.subheader("Organize your tasks and goals effectively!")

# Tabs for different sections
tabs = st.tabs(["Todos", "Weekly Goals", "Overall Goals"])

# Todos Tab
with tabs[0]:
    st.header("Todos")
    st.write("Manage your daily tasks here.")
    for index, todo in enumerate(todos):
        checked = st.checkbox(todo, key=todo)
        if checked:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()
    st.text_input(label="Add a new todo", placeholder="Add a new todo...",
                  on_change=add_todo, key='new_todo')

# Weekly Goals Tab
with tabs[1]:
    st.header("Weekly Goals")
    st.write("Set and track your weekly goals.")
    for index, goal in enumerate(weekly_goals):
        checked = st.checkbox(goal.strip(), key=f"weekly_goal_{index}")
        if checked:
            weekly_goals.pop(index)
            functions.write_weekly_goals(weekly_goals)
            del st.session_state[f"weekly_goal_{index}"]
            st.rerun()
    st.text_input(label="Add a new weekly goal", placeholder="Add a new weekly goal...",
                  on_change=add_weekly_goal, key='new_weekly_goal')

# Overall Goals Tab
with tabs[2]:
    st.header("Overall Goals")
    st.write("Define your long-term goals.")
    for index, goal in enumerate(overall_goals):
        checked = st.checkbox(goal.strip(), key=f"overall_goal_{index}")
        if checked:
            overall_goals.pop(index)
            functions.write_overall_goals(overall_goals)
            del st.session_state[f"overall_goal_{index}"]
            st.rerun()
    st.text_input(label="Add a new overall goal", placeholder="Add a new overall goal...",
                  on_change=add_overall_goal, key='new_overall_goal')
