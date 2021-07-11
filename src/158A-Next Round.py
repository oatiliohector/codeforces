a, b = [int(y) for y in input().split()]

numbers_scores= [int(x) for x in input().split()]
 
temp = numbers_scores[b-1]

count = 0

for i in range(0,len(numbers_scores)):
    if numbers_scores[i] >= temp and numbers_scores[i]>0:
        count += 1

print(count)    