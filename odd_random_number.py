import random


def get_user_input():
    low = int(input('Please enter your lower integer: '))
    high = int(input('Please enter your higher integer: '))
    user_even_odd = int(input('enter a zero for odd, and one for even: '))
    return high, low, user_even_odd


def odd_random_number(lower=1, higher=100):
    num = random.randint(lower, higher)
    if num % 2 == 1:
        print('your random odd number is', num)
    else:
        odd_random_number(lower, higher)


def even_random_number(lower=1, higher=100):
    num = random.randint(lower, higher+1)
    if num % 2 == 0:
        print('your random odd number is', num)
    else:
        even_random_number(lower, higher)


def main():
    user_high, user_low, even_odd = get_user_input()
    if even_odd == 0:
        odd_random_number(user_low, user_high)
    elif even_odd == 1:
        even_random_number(user_low, user_high)
    else:
        print('Invalid inputs')


if __name__ == '__main__':
    main()
