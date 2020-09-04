# Write a function that expresses an imperial volume using the largest units possible. The function will take the
# number of units as its first parameter, and the unit of measure (cup, tablespoon or teaspoon) as its second
# parameter. Return a string representing the measure using the largest possible units as the function’s only
# result. For example, if the function is provided with parameters representing 59 teaspoons then it should
# return the string “1 cup, 3 tablespoons, 2 teaspoons”.
# Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to 3 teaspoons.
# one cup - 16 tablespoons
# one cup - 48 teaspoons
# one tablespoon - 3 teaspoons

def main():
    unitNumber = int(input("unit Number: "))
    unitMeasure = input("unitMeasure: ")
    answer = largestPossible(unitNumber, unitMeasure)
    print(answer)

def largestPossible(unitNumber, unitMeasure):
    cup = 0
    tablespoons = 0
    teaspoons = 0
    if(unitMeasure == "cup"):
        cup = unitNumber
        return "{0} cup, {1} tablespoons, {2} teaspoons".format(cup, tablespoons, teaspoons)
    elif(unitMeasure == "tablespoons"):
        if(unitNumber >= 16 ):
            cup = unitNumber//16
            tablespoons = unitNumber%16
        else:
            tablespoons = unitNumber        
        return "{0} cup, {1} tablespoons, {2} teaspoons".format(cup, tablespoons, teaspoons)
    elif(unitMeasure == "teaspoons"):
        if(unitNumber >= 48 ):
            cup = unitNumber//48
            unitNumber = unitNumber - cup*48
        if(unitNumber >= 3):
            tablespoons = unitNumber//3
            teaspoons = unitNumber%3
        else:
            teaspoons = unitNumber   
        return "{0} cup, {1} tablespoons, {2} teaspoons".format(cup, tablespoons, teaspoons)



