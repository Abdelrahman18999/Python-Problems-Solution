hight = eval(input("Enter the hight of the diamond: "))
shapechar = input("Enter which character you want to draw the diamond?  ")
for i in range(1, hight+1, 2):
    spaces1 = (hight-i)//2
    print(spaces1*' ', shapechar*i, spaces1*' ', sep='')
for j in range(hight-2, 0, -2):
    spaces2 = (hight-j)//2
    print(spaces2*' ', shapechar*j, spaces2*' ', sep='')
