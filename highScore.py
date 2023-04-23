# python highest value finder

score = [99, 45, 56, 67, 178, 0]
length = len(score)


def highScore(score):
    scoreHigh = 0
    for x in score:
        if x > scoreHigh:
            scoreHigh = x

    return scoreHigh


print(highScore(score))
print(range(length))
