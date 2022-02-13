t = int(input())

for test_case in range(1,t+1):
    n= int(input())
    math_score=list(map(int, input().split()))
    mfn_dict={}
    for i in range(1000):
        if math_score[i] in mfn_dict.keys():
            mfn_dict[math_score[i]] += 1
        else: 
            mfn_dict[math_score[i]] = 1

    sorted_mfn_dict=sorted(mfn_dict.items(), key=lambda x:(x[1],x[0]), reverse=True)

    print(f'#{n} {sorted_mfn_dict[0][0]}')