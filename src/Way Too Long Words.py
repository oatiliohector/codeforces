times = int(input())

for i in range(times):
    word = str(input())

    if len(word) < 10:
        print(word)
    else:
        for k in range(times):
            first_letter = word[0]
            last_letter = word[-1]

            new_len = len(word)

            print('{}{}{}'.format(first_letter,new_len-2,last_letter))