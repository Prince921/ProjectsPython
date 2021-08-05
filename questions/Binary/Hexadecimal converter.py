print('Welcome to Binary/Hexadecimal convertor program')
max_value = int(input('Enter a Decimal number'))
decimal = list(range(1,max_value))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print('Generating lists...')

print('Using Slices we will now show a portion of each list : ')
lower_range = int(input("Where do you want to start : "))
upper_range = int(input("What number should we stop : "))

print('\nDecimal Value from '+str(lower_range)+' to '+str(upper_range)+' : ')
for num in decimal[lower_range-1:upper_range]:
    print(num)

print('\nBinary Value from '+str(lower_range)+' to '+str(upper_range)+' : ')
for num in binary[lower_range-1:upper_range]:
    print(num)

print('\nHexadecimal Value from '+str(lower_range)+' to '+str(upper_range)+' : ')
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)