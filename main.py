#variables
loopReset = False #condition for the first while loop

#constant variables
DELIVERY_CHARGE = 3 #delivery charge

#Array/List
#list of all the pizzas and their prices
PIZZA_NAMES = ["Peri-Peri Beef - $8.50", "BBQ Meatlovers - $8.50", "Supreme - $8.50", "Double Bacon Cheeseburger - $8.50", "Godfather - $8.50", "Mr. Wedge - $8.50", "Vegorama - $8.50", "Grand Supreme - $13.50", "Loaded Meatlovers - $13.50", "Chicken & Camembert - $13.50", "Pepperoni & Parmesan - $13.50", "Garlic Prawn - $13.50"]
#list of all pizza prices
PIZZA_PRICES = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50,]

#functions
#checks if the order is for pickup or delivery   
def orderMethod():
    global orderMethodValid
    orderMethodValid = False #condition which is changed if the input is deemed valid
    
    while not orderMethodValid:
        getOrderMethod = input("Is the order for delivery? (y/n) \n")
            
        if getOrderMethod == "y" or getOrderMethod == "Y":
            global forDelivery
            forDelivery = True #sets the program to delivery mode
            orderMethodValid = True #sets the loop condition to true stopping it from repeating
            global totalCost
            totalCost = totalCost + DELIVERY_CHARGE
            print("$" + '{0:.2f}'.format(DELIVERY_CHARGE) + " added to Total Cost \n- Cost currently $" + '{0:.2f}'.format(totalCost) + "\n")
            print("Delivery mode selected -")
        elif getOrderMethod == "n" or getOrderMethod == "N":
            global forPickup
            forPickup = True #sets the program to pickup mode
            orderMethodValid = True #sets the loop condition to true stopping it from repeating
            print("Pick-up mode selected -")
        elif getOrderMethod == "**": #sets the order reset variable to true and breaks the function/while loop.
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            break
        else:
            print("Not a valid answer, try again. \n")

#gets the customers name
def customerName():
    global quitFunction
    quitFunction = False #because this function is used within another function this is used to break out of both functions
    global customerNameValid
    customerNameValid = False #condition which is changed if the input is deemed valid
    while not customerNameValid:
        global getCustomerName
        getCustomerName = input("What is the customer's name? \n")
    
        if getCustomerName.isspace() or not getCustomerName: #this is to check if the input is only spaces or is blank
            print("Not a valid answer, try again. \n")
        elif getCustomerName == "**": #sets the order reset variable to true and breaks the function/while loop.
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            quitFunction = True
            break
        else:
            customerNameValid = True #sets the loop condition to true stopping it from repeating

#gets the customers phone number and area code            
def customerPhone():
    global quitFunction
    quitFunction = False #because this function is used within another function this is used to break out of both functions
    global customerPhoneValid
    customerPhoneValid = False #condition which is changed if the input is deemed valid
    while not customerPhoneValid:
        global getCustomerPhone
        getCustomerPhone = input("What is the customer's phone number & area code? (no spaces) \n")
             
        if getCustomerPhone == "**": #sets the order reset variable to true and breaks the function/while loop.
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            quitFunction = True
            break       
        try:
            int(getCustomerPhone) #checks that the input is an integer
        except ValueError:  
            print("Not a valid answer, try again. \n") 
        else:
            customerPhoneValid = True #sets the loop condition to true stopping it from repeating

#gets the customers street number
def customerStreetNumber():
    global quitFunction
    quitFunction = False #because this function is used within another function this is used to break out of both functions
    global customerStreetNumberValid
    customerStreetNumberValid = False #condition which is changed if the input is deemed valid
    while not customerStreetNumberValid:
        global getCustomerStreetNumber
        getCustomerStreetNumber = input("What is the customer's street number? \n")
    
        if getCustomerStreetNumber.isspace() or not getCustomerStreetNumber: #this is to check if the input is only spaces or is blank
            print("Not a valid answer, try again. \n")
        elif getCustomerStreetNumber == "**": #sets the order reset variable to true and breaks the function/while loop.
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            quitFunction = True
            break
        else:
            customerStreetNumberValid = True #sets the loop condition to true stopping it from repeating

#gets the customers street name
def customerStreetName():
    global quitFunction
    quitFunction = False #because this function is used within another function this is used to break out of both functions
    global customerStreetNameValid
    customerStreetNameValid = False #condition which is changed if the input is deemed valid
    while not customerStreetNameValid:
        global getCustomerStreetName
        getCustomerStreetName = input("What is the customer's street name? \n")
    
        if getCustomerStreetName.isspace() or not getCustomerStreetName: #this is to check if the input is only spaces or is blank
            print("Not a valid answer, try again. \n")
        elif getCustomerStreetName == "**": #sets the order reset variable to true and breaks the function/while loop.
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            quitFunction = True
            break
        else:
            customerStreetNameValid = True #sets the loop condition to true stopping it from repeating

#gets the customers suburb    
def customerSuburb():
    global quitFunction
    quitFunction = False #because this function is used within another function this is used to break out of both functions
    global customerSuburbValid
    customerSuburbValid = False #condition which is changed if the input is deemed valid
    while not customerSuburbValid:
        global getCustomerSuburb
        getCustomerSuburb = input("What is the customer's suburb? \n")
    
        if getCustomerSuburb.isspace() or not getCustomerSuburb: #this is to check if the input is only spaces or is blank
            print("Not a valid answer, try again. \n")
        elif getCustomerSuburb == "**": #sets the order reset variable to true and breaks the function/while loop
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            quitFunction = True
            break
        else:
            customerSuburbValid = True #sets the loop condition to true stopping it from repeating

