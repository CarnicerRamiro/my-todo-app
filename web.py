import streamlit as st
import functions as f


todos = f.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"].strip() + '\n'
    if not (new_todo == "\n" or new_todo in todos):
        todos.append(new_todo)
        f.set_todos(todos)
    st.session_state["new_todo"] = ""


def remove_todo():
    for item in todos:
        if st.session_state[item]:
            todos.remove(item)
            f.set_todos(todos)
            del st.session_state[item]


st.title("My Todo App")
st.subheader("This is crazy!")
st.text("This is crazy 2!")

for todo in todos:
    st.checkbox(todo, on_change=remove_todo, key=todo)

st.text_input(label="Enter a TODO", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")
for i in st.session_state:
    print(i)
