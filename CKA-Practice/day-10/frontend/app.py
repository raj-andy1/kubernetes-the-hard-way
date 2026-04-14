import os
import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

st.set_page_config(page_title="Notes App", page_icon="📝", layout="centered")
st.title("📝 Simple Notes App")

st.subheader("Create a note")

with st.form("create_note_form"):
    title = st.text_input("Title")
    content = st.text_area("Content")
    submitted = st.form_submit_button("Save note")

    if submitted:
        try:
            response = requests.post(
                f"{BACKEND_URL}/notes",
                json={"title": title, "content": content},
                timeout=5,
            )
            if response.status_code == 200:
                st.success("Note saved")
            else:
                st.error(f"Backend error: {response.text}")
        except Exception as exc:
            st.error(f"Could not connect to backend: {exc}")

st.divider()
st.subheader("Saved notes")

try:
    response = requests.get(f"{BACKEND_URL}/notes", timeout=5)
    if response.status_code == 200:
        notes = response.json()
        if not notes:
            st.info("No notes yet")
        else:
            for note in notes:
                with st.container():
                    st.markdown(f"### {note['title']}")
                    st.write(note["content"])
                    st.caption(f"ID: {note['id']}")
                    st.divider()
    else:
        st.error(f"Backend error: {response.text}")
except Exception as exc:
    st.error(f"Could not load notes: {exc}")