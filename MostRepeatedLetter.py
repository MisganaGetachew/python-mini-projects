# find the most repeated letter in the sentence
sentence = "rrighrre adldmkkkkkkk"


def counter(sentence):
    temp = 1
    for letter in sentence:
        counted = sentence.count(letter)
        if counted > temp:
            temp = counted
            theLetter = letter

    return theLetter, temp


print(counter(sentence))
