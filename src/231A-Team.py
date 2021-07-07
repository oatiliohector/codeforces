x = int(input())

sum_baby = 0

for i in range(x):

    a,b,c = [int(f) for f in input().split()]

    if a==1 and b == 1 and c == 0:
        sum_baby+=1
    elif a == 1 and b == 0 and c == 1:
        sum_baby+=1
    elif a == 0 and b == 1 and c == 1:
        sum_baby +=1
    elif a == 1 and b == 1 and c == 1 :
        sum_baby +=1

print(sum_baby)