def find_most_word(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    max = 0
    mfw = ""

    for word, frequency in word_count.items():
        if frequency > max or (frequency == max and word > mfw):
            max = frequency
            mfw = word

    return mfw, max

n = int(input())
words = [input().strip() for _ in range(n)]
re = find_most_word(words)
print(*re)
