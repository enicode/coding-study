def Delete(numbers, pos):
    while numbers[pos] == numbers[pos+1]:
        former=numbers[:pos]
        latter=numbers[pos+2:]
        numbers=''.join([former,latter])
        if not latter:
            return numbers
        else:
            pos -= 1
    return numbers

def FindPos(numbers):
    prev_num=-1
    for pos, number in enumerate(numbers):
        if number == prev_num:
            return pos-1
        prev_num=number   
    else:
        return False
for test_case in range(10):
    length,nums=input().split()

    while FindPos(nums):
        nums = Delete(nums,FindPos(nums))

    print(f'#{test_case+1} {nums}')
