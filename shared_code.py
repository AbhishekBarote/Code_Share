import streamlit as st
import time
import os

# Configuration
CODE_FILE = "shared_code.py"
REFRESH_INTERVAL = 2  # Seconds

# Set up the page
st.set_page_config(page_title="Real-Time Code Sharing", layout="wide")
st.title("Real-Time Code Sharing")
st.write("Write and share Python code in real-time with your friend on the same network.")

# Function to load code from the shared file
def load_code():
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, "r") as file:
            return file.read()
    return ""

# Function to save code to the shared file
def save_code(code):
    with open(CODE_FILE, "w") as file:
        file.write(code)

# Main app logic
def main():
    # Create two columns for side-by-side editing and viewing
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Edit Code")
        new_code = st.text_area(
            "Write your Python code here:",
            value=load_code(),
            height=400,
            key="code_editor"
        )
        if st.button("Save Code"):
            save_code(new_code)
            st.success("Code saved and shared!")

    with col2:
        st.subheader("Live Preview")
        code_placeholder = st.empty()

        # Continuously refresh the code preview
        while True:
            current_code = load_code()
            code_placeholder.code(current_code, language="python")
            time.sleep(REFRESH_INTERVAL)

# Run the app
if __name__ == "__main__":
    main()