#While Loop
def main():
    while True:
        #INPUT
        # prompt the user to enter an expression in the format X y Z (x and z are intergers and y is the sign)
        user_input = print(input("Enter an expression: "))

        #PROCESS
        # valiate the expression format
        # use the split method to split the expression at the space " "
        expression_data = user_input.split(" ")
        # if the length of the resulting list is not 3 then invalid format
        if len(user_input) != 3:
            print("Invalid Format")
            continue
        
        # validate that X and Z are integers
        X = user_input[0]
        Z = user_input[2]
        # convert to int
        try:
            int(user_input)
        # if converting causes an exception, then invalid format
        except:
            print("Invalid Format")
        

        
   

    

    # validate that Y is an acceptable operator (+, -, *, /)
        # use and if statement to determine if Y == + or - or * or /
        # invalid format if not

    # validate that when Y is "/" Z is not 0
        # use if: if Y == / and Z == 0: divide by 0 error

    # do the math

    #OUTPUT
    #print the output to the user
main()