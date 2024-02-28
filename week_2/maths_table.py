# to make a maths table
# name : synthia wangui
# date :22/02/2024

#set  the dimensions of  the table
rows = 5
columns = 5

# creat the multiplication table
for i in range (1,rows+1):
    for j in range (1,columns+1):
        #calculate the product and print it
        x = i * j
        print(str(x*3) + "\t",end =" ") # adjust the width as needed
        print () # move to the next row
                    

