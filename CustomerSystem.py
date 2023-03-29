# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv

def printMenu():
    print('''
            Customer and Sales System\n
            1. Enter Customer Information\n
            2. Generate Customer data file\n
            3. Report on total Sales (Not done in this part)\n
            4. Check for fraud in sales data (Not done in this part)\n
            9. Quit\n
            Enter menu option (1-9)
        ''')

def enterCustomerInfo():
    '''Gets the input for the information the user enters'''
    firstName = str(input("\nInput first name: "))
    lastName = str(input("\nInput last name: "))
    city = str(input("\nInput your city: "))
    postalCode = str(input("\nInput your postal code: "))
    if validatePostalCode(postalCode) == False:
        print("Invalid postal code")
        return False
    creditCard = str(input("\nInput your credit card: "))
    if validateCreditCard(creditCard) == False:
        print("Invalid credit card")
        return False

def validatePostalCode(postalCode):
    '''
        Validates the inputted postal code. Parses through the .csv file, 
        looking at the first 3 characters of every row and checking it against
        the inputted postal code
    '''
    with open("postal_codes.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter ="|")
        for row in reader:
            if postalCode == row[0]:
                csv_file.close()
                return True
    csv_file.close()
    return False

def validateCreditCard(creditCard):
    '''Validates the credit card using the lunh algorithm'''
    if len(creditCard) < 9:
        print("Invalid credit card")
        return False
    ############## ASK MR HO IF YOU CAN USE THIS FUNCTION
    elif creditCard.isnumeric() == False:
        print("Invalid credit card")
        return False
    # Sets variables needed for the algorithm
    sum1 = 0
    sum2 = 0
    sumTotal = 0
    # Reverse the credit card
    reverseCreditCard = creditCard[::-1]
    # Parses through the reversed credit card number
    for i in range(1, len(reverseCreditCard)+1):
        if i % 2 == 1:
            sum1 = sum1 + int(reverseCreditCard[i-1])
        else:
            evenDigit = int(reverseCreditCard[i-1]) * 2
            if evenDigit > 9:
                evenDigit = str(evenDigit)
                for x in evenDigit:
                    x = int(x)
                    sum2 = sum2 + x
            else:
                sum2 = sum2 + evenDigit
    sumTotal = sum1 + sum2
    sumTotal = str(sumTotal)
    if sumTotal[-1] == "0":
        return True
    return False

def generateCustomerDataFile():
    pass    # Remove this pass statement and add your own code below

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below

while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        if enterCustomerInfo() == False:
            continue


    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")