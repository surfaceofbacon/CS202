import random


def odd_random_number():
    num = random.randint(25, 129)
    if num % 2 == 1:
        print('your random odd number is', num)
    else:
        odd_random_number()


def main():
    odd_random_number()


if __name__ == '__main__':
    main()