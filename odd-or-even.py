def func(num):
    if (int (num) % 2)== 0:
        res = (str(num))+" is EVEN"
    else:
        res = (str(num))+" is ODD"
    return res


num = input("Enter a number between 1 and 1000")
if int(num) <1:
    print ("Invalid Entry...Try  Again")
else:
    print (func(num))
