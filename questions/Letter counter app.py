#letter counter program

#welcome line
print('Welcome to my letter counting app')
#taking mname
name = input('What is your name?').title().strip()
print('Hello '+name+'!')
#telling what can I do
while True:
    print('I will count the numbers of letter occur in your message')
    #taking message and which letter should be counted
    message = input('Enter you message : ')
    message=message.lower()
    letter = input('Which letter should I count in your message? :')
    letter = letter.lower()
    #main logic
    letter_count = message.count(letter)
    #final output
    print('Your message has total '+str(len(message))+' letters in it.')

    if letter_count>1:
        print('\n'+name+'Your message has '+str(letter_count)+' '+letter+"'s in it.")
    elif letter_count==1:
        print('\n' + name + 'Your message has ' + str(letter_count) + ' ' + letter + "'s in it.")
    else:
        print('\nSorry'+name+'Your message does not contain and'+letter+'in it')
    for_quit = input('Enter y to quit')
    if for_quit == 'y':
        quit()
    else:
        continue