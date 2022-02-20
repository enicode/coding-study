n, m, k = map(int, input().split())

n_numbers = list(map(int, input().split()))

n_numbers.sort(reverse=True)

first = n_numbers[0]
second = n_numbers[1]

times=m//(k+1)
reminder=m%(k+1)

print((first*k)*(times+reminder)+second*times)
