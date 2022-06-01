
def add(a, b):
    a=int(input('Enter the first number: '))
    b=int(input('Enter the second number: '))


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
