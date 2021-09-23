# this is a program to say hello and ask for a name

print('Hello world!')
print('What is your name?') #ask for their name
myName = input()
print('It\'s good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge= input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')