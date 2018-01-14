def odd_even():
    for x in range(1, 2001):
        if x % 2 == 0:
            print "number is " + str(x) + ". This is an even number."
        else:
            print "number is " + str(x) + ". This is an odd number."   
print odd_even()


a = [2,4,10,16]
def multiply(list, num):
    newlist = []
    for x in list:
        newlist.append(x*num)
    return newlist
print multiply(a,5)


def layered_multiples(arr):
    newarr =[]
    for x in arr:
        newarr2 =[]
        count=0
        while count < x:
            newarr2.append(1)
            count +=1
        newarr.append(newarr2)
    return newarr

test = layered_multiples(multiply([3,5,6],8))
print test





