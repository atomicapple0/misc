word = "ninja"
sentence = "ni *jaasdasd ninjaasdas **nja n** j*"

kk = len(word)
best = 0
for i in range(len(sentence)):
    print("start: ", end="")
    j = i
    k = 0
    n_stars = 0
    n_spaces = 0
    while k < kk and i < len(sentence):
        print(sentence[i], end = "")
        if k > 0 and sentence[i] == " ":
            n_spaces += 1
            i += 1
        elif sentence[i] == "*":
            k += 1
            n_stars += 1
            i += 1
        elif sentence[i] == word[k]:
            k += 1
            i += 1
        else:
            break
    score = 0
    if k == kk and n_spaces > 0:
        score = 1 + n_stars
        best = max(best, score)
    print(f" (score: {score})")

print(best)