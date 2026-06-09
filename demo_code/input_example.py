# Program to Convert lbs to kgs 
# INPUT (getting the data that will be processed)
# prompt user to enter weight in lbs
user_weight = float(input("Enter weight in lbs: "))

# PROCESING
# use a conversion factor to convert lbs to kgs (2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg    #data types for assignment statemnts have to match(a str + str)

# OUTPUT
# print the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kgs.")