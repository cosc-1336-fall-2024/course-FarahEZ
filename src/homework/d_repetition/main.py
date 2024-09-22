import repetition

def main():
    menu=int(input("Enter number: 1 for factorial, 2 for sum of odd numbers, and 3 for exit."))

    if (menu==1):
        fac1=int(input("Enter a number "))
        while (0>=fac1 or fac1>=10):
            fac1=int(input("Enter a number between 0-10 "))
        print(repetition.get_factorial(fac1))
        print("Do you want to exit?")
    if (menu==2):
        odd=int(input("Enter a number "))
        while (0>=odd or odd>=10):
            odd=int(input("Enter a number between 0-10 "))
        print(repetition.sum_odd_numbers(odd))
        print("Do you want to exit?")
    if (menu==3):
        print("Do you want to continue?")

main()

