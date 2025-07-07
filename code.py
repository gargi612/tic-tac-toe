def count(my_map,row,column,user_map):
    sum=0
    for i in range(0,3):
        new_row=row+1-i
        if(new_row<0 or new_row>9):
            break
        for j in range(0,3):
            new_column=column+1-j
            if(new_column<0 or new_column>9):
                break
            if(my_map[new_row][new_column]=="*"):
                sum=sum+1
            else:
                continue
    user_map[row][column]=sum
    return sum

def display():
    for i in range(0,10):
        for j in range(0,10):
            print(user_map[i][j],end="|")
        print()

def game(my_map,x,y,user_map):
    result=count(my_map,x,y,user_map)
    if (result!=0):
        return 
    else:
        for i in range(0,3):
            new_row=x+1-i
            if(new_row<0 or new_row>9):
                break
            for j in range(0,3):
                new_column=y+1-j
                if(new_column<0 or new_column>9):
                    break
                else:
                    game(my_map,new_row,new_column,user_map)
        

my_map=[[" "," "," "," "," ","*"," "," "," "," "],
        [" "," "," "," "," "," "," "," ","*"," "],
        ["*"," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," ","*"," "," "],
        [" "," "," ","*"," "," "," "," "," "," "],
        [" "," "," "," "," ","*"," "," "," "," "],
        [" ","*"," "," "," "," "," "," "," "," "],
        [" "," "," ","*"," "," "," "," "," "," "],
        [" "," "," "," "," "," ","*"," "," "," "],
        [" "," ","*"," "," "," "," "," "," "," "]]
user_map=[[" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "]]
for q in range(0,21):
    if(q==20):
        print("Yow win!")
        break
    else:
        print("enter the row and the column")
    user_input=list(map(int,input().split()))
    row,column=user_input[0],user_input[1]
    if(my_map[row][column]=="*"):
        print("game over")
    else:
        if(my_map[row][column]==" "):
            game(my_map,row,column,user_map)
            display()

