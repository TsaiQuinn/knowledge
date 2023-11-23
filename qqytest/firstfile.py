def BubblingSorting(x):
    len_x = len(x)
    for i in range(len_x):
        for j in range(len_x-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    print(x)


if __name__=="__main__":
    a = [2,9,4,8,1,9,3,4,7]
    BubblingSorting(a)
