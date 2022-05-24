def add(a, b):
    sum = int(a) + int(b)
    return sum

def main():
    a = input("Enter the values :")
    b = input("Enter the values :")

    c = add(a, b)
    print(c)
if __name__=="__main__":
    main()