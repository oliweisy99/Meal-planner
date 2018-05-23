notes = open("Notes", "r+")
n = 70
notes.seek(n,0)
check = notes.read(1)
assign = ""
bool = True
#count = 0


if check == "[":
    while bool == True:
        notes.seek(n+1)
        assign = notes.read(4)
        #foodList[index].tags[count] = notes.read(4)
        n = n + 5
        notes.seek(n)
        if notes.read(1) == ",":
            #count = count + 1
            continue
        else:
            bool = False
            break

'''
        while fo.read(variable) != "]":
        if fo.read(i+1) where it is only reading one character == "[" and fo.read(whatever) != "]":
            assign = fo.read(read next 4 characters after)
            foodlist[index].tags[countvar] = assign
            if fo.read(amount after tag of 4 chars) == ","
                increment count variable and continue
            elif fo.read(whatever) ==  "]":
                colonCount = 0
                n = n - count
                index = index + 1
        loop until fo.read(wtever) == "]"
        then finish 
print(check)

'''