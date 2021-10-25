import random

# Define a function that asks the user for input and DOESN'T QUIT until the user returns something valid
# In this case, "valid" means an integer between 1 and 100 (inclusive)


def get_input():

    a = True

    while a:

        try:
            user_input = int(input("Enter a valid number between 1 and 100: "))
            if type(user_input) == int and 1 <= user_input <= 100:
                a = False
                return user_input
            else:
                print("😡😡😡😡 Enter a valid number")
        except:
            print("Clever 🥸, now enter a valid number")


def compare_input(user, answer):
    if user == answer:
        return True, f"You won! {answer} billion ₩"
    elif user < answer:
        return False, "higher"
    elif user > answer:
        return False, "lower"

        # Define your main() function


def main():
    # Set a random number between 1 & 100
    answer = random.randint(0, 100)
    print("Rules:\n1. Player is not allowed to stop playing.\n2. The Player who refuses to play will be eliminated.\n3. the Games may be terminated if the majority agrees.\n Good luck!😈")
    while True:
        inp = get_input()
        win, result = compare_input(inp, answer)

        print(result)

        if win:
            break


if __name__ == "__main__":
    main()
