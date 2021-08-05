#Speed Conversion Program

# Welcome line
print('Welcome to this Speed Conversion Porgram')
#taking name
name = input('What is your name?').title().strip()
print('Hello '+name+'!')
#Asking What type of conversion
print('\nEnter 1 to convert Miles/hour to Meter/seconds')
print('\nEnter 2 to convert meter/second to miles/hours')
while True:
    x = input('Enter your section')
    y = int(x)   #taking input in interger form only
    # Logic for Mph to Mps
    if y==1:
        mph = float(input('\nEnter speed in Miles/hour :'))
        mps = mph*0.4474
        mps = round(mps,2)
        print('\nYour speed in Meter/second is '+str(mps)+' mps.')
    # Logic for Mps to Mph
    elif y==2:
        mps = float(input('\nEnter speed in Meters/second :'))
        mph = mps / 0.4474
        mph = round(mph, 2)
        print('\nYour speed in Miles/hour is ' + str(mph) + ' mph.')

    else:
        print("\nEnter a valid Selection")
    for_quit = input('Enter y to quit')
    if for_quit == 'y':
        quit()
    else:
        continue
