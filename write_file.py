# Q1: TO DO: Write a line of code to create a file handle to open and append to a file called pelican.txt')

pelican_file = open('pelican.txt' , 'a')

# Q2: TO DO: Append the following line to the file using the write method of the file handle:- A wonderful bird is the pelican- ')

pelican_file.write('A wonderful bird is the pelican')

# Q3 : Append the following second line using the write method: “His bill holds more than his belican.”

pelican_file.write('\nHis bill holds more than his belican.')

# Q4: Create a list that contains the following lines:

myList = ["\nHe can take in his beak,\n" , "Enough food for a week,\n",  "But I’m damned if I see how the helican.\n"]

# Q5: Append this list to the file using the writelines method.
pelican_file.writelines(myList)

# writelines is a function that allows us to attach a list with different things into the file.
# '\n is required to make a new line so the text is not written on the same line.