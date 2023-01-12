#   Welcome to Streamlit :wave:
# The fastest way to build and share data apps.
#
# Streamlit lets you turn data scripts into shareable web apps in minutes,
# not weeks. It’s all Python, open-source, and free! And once you’ve
# created an app you can use our Community Cloud platform to deploy, manage, and share your app!

import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)




st.title("My Todo App")
st.subheader("This is in fact, my reincarnation of the my to do App")
st.write("This app is to improv your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()




st.text_input(label="my input", placeholder="Add new todo ....",
              on_change=add_todo, key='new_todo')

print("HElllllo")

st.session_state



# x = st.slider("Select a value")
#  st.write(x, "squared is ", x*x)


