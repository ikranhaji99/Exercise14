# Q1: Use the open and read methods to slurp the entire contents of your pelican.txt file

file = open('pelican.txt', 'r')
all_of_it = file.read()
print(all_of_it)
# Q2 :What data type is the output?
print(type(all_of_it))

# Q3: Now, write some code that will read the pelican.txt file into a list and then output the number of items within
#the list.

my_file= open("pelican.txt" , 'r')
my_file_list = my_file.readlines()
print(my_file_list)

print(len(my_file_list))

# Q4: Now use a loop to iterate over and print the contents of the file. Be sure not to include any blank lines in the
# output.

my_file= open("pelican.txt" , 'r')
for x in my_file:
    print(x, end= '')


my_file.close()
