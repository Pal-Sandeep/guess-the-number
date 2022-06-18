import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry,Please guess again. Too low🔽.')
        elif guess > random_number:
            print('Sorry, Please guess again. Too high🔼.')

    print(f'Yupp, Badhai Ho!🥳 You have guessed the number {random_number} correctly!!✅✅✅')

guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # in a case both are equal.(low = high)
        feedback = input(f'Is {guess} too high🔼 (H/h), too low🔽 (L/l), or correct✅ (C/c)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yupp! The computer guessed your number, {guess}, correctly!!✅✅✅')



computer_guess(20)