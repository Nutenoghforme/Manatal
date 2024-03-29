#Exercise 2: Randomness Test
#In a lottery game, there is a container which contains 50 balls numbered from 1 to 50. The lottery game consists in picking 10 balls out of the container, and ordering them in ascending order. Write a Python function which generates the output of a lottery game (it should return a list). Also describe which unit tests you could implement to test the output of your function.

import random
START = 1
END   = 50
LIMIT = 11 #stop+1 = 10+1 = 11

def random_lottery_number():
    number = [random.randint(START, END) 
        for _ in range(1, LIMIT)]
    number.sort()
    return number
if __name__ == '__main__':
    print("The List of the Lottery Number are : " , random_lottery_number())
