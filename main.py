import re
from js import document

def validate_account(event=None):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    message_div = document.getElementById("message")

    # Username check
    if len(username) < 7:
        message_div.innerHTML = "Username must be at least 7 characters long."
        message_div.className = "message error"
        return

    # Password checks
    if len(password) < 10:
        message_div.innerHTML = "Password must be at least 10 characters long."
        message_div.className = "message error"
        return

    if not re.search(r"[A-Za-z]", password):
        message_div.innerHTML = "Password must contain at least one letter."
        message_div.className = "message error"
        return

    if not re.search(r"[0-9]", password):
        message_div.innerHTML = "Password must contain at least one number."
        message_div.className = "message error"
        return

    # Success
    message_div.innerHTML = "Account created successfully!"
    message_div.className = "message success"

# Connect the button click to the Python function
create_btn = document.getElementById("createBtn")
create_btn.addEventListener("click", validate_account)
