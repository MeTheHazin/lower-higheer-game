from gameData import data
import random

end = False




a = random.choice(data)
b = random.choice(data)
score = 0


print("A " + a["name"], a["follower_count"])
print("B " + b["name"], b["follower_count"])


def answer():
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


def win():
    global score
    global a
    global b
    global guess
    a = b
    b = random.choice(data)
    score += 1

    

def lose():
    global score
    global a
    global b
    global guess
    print(f"you lose. your final score is {score} ")


while end == False:

    guess = str(input("Who has more followers? Type 'A' or 'B' \n")).lower()

    if answer() == guess:
        win()
        print("A " + a["name"], a["follower_count"])
        print("B " + b["name"], b["follower_count"])
    else:
        lose()
        break











    


    
