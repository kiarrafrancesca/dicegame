import os
import datetime

class User:
    def __init__(self, userinfos="userinfos.txt", rankings="rankings.txt"):
        self.userinfos = userinfos
        self.rankings = rankings

    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def press_return(self):
        input("Press 'enter' to return.")
        self.clear_screen()

    def validate_username(self, username):
        if len(username) < 4:
            print("Username must be at least 4 characters long.")
            return False
        else:
            try:
                with open(self.userinfos, "r") as file:
                    for line in file:
                        if f"{username}" in line:
                            print("Username already exists.")
                            return False
            
            except FileNotFoundError:
                pass
            return True

    def validate_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        return True

    def save_user(self, username, password):
        try:
            with open(self.userinfos, "a") as file:
                file.write(f"{username}, {password}")
        
        except Exception as e:
            print(f"Error saving user: {e}")
        
    def load_user(self, username, password):
        try:
            with open(self.userinfos, "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(", ")
                    if username == stored_username and password == stored_password:
                        return True
        
        except FileNotFoundError:
            print("File not found.")
        return False
        
    def save_score(self, username, user_score, stages_won):
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.rankings, "a") as file:
                file.write(f"{date_time} / {username}:     Score - {user_score},      Wins - {stages_won}")
        
        except Exception as e:
            print(f"Error saving... {e}")

    def load_scores(self):
        try:
            if not os.path.exists(self.rankings):
                with open(self.rankings, "w"):
                    pass
        
        except FileNotFoundError:
            return None