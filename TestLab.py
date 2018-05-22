notes = open("Notes", "r+")
notes.seek(70,0)
check = notes.read(1)
assign = ""
bool = True
while check != "]":
    notes.seek(71,0)
    assign = notes.read(4)
    print(assign)
    notes.seek(75,0)
    while bool == True:
        if notes.read(1) == ",":
            notes.seek(76,0) # 76 is a variable that gets added on
            assign = notes.read(4)
            print(assign)
        else:
            check = "]"
            bool = False
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