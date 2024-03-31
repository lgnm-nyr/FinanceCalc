import math

# Functions to make the breaks for easier reading
def start_speech():
    print('=' * 150)
    print()

def end_speech():
    print()
    print('=' * 150)



# Making functions so that it becomes easier to restart when someone misspells something
def intro():

    #general opening text and choosing an option
    start_speech()
    print('''Investment - to calculate the amount of interest you'll earn on your investment
          \nBond\t   - to calculate the amount you'll have to pay on a home loan\n''')
    option = input("Enter either 'investement' or 'bond' from the menu above to proceed: ")
    end_speech()

    #making the way the user input investment and bond not matter
    option = option.lower()

    #option paths for investment and bond
    if option == "investment" :
        investment()
    elif option == "bond" :
        bond()    
    #If they misspell/Choose an unavailable option ->Error then restart
    else :
        start_speech()
        print("You can only pick Investment or Bond")
        end_speech()

        ending()



# Function for the investment system
def investment():

    # finding out all the required numbers to calculate with
    start_speech()
    deposit = float(input('''Enter the amount of money you are depositing"
                          to the nearest pound(£): '''))
    interest_rate = float(input('''Enter the interest rate at which
                                you wish to grow your money at in %: '''))
    num_years = float(input("Enter the amount of years you plan to invest for: "))
    interest_type = input("Enter the type of interest you would like to use (Simple or Compound): ")
    end_speech()

    # Formatting the variables so they can be used in the upcoming calculations
    # - variables changed so that they fit mathmatical formulas and so it is quicker to type out
    p = deposit
    r = interest_rate/100
    t = num_years
    interest_type = interest_type.lower()

    if interest_type == "simple":
        #Maths
        total = p * (1 + (r * t))

        #Result(rounded to 2dp so it makes sense money wise)
        start_speech()
        print(f'''The total amount of money £{deposit} becomes after {num_years} years
              with a simple interest rate of {interest_rate}% is £{round(total,2)}''')
        end_speech()

        #More calcs?
        ending()

    elif interest_type == "compound":
        #Maths
        total = p * (math.pow((1 + r), t))

        #Result(rounded to 2dp so it makes sense money wise)
        start_speech()
        print(f'''The total amount of money £{deposit} becomes after {num_years} years
              with a compound interest rate of {interest_rate}% is £{round(total,2)}''')
        end_speech()

        #More calcs?
        ending()

    else:
        #Error msg
        start_speech()
        print("You can only pick Simple or Compound types of investment")
        end_speech()

        #More calcs?
        ending()



#Function for bond system
def bond():

    #Number inputs
    start_speech()
    house_value = float(input('''Enter the current value of the house
                              you wish to assess in pounds(£): '''))
    interest_rate = float(input('''Enter the yearly interest rate at
                                which your bond will be applied with in %: '''))
    num_months = float(input('''Enter the number of number of months
                             you wish to take to repay the bond: '''))
    end_speech()

    # Fomratting numbers so that calculations work properly,
    # also providing different names to fit mathmatical formulae and to type it quicker
    p = house_value
    i = (interest_rate/100)/12
    n = num_months

    #Maths
    repayment = (i * p)/(1 - (1 + i)**(-n))

    #Result(rounded to 2dp so it makes sense money wise)
    start_speech()
    print(f'''On a house of present value £{house_value},
          a bond of {num_months} months with a yearly interest rate of {interest_rate}%,
          \nYou would have to repay £{round(repayment,2)} every month''')
    end_speech()

    #More calcs?
    ending()



#Function to restart or stop after making a calculation
def ending():

    #General message
    start_speech()
    restart_option = input('''If you would like to calculate another investment or bond,
                           please enter \"restart!\"
                           \nOtherwise, please enter anything else
                           \n''')
    end_speech()

    #If yes - rerun the function, if no, stop the program with a goodbye message
    if restart_option == "restart":
        intro()
    else:
        start_speech()
        print("Thanks for using this service! Goodbye!")
        end_speech()

def main():
    intro()

#Actually run the system
if __name__ =="__main__" :
    main()
