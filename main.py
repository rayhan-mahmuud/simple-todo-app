import streamlit as st
import utils


def add_todos():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(str(new_todo).capitalize())
    if len(new_todo) > 1 and new_todo != " ":
        utils.set_todos(todos)
    st.session_state["new_todo"] = ""


def clear_todos():
    removed_todos.clear()
    with open("removed_todos.txt", "w") as file:
        file.writelines(removed_todos)


st.title("ToDo App")
st.subheader("Make keeping track of your tasks easier!")
st.markdown("### Your ToDos:")
st.markdown("---")

todos = utils.get_todos()

for index, todo in enumerate(todos):
    key = f"todo_item{index}"
    checkbox = st.checkbox(label=todo, key=key)
    if checkbox:
        removed_todo = todos.pop(index)
        utils.set_todos(todos)
        del st.session_state[key]
        utils.store_removed_todo(removed_todo)
        st.rerun()

removed_todos = utils.get_removed_todos()

st.text_input("Enter a ToDo:", key="new_todo", on_change=add_todos)

if len(removed_todos) > 0:
    with st.expander("Completed ToDos"):
        st.write("Here are the todos you have completed. Well Done!")
        html_list = "<ul>" + "\n".join([f"<li>{item}</li>" for item in removed_todos]) + "</ul>"
        st.markdown(html_list, unsafe_allow_html=True)

        st.button("Clear", on_click=clear_todos)

