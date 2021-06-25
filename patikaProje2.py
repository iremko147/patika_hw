def toReverse(x):
    x.reverse()
    for i in x:
        if type(i)==list:
            toReverse(i)
    return x
a=toReverse([[1,2],[3,[],4,[5,6,[7,8,[9,[10,11,12]],13],14]],[15,16,17]])
print(a)

"""def toReverse(x):
    x.reverse()
    for i in x:
        if type(i)==list:
            i.reverse()
            for c in i:
                if type(c)==list:
                    toReverse(c)"""