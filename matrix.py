# create a 2d list
d2_list= [[1,7,8],[3,5,6],[5,8,9]]
print(d2_list)

# finding lengh of 2d list row
row = len(d2_list)
print("The total rows are", row)

# finding lengh of 2d list column
col = len(d2_list[0])
print("The total columns are", col)

# accesing elements in a 2d list
hiiiiiiii_item = d2_list[1][1]
print("The special number is...  " , hiiiiiiii_item)

# adding values in an empty metrix
print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
matrix = []
rows = int(input("HoW MAny RoWS? "))
cols = int(input("HoW MAny COlOUmns? "))
n=0
for i in range(rows):
    li = []
    for e in range(cols):
        n=int(input("ENtEr A ValUE NoW! "))
        li.append(n)
    matrix.append(li)
    
print(matrix)

# accesing each value in the 2d list and printing them
for row_index,row in enumerate(d2_list):
    for val_index,value in enumerate(row):
        print("row ",row_index, "coluumn ",val_index, ": ", value)
