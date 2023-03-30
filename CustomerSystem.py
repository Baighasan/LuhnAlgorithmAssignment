# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv
import subprocess
import os

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
    global id
    # Creates a hidden txt file to store the user inputes
    hiddenDatabase = open("hiddenDatabase.txt", "a")
    # Hides the file from the user in file explorer using the subprocess library, executes only under certain conditions
    if id == 0:
        subprocess.check_call(["attrib","+H","hiddenDatabase.txt"])
    
    # General Customer info 
    firstName = str(input("\nInput first name: "))
    lastName = str(input("\nInput last name: "))
    city = str(input("\nInput your city: "))
    
    # Validates postal code
    postalCode = str(input("\nInput your postal code: "))
    while (len(postalCode) != 3) or (validatePostalCode(postalCode) == False):
        postalCode = input("\nInvalid postal code. Pease re-enter: ")
    
    # Validates credit card
    creditCard = str(input("\nInput your credit card: "))
    while (len(creditCard) < 9) or (validateCreditCard(creditCard) == False):
        creditCard = input("\nInvalid credit card. Please re-enter: ")
    
    # Appends the data to a hidden database to store it for later use when we need to generate the csv file
    id += 1
    hiddenDatabase.writelines(f"{id}|{firstName}|{lastName}|{city}|{postalCode}|{creditCard}\n")
    hiddenDatabase.close()
    
    print("\nSuccessfully inputted customer data\n")

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
    try:
        hiddenDatabase = open("hiddenDatabase.txt")
    except IOError:
        print("\nYou have not inputted any customer data.")
        return False
    hiddenDatabase.close()
    
    ####### FIX ERROR WHERE USER ENTERS BLANK NAME
    fileName = input("\nInput a name for your generated csv file. Try not to put any spaces. Do not end your file with .csv: ")
    filePath = input("\nInput the file path where you want the csv file to be generated. \nIf you are on a windows, seperate your path with \\. If you are on a mac, seperate your path with /. \nMake sure to end your file path with your correct slash. \nLeave blank to generate in current folder: ")
    
    if filePath == "":
        filePath = os.getcwd() + "\\" + fileName + ".csv"
    
    else:
        filePath = filePath + fileName + ".csv"
    
    try: 
        customerInfoFile = open(filePath, "a")
    except FileNotFoundError: 
        print("\nInvalid file path. Try again.")
    
    # Appends the header row
    customerInfoFile.write("id|First Name|Last Name|City|Postal Code|Credit Card\n")
    
    hiddenDatabase = open("hiddenDatabase.txt", "r")
    for line in hiddenDatabase:
        customerInfoFile.write(line)
    
    # This resets the hidden database for then next set of inputs
    hiddenDatabase.close()
    customerInfoFile.close()

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
id = 0

while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()


    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")