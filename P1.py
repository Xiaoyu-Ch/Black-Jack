import p1_random as p1
rng = p1.P1Random()


class CardGame:
    def __init__(self):
        self.reset_game()
        self.statlock=0

    def reset_game(self):
        self.player_hand = 0
        self.dealer_hand = 0
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0
        self.games = 0

    def start_game(self):
         self.reset_game()
         self.games += 1
         print(f"START GAME #{self.games}")
         self.play()

    def play(self):
         while True:

            if self.statlock == 0:
                card = rng.next_int(13) + 1
                if card == 1:
                    print(f"\nYour card is a ACE!")
                    self.player_hand += 1
                elif card == 11:
                    print(f"\nYour card is a JACK!")
                    self.player_hand += 10
                elif card == 12:
                    print(f"\nYour card is a QUEEN!")
                    self.player_hand += 10
                elif card == 13:
                    print(f"\nYour card is a KING!")
                    self.player_hand += 10
                else:
                    print(f"\nYour card is a {card}!")
                    self.player_hand += card
                print(f"Your hand is: {self.player_hand}")

            if self.player_hand == 21:
                print("BLACKJACK! You win!")
                self.player_wins += 1
                self.player_hand = 0
                self.games += 1
                print(f"START GAME #{self.games}")
                continue

            elif self.player_hand > 21:
                print("You exceeded 21! You lose.")
                self.dealer_wins += 1
                self.player_hand = 0
                self.games += 1
                print(f"START GAME #{self.games}")
                continue

            while True:
                print("\n1. Get another card")
                print("2. Hold hand")
                print("3. Print statistics")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice in ['1', '2', '3', '4']:
                    break
                else:
                    print("Invalid input! Please enter an integer value between 1 and 4.")

            if choice == '1':
                self.statlock = 0
                continue
            elif choice == '2':
                self.dealer_hand = rng.next_int(11) + 16
                print(f"\nDealer's hand: {self.dealer_hand}")
                print(f"Your hand is: {self.player_hand}")
                self.determine_winner()
                self.statlock = 0
                continue
            elif choice == '3':
                self.print_statistics()
                self.statlock = 1

            elif choice == '4':
                exit()

    def determine_winner(self):
        if self.dealer_hand > 21 or self.player_hand > self.dealer_hand:
            print("You win!")
            self.player_wins += 1
            self.player_hand = 0
            self.games += 1
            print(f"START GAME #{self.games}")
        elif self.player_hand < self.dealer_hand:
            print("Dealer wins!")
            self.dealer_wins += 1
            self.player_hand = 0
            self.games += 1
            print(f"START GAME #{self.games}")
        else:
            print("It's a tie! No one wins!")
            self.ties += 1
            self.player_hand = 0
            self.games += 1
            print(f"START GAME #{self.games}")

    def print_statistics(self):
        total_games = self.player_wins + self.dealer_wins + self.ties
        player_win_percentage = (self.player_wins / total_games * 100) if total_games > 0 else 0
        print(f"\nNumber of Player wins: {self.player_wins}")
        print(f"Number of Dealer wins: {self.dealer_wins}")
        print(f"Number of tie games: {self.ties}")
        print(f"Total # of games played is: {total_games}")
        print(f"Percentage of Player wins: {player_win_percentage:.1f}%")

if __name__ == "__main__":
    game = CardGame()
    while True:
        game.start_game()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break