

def load_hours(amount):
    minutes = 50
    return str(amount) + ':' + str(minutes)


def main():
    load_amount = int(input('How many loads do you need to do?: '))
    print(str(load_hours(load_amount)))


if __name__ == '__main__':
    main()
