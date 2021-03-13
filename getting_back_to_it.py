import random


i = 1

while i < 101:
    count = str(i) + " Mississippi"
    i = i + 1
    print(count)
    
  
for i in range(1,101):
    count = str(i) + " Mississippi"
    i = i + 1
    print(count)


absoluteChange = lambda a,b: a - b
relativeChange = lambda a,b: (b - a)/a
average = lambda a,b: (a + b) / 2
percentage = lambda a,b: (a/b) * 100
percentDifference = lambda a,b: round(((a-b)/((a + b)/ 2)) * 100)

print("Percent Change: " + str(percentDifference(100, 20))+ "%") 
print("Relative Change: " + str(relativeChange(100, 20))) 

x = 10
y = x * 2.3

while x < 250:
    change = "Percent Change: " + str(percentDifference(x, y))+ "%" + "\n" + "Relative Change: " + str(relativeChange(x, y))
    x = x + 1
    print(change)
    

arrayOne = []
arrayTwo = []
growth = 1
days = 7
for i in range(0, 52):
    if i == 0:
        minimalGrowth = random.randrange(1, 101)
        eachWeek = 7
    else:
        minimalGrowth = random.randrange(1, 101)
        eachWeek = (days * i) + 7
    arrayOne.append(minimalGrowth)
    arrayTwo.append(eachWeek)
 
for i in range(0, 52):
    x = arrayOne[i]
    y = arrayTwo[i]
    values = "For the values " + str(x) + " and " + str(y) + "\n"
    absChange = "Absolute Change: " + str(absoluteChange(arrayOne[i] , arrayTwo[i])) + "\n" 
    relChange = "Relative Change: " + str(relativeChange(arrayOne[i] , arrayTwo[i])) + "\n"  
    avg = "Average: " + str(average(arrayOne[i] , arrayTwo[i])) + "\n" 
    perc = "Percent: " + str(percentage(arrayOne[i] , arrayTwo[i]))+ "%" + "\n" 
    percDifference = "Percent Difference: " + str(percentDifference(arrayOne[i] , arrayTwo[i]))+ "%" + "\n" 
    print(values + absChange + relChange + avg + perc + percDifference)

 
x = 1
while x != 0: 
    x = int(input("Pick a starting value or type 0 to end: ")) 
    if x == 0:
        break
    else:
        y = int(input("Pick an ending value or type 0 to end: ")) 
        if y != 0:
            spaces = "\n----------------------------------------------------\n"
            values = "For the values " + str(x) + " and " + str(y) + "\n"
            absChange = "--Absolute Change: " + str(absoluteChange(x,y)) + "\n" 
            relChange = "--Relative Change: " + str(relativeChange(x,y)) + "\n"  
            avg = "--Average: " + str(average(x,y)) + "\n" 
            perc = "--Percent: " + str(percentage(x,y))+ "%" + "\n" 
            percDifference = "--Percent Difference: " + str(percentDifference(x,y))+ "%" 
            print(spaces + values + absChange + relChange + avg + perc + percDifference + spaces)
        else:
            break