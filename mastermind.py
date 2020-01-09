import random

while(True):
    finish = input("Want to play? input 'q' to quit ")
    if finish == "q" :
        break
    secret_number = str(random.choice(list(range(1000,10000))))
    count = 1
    while(True):
        guess = input("Guess the secret number: ")
        everything_correct = sum([1 for i in range(4) if guess[i] == secret_number[i]])
        correct_num_wrong_position =  sum([1 for i in range(4) if (guess[i] in secret_number and guess[i]!=secret_number[i])])
        print("Numbers in the right position:",everything_correct,"\nNumers which are in the number but in the wrong position", correct_num_wrong_position)
        if everything_correct == 4:
            print("It took",count,"guess to get it right! Congrats!\n\n")
            break
        count += 1
    
