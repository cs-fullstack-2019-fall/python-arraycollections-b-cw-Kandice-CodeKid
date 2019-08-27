# python-arrayCollections_b-cw

### Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# ``` arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"] ```
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.

def prob1():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2])
    print(len(arrayForProblem2))
    arrayForProblem2.pop(1)
    print(arrayForProblem2[2])

# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.

def prob2():
    userInput =''
    while userInput != 'q':
        userInput = input('Enter some data, press "q" to quit: ')

### Problem 3:
# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
# ```
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# ```
# a) Print the collection
# b) Print William's nickname

### Problem 4:
# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function


# numberArray = [10,20,30,40,50]
# for a in reversed(numberArray):
#     print(a)


### Problem 5:
# Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def prob5(givenArray):
   for x in givenArray:
       while userInput != givenArray:
           if userArray > givenArray:
               print(len(givenArray))
       else:
        print("something")




userArray = [12,27,-2,59]
userInput =userArray.append(int(input('Enter a number')))
prob5(userArray)

# prob1()
# prob2()
# prob3()
# prob4()