#a main function which calls all the functions which ask for the delivery details           
def deliveryDetails():
    customerName()
    if quitFunction == True: #this checks if the function which has just been called has set the quitFunction variable to true and if so it will break this entire function
        return 
    customerPhone()
    if quitFunction == True:
        return
    customerStreetNumber()
    if quitFunction == True:
        return
    customerStreetName()
    if quitFunction == True:
        return
    customerSuburb()
    if quitFunction == True:
        return        

#a main function which calls all the functions which ask for the pickup details  
def pickupDetails():
    customerName()
    if quitFunction == True:
        return  
        
    customerPhone()
    if quitFunction == True:
            return

#gets how many pizzas the customer wants to order        
def pizzaAmountSelector():
    global pizzaNumberValid
    pizzaNumberValid = False #condition which is changed if the input is deemed valid
    while not pizzaNumberValid:
        global getPizzaNumber
        getPizzaNumber = input("How many pizzas would the customer like to order? \n")
             
        if getPizzaNumber == "**": #sets the order reset variable to true and breaks the function/while loop.
            global exitProgram
            exitProgram = True
            print("You have cancelled the order. \n \n")
            return
        try:
            int(getPizzaNumber) #checks that the input is an integer
        except ValueError:
            print("Not a valid answer, try again. \n")
            continue
        if int(getPizzaNumber) <= 0 or int(getPizzaNumber) > 6:
            print("Only allowed to order between 1 - 5 pizzas.")          
        else:
            pizzaNumberValid = True #sets the loop condition to true stopping it from repeating

#prints out the list of pizzas and their prices
def pizzaList():
    print("")
    print("Pizza list -")
    for n in range (len(PIZZA_NAMES)):
        print (str(n) + ".", PIZZA_NAMES[n])
    print("")
    

#gets the pizzas that the customer wants to order and calculates the total order cost
def pizzaSelector():
    print("Select Pizza: ")
    for n in range(int(getPizzaNumber)):
        pizzaChoiceValid = False #condition which is changed if the input is deemed valid
        while not pizzaChoiceValid:
            global getPizzaChoice
            getPizzaChoice = input("What pizza would the customer like to order? \n")
                 
            if getPizzaChoice == "**": #sets the order reset variable to true and breaks the function/while loop.
                global exitProgram
                exitProgram = True
                print("You have cancelled the order. \n \n")
                return
            try:
                int(getPizzaChoice) #checks that the input is an integer
            except ValueError:
                print("Not a valid answer, try again. \n")
                continue
            if int(getPizzaChoice) < 0 or int(getPizzaChoice) > 11: #check if the pizza number is actually a valid number
                print("That is not a valid pizza. \n")
            else:
                pizzaChoiceValid = True #sets the loop condition to true stopping it from repeating
           
        global totalCost 
        totalCost = totalCost + PIZZA_PRICES[int(getPizzaChoice)] #adds the cost of the pizza to the total cost
        orderedPizzas.append(PIZZA_NAMES[int(getPizzaChoice)]) #adds the pizza to the list of ordered pizzas

#prints the order receipt and asks if the operator wants to make another order or cancel the program completely
def orderReceipt():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("                       - Order Receipt -")                       
    print("Order Includes: ", orderedPizzas)
    print("Final order cost (inc. GST):", "$" + '{0:.2f}'.format(totalCost))
    print("Customer Name:", getCustomerName)
    print("Customer Phone:", getCustomerPhone)
    if forDelivery == True:
        print("Customer Street Number:", getCustomerStreetNumber)
        print("Customer Street Name:", getCustomerStreetName)
        print("Customer Suburb:", getCustomerSuburb,)
    print("Thank you for ordering with Dream Pizza!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        
    global orderCompleteValid        
    orderCompleteValid = False
    
    while orderCompleteValid == False:
        getOrderComplete = input("Would you like to take another order? (y/n) \n")
            
        if getOrderComplete == "y" or getOrderComplete == "Y":
            orderCompleteValid = True
        elif getOrderComplete == "n" or getOrderComplete == "N":
            orderCompleteValid = True
            global loopReset
            loopReset = True
            global exitProgram
            exitProgram = True
            print("You have shutdown the program.")
            break
        else:
            print("Not a valid answer, try again. \n")    
        
    

#main routine
while not loopReset: #first loop which works in conjunction with the secondary loop, this loop only cancels if at the end of an order the operator says they do not want to do another order
    exitProgram = False 
    while not exitProgram: #secondary loop which allows the program to restart when the quit key is used rather than cancelling completely
        orderedPizzas = [] #a blank list which will later store the pizzas the customer has ordered
        totalCost = 0.00 #the total cost of the order
        forDelivery = False #if the order is for delivery
        forPickup = False #if the order if for pickup        
    
        #a welcome message at the start of an order
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("          Welcome to the Dream Pizza ordering system!")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("- To quit this program simply enter ** at any time. \n")
    
        #check if the order is for pickup or delivery
        orderMethod()
        
        #required to break the loop
        if exitProgram == True:
            break
    
        #check what type of information the operator should ask for
        if forPickup == True:
            pickupDetails()
        elif forDelivery == True:
            deliveryDetails()
        
        #required to break the loop    
        if exitProgram == True:
            break        
    
        #pizza stuff
        pizzaAmountSelector()
        
        #required to break the loop    
        if exitProgram == True:
            break   
        
        #pizza stuff
        pizzaList()
        
        #pizza stuff
        pizzaSelector()
        
        #required to break the loop    
        if exitProgram == True:
            break
        
        #display an order receipt
        orderReceipt()
        
        

    
    

    
