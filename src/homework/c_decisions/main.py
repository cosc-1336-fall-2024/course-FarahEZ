import decisions

def main():
    num=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))

    ratio=decisions.get_options_ratio(num,num2)

    print(decisions.get_faculty_rating(ratio))

main()