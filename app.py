# app.py

import streamlit as st
from pathlib import Path
import os

st.set_page_config(
    page_title="CRUD File Manager",
    page_icon="📁",
    layout="centered"
)

# ---------------------------
# Helper Function
# ---------------------------

def get_all_items():
    p = Path(".")
    return list(p.rglob("*"))

# ---------------------------
# Title
# ---------------------------

st.title("📁 CRUD File Manager")
st.write("Manage Files & Folders using Streamlit")

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# ---------------------------
# Show Existing Files/Folders
# ---------------------------

st.subheader("📂 Existing Files & Folders")

items = get_all_items()

if items:
    for item in items:
        st.write(item)
else:
    st.info("No files/folders found.")

# ---------------------------
# Create File
# ---------------------------

if menu == "Create File":

    st.header("📄 Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("File already exists!")

        else:
            with open(file_name, "w") as file:
                file.write(content)

            st.success("File created successfully!")

# ---------------------------
# Read File
# ---------------------------

elif menu == "Read File":

    st.header("📖 Read File")

    file_name = st.text_input("Enter file name to read")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, "r") as file:
                data = file.read()

            st.text_area("File Content", data, height=300)

        else:
            st.error("File not found!")

# ---------------------------
# Update File
# ---------------------------

elif menu == "Update File":

    st.header("✏️ Update File")

    file_name = st.text_input("Enter file name to update")

    update_option = st.radio(
        "Choose Update Type",
        ["Overwrite", "Append"]
    )

    new_content = st.text_area("Enter new content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if update_option == "Overwrite":

                with open(file_name, "w") as file:
                    file.write(new_content)

            else:

                with open(file_name, "a") as file:
                    file.write(new_content)

            st.success("File updated successfully!")

        else:
            st.error("File does not exist!")

# ---------------------------
# Delete File
# ---------------------------

elif menu == "Delete File":

    st.header("🗑️ Delete File")

    file_name = st.text_input("Enter file name to delete")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)

            st.success("File deleted successfully!")

        else:
            st.error("File not found!")

# ---------------------------
# Rename File
# ---------------------------

elif menu == "Rename File":

    st.header("🔄 Rename File")

    old_name = st.text_input("Enter current file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("File renamed successfully!")

        else:
            st.error("File not found!")

# ---------------------------
# Create Folder
# ---------------------------

elif menu == "Create Folder":

    st.header("📁 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():

            st.error("Folder already exists!")

        else:

            p.mkdir()

            st.success("Folder created successfully!")

# ---------------------------
# Delete Folder
# ---------------------------

elif menu == "Delete Folder":

    st.header("❌ Delete Folder")

    folder_name = st.text_input("Enter folder name to delete")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()

            st.success("Folder deleted successfully!")

        else:
            st.error("Folder not found!")