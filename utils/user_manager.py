from utils.user import User
from utils.dicegame import DiceGame

class UserManager:
    def __init__(self):
        self.user = User()
        self.dicegame = DiceGame(self.user)

    def main_menu(self):
        while True:
            try:
                print("<------------------------->")
                print("|  Welcome to Dice Game!  |")
                print("<------------------------->")
                print("| 1. Register             |")
                print("| 2. Log-in               |")
                print("<------------------------->")
                print("| 3. Exit                 |")
                print("<------------------------->")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.user.clear_screen()
                    self.register()
                elif choice == 2:
                    self.user.clear_screen()
                    self.login()
                elif choice == 3:
                    self.user.clear_screen()
                    print("Exiting...")
                    quit()
                else:
                    self.user.clear_screen()
                    print("Please enter a valid choice from the menu.")

            except ValueError:
                print("Please enter a valid choice from the menu.")

    def register(self):
        while True:
            print("<------------------------->")
            print("|        REGISTER         |")
            print("<------------------------->")
            username = input(" Enter a username: ")

            if self.user.validate_username(username):
                break

            while True:
                password = input(" Enter a password: ")
                
                if self.user.validate_password(password):
                    self.user.save_user(username, password)
                    print("User registered successfully!")
                    break

    def login(self):
        while True:
            try:
                print("<------------------------->")
                print("|          LOG-IN         |")
                print("<------------------------->")

                username = input(" Enter your username: ")
                password = input(" Enter your password: ")

                if self.user.load_user(username, password):
                    print("Login successful!")
                    self.dicegame.game_menu(username)
                    break
                else:
                    print("Username or password invalid.")
            
            except FileNotFoundError:
                print("No user found.")
                return None

    