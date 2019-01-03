



def chu2(numbers):
    global n
    n = int(numbers / 2)
    return n

while True:
    data = float(input('enter decimal int number:'))
    if data == 0:
        print(0)
        continue

    elif data == 1:
        print(1)
        continue

    dcm = []
    n = None

    if data%2 == 1:
        chu2(data)
        dcm.append('1')

    else:
        chu2(data)
        dcm.append('0')


    while n >= 2:
        if n%2 == 1:
            chu2(n)
            dcm.insert(0,'1')

#        elif n == 1:
#            break

        elif n%2 == 0:
            chu2(n)
            dcm.insert(0,'0')

#        else:
#           break

    dcm.insert(0,'1')
    b = ''.join(dcm[::])
    print(b)
    print('decimal over')
