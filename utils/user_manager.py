from utils.user import User
from utils.dicegame import DiceGame

def main_menu():
    user = User()
    usermanager = UserManager()
    
    while True:
        print("<------------------------->")
        print("|  Welcome to Dice Game!  |")
        print("<------------------------->")
        print("| 1. Register             |")
        print("| 2. Log-in               |")
        print("<------------------------->")
        print("| 3. Exit                 |")
        print("<------------------------->")

        choice = int(input(" Enter your choice: "))

        if choice == 1:
            user.clear_screen()
            usermanager.register()
        elif choice == 2:
            user.clear_screen()
            usermanager.login()
        elif choice == 3:
            user.clear_screen()
            print(" Exiting...")
            quit()
        else:
            user.clear_screen()
            print(" Please enter a valid choice from the menu..\n")

class UserManager:
    def __init__(self):
        self.user = User()
        self.dicegame = DiceGame()

    def register(self):
        while True:
            print("<------------------------->")
            print("|        REGISTER         |")
            print("<------------------------->")
            username = input(" Enter a username: ")

            if self.user.validate_username(username):
                while True:
                    password = input(" Enter a password: ")
                    
                    if self.user.validate_password(password):
                        self.user.save_user(username, password)
                        self.user.clear_screen()
                        print(" User registered successfully!\n")
                        return

    def login(self):
        while True:
            print("<------------------------->")
            print("|          LOG-IN         |")
            print("<------------------------->")

            username = input(" Enter your username: ")
            password = input(" Enter your password: ")

            if self.user.load_user(username, password):
                self.user.clear_screen()
                print("\n Login successful!\n")
                self.dicegame.game_menu(username)
                break
            else:
                self.user.clear_screen()
                print(" Username or password invalid.\n")