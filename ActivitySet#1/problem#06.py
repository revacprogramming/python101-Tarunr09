# Loops & Iterators

largest = 0
smallest = None
while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try :
         a= int(num)
        except:
            print("Invalid input")
            continue
        if smallest is None:
            smallest = a
        elif a < smallest:
            smallest = a
        elif a > largest:
            largest = a

print("Maximum is", largest)
print("Minimum is", smallest)