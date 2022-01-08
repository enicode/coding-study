def frepIndex(string_):
    if len(string_) == 1:
        return 1000
    for i in range(len(string_)-1):
        if string_[i] == string_[i+1]:
            return i
    return 1000

def n_string(string_, i_index):  
    return string_[0:i_index]+string_[i_index+2:]

t=int(input())
for _ in range(t):
    chr_list=input()   
    while True:
        i_index=frepIndex(chr_list)
        if i_index == 1000:
            break   
        chr_list = n_string(chr_list, i_index)
    print(f'#{_+1} {len(chr_list)}')