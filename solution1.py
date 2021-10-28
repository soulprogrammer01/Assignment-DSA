# taking user input as string
string = input("Enterthe string : ")
# taking user input as character
char= input("Enter the word : ")

# initializing frequency variable to 0
frequency = 0
# iterating over the string
for i in string:
   # checking the match of the words whether its lower or upper case
   if i == char.upper() or i == char.lower() :
      # incrementing frequency on match
      frequency += 1
# printing the count
print(frequency)