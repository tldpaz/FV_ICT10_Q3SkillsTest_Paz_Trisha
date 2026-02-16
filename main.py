def verify_account(username, password):

    # Username must be at least 7 characters
    if len(username) < 7:
        return "❌ Username must be at least 7 characters."

    # Password checks
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    if len(password) < 10:
        return "❌ Password must be at least 10 characters."

    if not has_letter:
        return "❌ Password must contain at least one letter."

    if not has_number:
        return "❌ Password must contain at least one number."

    return "✅ Account created successfully!"


# Main program
username = input("Enter username: ")
password = input("Enter password: ")

result = verify_account(username, password)
print(result)
