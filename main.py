from simple_term_menu import TerminalMenu
import csv
import random

ENGLISH = "english"
GERMAN = "german"
EXIT = "exit"

VERBS_FILENAME = "verbs.csv"
MOST_COMMON_FILENAME = "most_common.csv"


def learn(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        data = [row for row in reader]
        tot_data = len(data)
        i = 0

        print(f"Type '{EXIT}' when you want to quit")
        while True:
            i = i + 1
            data_idx = random.randint(0, tot_data)
            guess = input(f"[{i}] Meaning of '{data[data_idx][GERMAN]}': ").casefold()

            if guess == EXIT:
                print("Tschüss")
                return
            elif guess == data[data_idx][ENGLISH]:
                print("\t[V] Das ist richtig!")
            else:
                print(f"\t[X] Nope! Correct translation is: {data[data_idx][ENGLISH]}")


def main():
    options = ["Top 100 verbs", "Most common words"]

    terminal_menu = TerminalMenu(options)
    menu_idx = terminal_menu.show()

    if menu_idx == 0:
        learn(VERBS_FILENAME)
    elif menu_idx == 1:
        learn(MOST_COMMON_FILENAME)


if __name__ == "__main__":
    main()
