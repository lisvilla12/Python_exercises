wordlist = ['hello','world','my','name','is','Anna']
char = 'o'

def character(mylist, subStr):
    newlist= []
    for element in mylist:
        if subStr in element:
            newlist.append(element)
    print newlist

character(wordlist, char)

