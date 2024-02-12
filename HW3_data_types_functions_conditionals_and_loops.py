#Power of a Number
#x = int(input("Enter a base value:"))
#y = int(input("Enter of an exponent value:"))
#def power_function(x, y): 
#    answer = 1
#    for i in range(y):
#        answer = answer * x
#    return answer
#print(power_function(x,y))

#Minimum and Maximum
#list = []
#n = int(input("Enter number of elements in your list: "))
#for i in range(0,n):
#    elements = int(input())
#    list.append(elements)
#
#def sort(list):
#    minimum = min(list)
#    maximum = max(list)
#    return minimum, maximum
#
#print(sort(list))

#Check Leap Year
#year = int(input("Enter a year: "))
#def find_leap(year):
#    if year % 400 == 0:
#        return True
#    elif year % 4 == 0 and year % 100 != 0:
#        return True
#    else:
#        return False 
#print(find_leap(year))

#Calculate BMI (weight in kilograms / (height in meters)^2)
#weight = int(input("Enter a weight (kg): "))
#height = int(input("Enter a height (meters): "))
#def BMI(weight, height): 
#    if weight > 0 and height > 0:
#        result = weight / (height**2)
#        return result
#    else:
#        print("Enter a valid height and weight")
#print(BMI(weight, height)+" (kg/m^2)")

#Rotate digits
#number = int(input("Enter a number: "))
#def rotate_digit(number):
#    last_digit = str(number % 10)
#    front_digits = str(number // 10)
#    result = last_digit + front_digits
#    return result
#print(rotate_digit(number))

#Minimum and Maximum but with Loops
#list = list(input("Enter
#def find_min(x,y)

#Vowels
#word = str(input("Enter a word: "))
#def count_vowels(word):
#    count = 0
#    for characters in str(word):
#        if characters in "aeiouAEIOU":
#            count = count + 1
#    return count
#print(count_vowels(word))

#Digital Root
integer = int(input("Enter an integer: "))
def sum_digits(integer):
    integer = str(integer)
    digits = list(integer)
    sum = 0
    for i in digits:
        sum = sum + int(i)
    return sum
print(sum_digits(integer))
