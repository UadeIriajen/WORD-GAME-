WORDS = {"Gold": 4, "Bold": 4, "Mold": 4}

def main():
    print("WELCOME TO THE GAME!!")
    print("Your letters are:")
    print(" o l h G d m B")

    while WORDS:
        guess = input("What's the word? ").strip().capitalize()

        if guess in WORDS:
            points = WORDS.pop(guess)
            print(f"Great! You got {points} points!") 
        else:
            print("Try again ^_^")

    print("\n🎉 Game Over! You found all the words!")

main()

