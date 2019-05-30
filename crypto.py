

array=[]
array2=[]
alpha=[' !', '@', '#', '$', '%', '^', '&', '*', '(', ')',
'-', '_', '+', '=', "{", '[', '}', ']', ':', ';',
'"', "'", '<', '>', ',', '.', '?', '/', '|', '\\', 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', ' ']


userInput=input("Begin the program?")
print("Menu")

while userInput!="0":
    print("1. Update character substitution")
    print("2. Write secret message")
    print("3. Encrypt a file")
    print("4. Decrypt a file")
    print("0.Exit")
    userInput=input("Enter option:")
    if userInput=="1":
        print("Updated character substitution")
    if userInput=="2":
        fileName=input("Enter filename without extension:")
        messageLine1=input("Enter message line or <enter> to end:")
        messageLine2=input("Enter message line or <enter> to end:")
        messageLine3=input("Enter message line or <enter> to end:")
    if userInput=="3":
        fileName=input("Enter filename without extension:")
        f = open(fileName+".txt", "r")

        for element in f:
            print(element)
            array.append(element)



        for num in range(len(array)):
            for element in array[num]:
                for i in element:
                    if i!="\n":
                        array2.append(i)
            for item in array2:
                position=alpha.index(item)
                print(position+1,end=" ")
    
    if userInput=="4":
        fileName=input("Enter filename without extension:")
        f = open(fileName+".txt", "r")
        for i in f:
            posi=alpha.index(i)
            print(posi,end=" ")
    userInput=input("Do you wish to end the program, Enter 0 to quit")








            


        

