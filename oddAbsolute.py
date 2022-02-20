def calculateAbsolute():
    
    # This first line is provided for you

    # Function to determine difference between user entered number and 21. 
    def absoluteDifference(number):
        if number < 21 and number >= 0:
            difference = 21 - number
        elif number < 0:
            difference = (number * -1) + 21
        elif number > 21:
            difference =  (number - 21) * 2
        else:
            difference = 0
        
        return int(difference)

    # While loop to error check user's input. Continues until numerical value
    # entered.
    while True:   
        try:
            in_num  = float(input("Enter a number: "))
            break
        except:
            print("Please enter a numerical value.")
            continue

    difference = absoluteDifference(in_num)
    print(difference)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()