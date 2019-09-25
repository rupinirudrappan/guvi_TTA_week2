def sentence_count(line):
    sentence=line.split('.')
    sentence=str(sentence)
    sentence=sentence.split('?')
    sentence=str(sentence)
    sentence=sentence.split('!')
    return len(sentence)
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = ['a','e','i','o','u','y']
    splchar=['.','!','?']
    for i in splchar:
        if i in word:
            word=word.replace(i,"")
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
        try:
            if word[index] in vowels and word[index+1] in vowels:
                count-=1
        except IndexError:
            pass
    if word.endswith("e"):
        count -= 1
    if ((word.endswith("le") and word[-3] not in vowels) or (word.endswith("les") and word[-4] not in vowels)):
        count+=1
    if count == 0:
        count += 1
    return count

num_lines=num_words=num_syllables=0
file="input.txt"
with open(file, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += sentence_count(line)
        num_words += len(words)
        for word in words:
            num_syllables += syllable_count(str(word))
print("Number of sentence : "+str(num_lines))
print("Number of words : "+str(num_words))
print("Number of syllables : "+str(num_syllables))
F = 206.835 - 1.015 *(num_words / num_lines) - 84.6 * (num_syllables / num_words)
G = 0.39 * (num_words / num_lines)+ 11.8 * (num_syllables / num_words) - 15.59
print("Flesch Index : "+str(F))
print("Flesch-Kincaid Grade Level Equivalent : "+str(G))