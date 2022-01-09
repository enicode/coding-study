def frepIndex(string_):
    if len(string_) == 1:
        return 1000
    for i in range(len(string_)-1):
        if string_[i] == string_[i+1]:
            return i
    return 1000
#반복되는 문자!이 있다면 그 처음의 index를 반환 없다면 1000을 반환(문자열 길이가 1000까지 이므로 index는 999까지)
def n_string(string_, i_index):  
    return string_[0:i_index]+string_[i_index+2:]
#문자열과, index가 주어지면 index, index+1 문자를 삭제하고 난 뒤 새로운 문자열 반환// 만약 4연속이어도 2개씩만 지움
t=int(input())
for _ in range(t):
    chr_list=input()   
    while True:
        i_index=frepIndex(chr_list)
        if i_index == 1000:
            break   
        chr_list = n_string(chr_list, i_index)
#더 이상 연속되는 문자열이 없을 때까지 반복
    print(f'#{_+1} {len(chr_list)}')