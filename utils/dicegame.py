from utils.user import User
import random
import datetime

class DiceGame:
    def __init__(self):
        self.user = User()

    def game_menu(self):
        while True:
            try:
                print("<------------------------->")
                print("|  Welcome to Game Menu!  |")
                print("<------------------------->")
                print("| 1. Play Game            |")
                print("| 2. Show Top Scores      |")
                print("<------------------------->")
                print("| 3. Log Out              |")
                print("<------------------------->")

                choice = int(input(" Enter your choice: "))

                if choice == 1:
                    self.user.clear_screen()
                    self.play_game()
                elif choice == 2:
                    self.user.clear_screen()
                    self.show_top_scores()
                elif choice == 3:
                    self.user.clear_screen()
                    print("Logging out...")
                    quit()
                else:
                    self.user.clear_screen()
                    print("Please enter a valid choice from the menu.")

            except ValueError:
                print("Please enter a valid choice from the menu.")

    def play_game(self, username):
        print(f"Starting game as {username}\n")

        self.user_score = 0
        self.cpu_score = 0
        self.stage = 1
        self.stages_won = 0

        while True:
            self.round = 1
            self.user_point = 0
            self.cpu_point = 0

            print("Dice rolling...")
            
            while self.round <= 3:
                user_dice = random.randint(1, 6)
                cpu_dice = random.randint(1, 6)

                print(f"{username} rolled: {user_dice}")
                print(f"CPU rolled: {cpu_dice}")

                if user_dice > cpu_dice:
                    print(f"---{username} win this round.")
                    self.user_point += 1
                elif user_dice < cpu_dice:
                    print("---CPU win this round.")
                    self.cpu_point += 1
                else:
                    print("*It's a tie.*")

                self.round += 1
            
            while self.user_point == self.cpu_point:
                print("\nTie-breaker round!")
                user_dice = random.randint(1, 6)
                cpu_dice = random.randint(1, 6)

                print(f"{username} rolled: {user_dice}")
                print(f"CPU rolled: {cpu_dice}")

                if user_dice > cpu_dice:
                    print(f"---{username} win this round.")
                    self.user_point += 1
                elif user_dice < cpu_dice:
                    print("---CPU win this round.")
                    self.cpu_point += 1

            if self.user_point > self.cpu_point:
                print(f"\n{username} won this stage.")
                self.user_score += self.user_point + 3
                self.stages_won += 1

                print(f"Total Points: {self.user_score} | Stage/s Won: {self.stages_won}")

                while True:
                    try:
                        choice = int(input("\nDo you wish to (1) continue to next stage or (2) quit the game?: "))

                        if choice == 1:
                            self.stage += 1
                            break
                        elif choice == 2:
                            print(f"Game over. You won {self.stages_won} with a total points of {self.user_score}")
                            self.user.save_score()
                            return
                        else:
                            print("Please enter a valid choice from the menu.")

                    except ValueError:
                        print("Please enter a valid choice from the menu.")

            elif self.user_point < self.cpu_point:
                print(f"\nYou lost this stage, {self.user.username}. It's game over.")
                self.user.save_score()
                return

    def show_top_scores(self):
        try:
            with open(self.user.rankings, "r") as file:
                lines = file.readlines()

            if not lines:
                print("\nNo games played yet. Play a game to see top scores.")
                return
            
            rankings = []
            for line in lines:
                parts = line.strip().split(" / ")
                date_time = parts[0].strip()
                date_time_1 = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
                username_2 = parts[1]. split(": ")
                username = username_2[0].strip()
                user_score_2 = username_2[1].split(", ")
                user_score = int(user_score_2[0].split(" - ")[1].strip())
                stages_won = int(user_score_2[1].split(" - ")[1].strip())

                rankings.append((date_time_1, username, user_score, stages_won))

            rankings.sort(key=lambda x: x[2], reverse=True)

            print("\n\t\t\t----TOP SCORES----")
            print("Rank\tDate&Time\t\tPlayer\t\tScores\t\tWins")
            for rank, (date_time_1, username, user_score, stages_won) in enumerate(rankings[:10], 1):
                print(f"{rank}\t{date_time_1}\t{username}\t\t{user_score}\t\t{stages_won}")
        
        except FileNotFoundError:
            print("\nNo games played yet. Play a game to see top scores.")
            return