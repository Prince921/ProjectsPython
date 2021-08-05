#Mathametical & Exponential Table

print('Welcome to this Mathametical & Exponential Table Porgram')
name = input('What is your name?').title().strip()
print('Hello '+name+'!')
while True:
    num = float(input('What number Mathametical & Exponential Table you want?'))
    print('Multiplication Table of '+str(num)+' is : ')
    for i in range(1,11):
        print('\t '+str(i)+' * '+str(num)+' = '+str(round(i*num,4)))

    print('Exponential Table of '+str(num)+' is : ')
    for i in range(1,11):
        print('\t '+str(num)+'^'+str(i)+' = '+str(round(num**i,4)))
    for_quit = input('Enter y to quit')
    if for_quit == 'y':
        quit()
    else:
        continue



