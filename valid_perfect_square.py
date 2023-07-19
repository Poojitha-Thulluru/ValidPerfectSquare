def is_perfect_square(num: int) -> bool:
    for val in range(1, num):
        if val * val == num:
            return True
        if val * val > num:
            return False


try:
    number = int(input("Enter the number : "))
    print(is_perfect_square(number))
except ValueError:
    print("Invalid Input, Please enter only integer")
