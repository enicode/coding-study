n=int(input())

fNums=[0,1]
for i in range(0, 46):
    fNums += [fNums[i]+fNums[i+1]]

print(fNums[n])