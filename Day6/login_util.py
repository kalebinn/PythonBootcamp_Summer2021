from user_database import users 

def check_user_credentials(username, password):
    if username in users:
        if password == users[username]:
            print("Successfully logged in")
        else:
            print("Invalid Password. You can reset your password with this link.")
    else:
        print("Invalid username. Please sign up for CUNYFirst.")