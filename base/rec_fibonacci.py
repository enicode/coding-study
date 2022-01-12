def fnumber(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fnumber(n-1)+fnumber(n-2)