#Right Triangle

#import math library for doing square_root
import math
print('Welcome to this Right Triangle solver Porgram')
name = input('What is your name?').title().strip()
print('Hello '+name+'!')
while True:
    #asking for base and hypotenous
    base = float(input("Enter base of triangle : "))
    height = float(input("Enter Height of triangle : "))
    #Logic for Area
    area = 1/2*base*height
    #logic for Hypotenous
    hypo = math.sqrt(base**2 + height**2)
    area = round(area, 3)
    hypo = round(hypo, 3)
    #Final Answer
    print('The area of given Triangle is : '+str(area))
    print('The hypotenuse of given triangle is : '+str(hypo))
    for_quit = input('Enter y to quit')
    if for_quit == 'y':
        quit()
    else:
        continue
