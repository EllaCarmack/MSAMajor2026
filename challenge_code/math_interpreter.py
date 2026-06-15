#While Loop
def main():
    while True:
        #INPUT
        # prompt the user to enter an expression in the format X y Z (x and z are intergers and y is the sign)
        user_input = input("Enter an expression: ")

        #PROCESS
        # valiate the expression format
        # use the split method to split the expression at the space " "
        expression_data = user_input.split(" ")
        # if the length of the resulting list is not 3 then invalid format
        if len(expression_data) != 3:
            print("ERROR: Invalid Format")
            continue
        
        # validate that X and Z are integers
        X = expression_data[0]
        Y = expression_data[1]
        Z = expression_data[2]
        # convert to int
        try:
            X = int(X)
            Z = int(Z)
        # if converting causes an exception, then invalid format
        except:
            print("ERROR: Invalid Format")

        # validate that Y is an acceptable operator (+, -, *, /), if statement to determine if Y == + or - or * or /
        if Y != "+" and Y != "-" and Y != "*" and Y != "/":

            # invalid format if not
            print("ERROR: Invalid Format")
            continue

        # validate that when Y is "/" Z is not 0, use if: if Y == / and Z == 0: divide by 0 error
        if Y == "/" and Z == 0:
            print("ERROR: Divide by 0 error")
            continue
  
        # do the math
        if Y == "+":
            answer = X + Z
        if Y == "-":
            answer = X - Z
        if Y == "*":
            answer = X * Z
        if Y == "/":
            answer = X / Z
        #OUTPUT, print the output to the user
        print(answer)

        re_prompt = input("Do you want to evaluate another expression? (Press y to continue):")
        if re_prompt == "y":
            continue
        else:
            break     
main()