def LCM(x,y):
    # choose the greater number
    if x > y:
        maxNum = x
    else:
        maxNum = y
    while (True):
        if ((maxNum % x == 0) and (maxNum % y == 0)):
            lcm = maxNum
            break
        maxNum += 1

    return lcm
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
print("The L.C.M. of the given numbers is: ", LCM(num1, num2))
