#automate the boring stuff
#chapter 3 - functions
#collatz program - program that performs a collatz function on a given number

#defines collatz function
def collatz(number):
    if number % 2 == 0:
        number = (number // 2)
    elif number % 2 == 1:
        number = 3 * number + 1
    return number


#prompts user to enter a number
guess = None
while guess is None:
    try:
        guess = int(input('Please enter a number: '))
    except ValueError:
        print('Please enter a valid integer.')


#repeats collatz function until 1 is reached
print(guess)

while guess != 1:
    guess = collatz(guess)
    print(guess)
