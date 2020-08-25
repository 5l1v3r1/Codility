A = [3, 5, 6, 3, 3, 5]

    kvDict = {}

    for i in range(len(A)):
        kvDict[i] = A[i]



    count = 0
    for i in range(len(kvDict)):
        for j in range(i+1, len(kvDict)):
            if kvDict[i] == kvDict[j]:
                count += 1

        if count >= 1000000000:
            return 1000000000

    return count