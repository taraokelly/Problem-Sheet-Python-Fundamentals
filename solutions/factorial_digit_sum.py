n = 100;
sum = 0;

for x in range(n,0,-1):
    if x == n:
        sum = n;
    else:
        sum = sum * x;

print(sum)