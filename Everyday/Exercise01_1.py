import random

def guessing_game():
    answer = random.randint(0,100)
    
    while True:
        guess = int(input("Enter the number: "))
        if answer > guess:
            print("Too low")
            continue
        elif answer < guess:
            print("Too high")
            continue
        else:
            print("Just right")
            break
        
guessing_game()

#while True에 ()빼기
