n, B = list(map(int, input().strip().split()))
T = 0

# your code here

lower = 0
upper = 10000
k = 0

while k < 100:
    sum = 0
    T = (lower + upper) // 2

    for i in range(n):

        if (i + 1) % 2 == 0:
            ps = 2 ** (i + 1) + 1

        else:
            ps = 3 ** (i + 1) + 1

        sum += (ps ** (n - (i + 1))) * T

    if sum > B:
        upper = T
    elif sum < B:
        lower = T
    else:
        break
    k += 1

T += 1
if T == 10000:
  T = -1


# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)