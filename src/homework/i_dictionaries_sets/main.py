#HW 7
"""from lists import get_lowest_list_values, get_highest_list_values 

def main():
    menu=int(input("Enter 1 to show highest and lowest value, Enter 2 to exit. "))

    while menu != 2:
        if (menu==1):
            val1=int(input("Enter a number "))
            val2=int(input("Enter a number "))
            val3=int(input("Enter a number "))
            thislist = [val1, val2, val3]
            print("Do you want to continue? Type another value or stop")
            val4=input("Enter a number or stop ")
            if (val4 != "stop"):
                thislist.append(int(val4))
                val5=input("Enter a number or stop ")
                while val5 != "stop":
                    thislist.append(int(val5))
                    val5=input("Enter a number or stop ")
            print ("The lowest value is: ",lists.get_lowest_list_values(thislist))
            print ("The highest value is: ",lists.get_highest_list_values(thislist))
        menu=int(input("Enter 1 to show highest and lowest value, Enter 2 to exit. "))
    
main()"""

from dictionary import add_inventory, remove_inventory_widget

def main():
    menu=int(input("Enter 1 to add or update item. Enter 2 to delete item. Enter 3 to exit. "))

    widgets={}

    while menu != 3:
        if (menu==1):
            widget_name=input("Enter the key ")
            quantity=int(input("Enter the quantity number "))
            widgets= add_inventory(widgets, widget_name, quantity)
        if (menu==2):
            widget_name=input("Enter the key ")
            print(remove_inventory_widget(widgets,widget_name))
        menu=int(input("Enter 1 to add or update item. Enter 2 to delete item. Enter 3 to exit. "))
main()
