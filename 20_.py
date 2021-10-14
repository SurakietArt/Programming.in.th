word_len = int(input())
word_round = int(input())
word_list = []

for i in range(word_round):
    word = input()
    word_list.append(word)

def collect_word(x,y):
    word_check = []
    for i in x:
        for j in i:
            if len(word_check) < word_len:
                word_check.append(j)
    return word_check[y]

while i < (word_round-1):
    score = 0
    j = 0
    while j < word_len:
        if collect_word(word_list[i],j) == collect_word(word_list[i+1],j):
            score += 1
            j+=1
        else:
            j+=1
    if score < 2:
        break
    i += 1
print(word_list[i])