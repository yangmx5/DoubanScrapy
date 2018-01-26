def testyield():
    if 1 == 1:
        print(1)
        yield 5
        print(2)
    if 2 == 2:
        print(3)
        yield  6
        print(4)


def testyield2():
    for i in range(2):
        print i
        yield "first",i
        print "=="
        yield  "sec",i


for i  in testyield2():
    print i,"+"