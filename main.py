correct_username = "admin"
correct_password = "1234"

# Maximum attempts
max_attempts = 6
attempt = 0

while attempt < max_attempts:
    print("\nLogin System")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check username first
    if username == correct_username:
        
        # Nested if for password
        if password == correct_password:
            print("✅ Login successful! Welcome.")
            break
        else:
            print("❌ Incorrect password.")
    
    else:
        print("❌ Incorrect username.")

    attempt += 1
    remaining = max_attempts - attempt
    print(f"Attempts remaining: {remaining}")

# If attempts are used up
if attempt == max_attempts:
    print("\n🚫 Too many failed attempts. Access locked.")
