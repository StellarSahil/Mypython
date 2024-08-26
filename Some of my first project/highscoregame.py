import random

def game():
    sco = 1  # Initial score
    while sco >= 0:
        # To open the file and read the data
        with open("save.txt") as f:
            data = f.readlines()

        # Removing newline characters from data
        data = [line.strip() for line in data]

        # Ensure that data is in expected format
        if len(data) < 3:
            data = ["0", "0", "0"]  # Default values if the file is empty or corrupted

        # Intro
        print("Number guessing game")
        print("Guess a number between 1 to 1000")
        you = int(input())

        # AI random number generation
        ai = random.randint(1, 1000)

        # Finding the score
        if (ai - 200) <= you <= (ai + 200):
            sco = 100 - abs(ai - you)
        else:
            sco = 0

        # result and updating scores
        streak = int(data[0])
        Tscore = int(data[1])
        Hscore = int(data[2])

        if sco == 100:
            print(f"Pretty accurate, Your score {sco}")
        elif 60 <= sco < 100:
            print(f"Too close, Your score {sco}, The Number is {ai}")
        elif 0 < sco < 60:
            print(f"You are around it, Your score {sco}, The Number is {ai}")
        else:
            print(f"You lose, The Number is {ai}")
            streak = 0  # Reset streak if the player loses

        if sco > 0:
            streak += 1
            Tscore += sco

        # Update the highest score
        if Tscore > Hscore:
            Hscore = Tscore

        # Update the data to be written back to the file
        new_data = f"{streak}\n{Tscore}\n{Hscore}\n"

        # Writing updated data to the file
        with open("save.txt", "w") as f:
            f.write(new_data)

        # Print the final result
        print(f"Streak: {streak}, Total Score: {Tscore}, Highest Score: {Hscore}")
        
        # Optionally, end the game
        if sco == 0:
            break

# Run the game
game()