n, B = list(map(int, input().strip().split()))
T = 0

# your code here

sum = 0

while sum < B:
  sum = 0
  T += 1
  for i in range(1,n+1):
    
      if (i)%2 == 0:
        pi = 2**(i) + 1
        
      else:
        pi = 3**(i) + 1
        
      sum += (pi**(n-(i)))*T
  if T > 10000:
    T = -1
    break
  
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)