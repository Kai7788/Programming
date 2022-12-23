import sys

#Declare the function called 'main()'
def main(argv):
    list_length = len(argv)
    print("The list has " +str(list_length) + " attributes!")
    counter = 0
    for x in argv:
        print("The " + str(counter) + " value of the inputed arguments is: " + str(x))
        counter += 1

#If this Script is executed the attribute __name__ will change to "__main__ and thus call the main funcion"
if __name__ == "__main__":
    #Call the main function
    main(sys.argv)