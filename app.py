import streamlit as st

st.set_page_config(page_title="To-Do List App", page_icon="✅")
st.title("✅ To-Do List App")
st.caption("CodSoft Python Project — Shubham Kumar")

if "todos" not in st.session_state:
    st.session_state.todos = []

with st.form("add_form", clear_on_submit=True):
    task = st.text_input("Enter a new task")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    submitted = st.form_submit_button("Add Task")
    if submitted and task:
        st.session_state.todos.append({"task": task, "priority": priority, "done": False})
        st.success(f"Task added!")

st.divider()
st.subheader("Your Tasks")

if not st.session_state.todos:
    st.info("No tasks yet. Add one above!")
else:
    for i, todo in enumerate(st.session_state.todos):
        col1, col2, col3, col4 = st.columns([0.1, 0.6, 0.15, 0.15])
        with col1:
            done = st.checkbox("", value=todo["done"], key=f"check_{i}")
            st.session_state.todos[i]["done"] = done
        with col2:
            if done:
                st.markdown(f"~~{todo['task']}~~")
            else:
                st.markdown(todo["task"])
        with col3:
            color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            st.write(color[todo["priority"]] + " " + todo["priority"])
        with col4:
            if st.button("🗑️ Delete", key=f"del_{i}"):
                st.session_state.todos.pop(i)
                st.rerun()

if st.session_state.todos:
    completed = sum(1 for t in st.session_state.todos if t["done"])
    total = len(st.session_state.todos)
    st.divider()
    st.progress(completed/total if total > 0 else 0)
    st.caption(f"{completed} of {total} tasks completed")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mark All Done"):
            for t in st.session_state.todos:
                t["done"] = True
            st.rerun()
    with col2:
        if st.button("🗑️ Clear All"):
            st.session_state.todos = []
            st.rerun()