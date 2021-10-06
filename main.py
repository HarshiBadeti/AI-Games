# Python program to convert uppercase to lowercase

# take input
string = input('Enter any string: ')

# convert uppercase to lowercase
new_string =''
for i in string:
    if(ord(i) >= 65 and ord(i) <= 90):
        new_string = new_string + chr((ord(i) + 32))
    else:
        new_string = new_string + i

# print lowercase string
print('In Lower Case:',new_string)
