def solution(S):
    listS = list(S)
    start = 0

    for i in range(len(listS)):
        number = listS.pop()
        if number == '1':
            start = start + pow(2, i)
    print(start)




solution("1"*400000)
