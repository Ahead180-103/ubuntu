
while True:
    data = input('enter binary number:')
    #if data == '0':
    #   print(0)
    n = len(data)
    print('length:',n)
    l = []
    ss = 1
    sum = 0
    for i in data:
        l.append(i)
        #print(l)
    while ss <= n:
        aa = l[ss-1]
        #print(aa)
        if aa == '0':
            ss += 1
            pass
        elif aa == '1':
            b = 2**(n-ss)
            ss += 1
            sum += b
        else:
            print('please enter banary number')
            exit()
    print(sum)
