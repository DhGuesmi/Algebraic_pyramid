import os

#Function to print the pyramid
def print_pyramid(L):
    
    print(
    '''
                           ----------
                           |   {}   |
                      -------------------
                      |   {}   |   {}   |
                  ----------------------------
                  |   {}   |   {}   |   {}   |
             -------------------------------------
             |   {}   |   {}   |   {}   |   {}   |
        ----------------------------------------------
        |   {}   |   {}   |   {}   |   {}   |   {}   |
        ----------------------------------------------
    '''.format(L[0][0],
               L[1][0],L[1][1],
               L[2][0],L[2][1],L[2][2],
               L[3][0],L[3][1],L[3][2],L[3][3],
               L[4][0],L[4][1],L[4][2],L[4][3],L[4][4]))
    
    
#Function to sovle a pyramid with 3 values
def solve_pyramid(L,i,j):
    T = (L[i][j] , L[i+1][j] , L[i+1][j+1])
    if ("" not in T) or (T.count("") > 1):
        pass
    else:
        if L[i][j] == "":
            L[i][j] = L[i+1][j] + L[i+1][j+1]
        elif L[i+1][j] == "":
            L[i+1][j] = L[i][j] - L[i+1][j+1]
        else:
            L[i+1][j+1] = L[i][j] - L[i+1][j]

            
#Function to check the coherance of the solution
def check_coherance(L):
    Test = True
    for i in range(4):
        for j in range(i+1):
            if L[i][j] != L[i+1][j] + L[i+1][j+1]:
                Test = False
                break
    return Test
    
    
#Intializing the pyramid
L = [[""] , ["",""] , ["","",""] , ["","","",""] , ["","","","",""]]

#Filling the pyramid with values
for i in range(5):
    for j in range(i+1):
        while True:
            L[i][j] = "X"
            print_pyramid(L)
            number = input("Enter a number or press enter to skip: ")
            os.system('cls')
            if number == "":
                L[i][j] = number
                break
            try:
                L[i][j] = int(number)
                if L[i][j] < 0:  # if not a positive int print message and ask for input again
                    print("Sorry, input must be a positive integer, try again")
                    continue
                break
            except ValueError:
                print("That's not an int!")
# else all is good, val is >=  0 and an integer
        
#Printing the filled pyramid
print_pyramid(L)

#Solving the pyramid
while any("" in sub_list for sub_list in L):
    M = list(L)
    for i in range(4):
        for j in range(i+1):
            solve_pyramid(L,i,j)
    if M == L:
        break
        
if any("" in sub_list for sub_list in L):
    print("Not enough values to solve the pyramid!")
elif check_coherance(L) == False:
    print("The values are incoherants")
elif any((x < 0 for x in sub_list) for sub_list in L):
    print("This pyramid doesn't have a solution with positive numbers")
else:
    print("Solution:")
    print_pyramid(L)

#Press enter to continue
input("Press enter to continue...")
