#this is a letter counter described in section 7 of Automate the Boring Stuff
#made before watching the example
import datetime

beginTime = datetime.datetime.now() ##for time needed

message = "This is a message for all the letters within to be counted"
listMessage = list(message.lower().replace(" ", "")) #converts message string to list so i can use list methods
messageLetters = {} #this is a dict of letters and counts in the message
count = 0 #this is a counter to be used to report count and change the message


while len(listMessage) > 0:
    workingLetter = listMessage[0]
    count = listMessage.count(workingLetter) #counts the occurrence of first index in the message
    for i in range(count):
        listMessage.remove(workingLetter) #completely removes i from the message so that effort is not duplicated
    messageLetters.update({workingLetter:count}) #returns the working letter and its count

print(messageLetters)
endTime = datetime.datetime.now() 
print(str(endTime - beginTime)) ##how quickly this executes

#####
#####this is the actual solution
print(' - - -  actual solution - - - - \n')

beginTime = datetime.datetime.now() ##for time needed

message = "This is a message for all the letters within to be counted"
count = {}

for i in message.lower():
    count.setdefault(i, 0)
    count[i] = count[i]+1

print(count)
endTime = datetime.datetime.now() 
print(str(endTime - beginTime)) ##how quickly this executes

###what was learned: it's a good idea to understand the built-in methods because they are probably faster than a homebrew solution.
###the actual solution was apprx 2x the speed of my homebrew solution