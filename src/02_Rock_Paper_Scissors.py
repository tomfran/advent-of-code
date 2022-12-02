from utils.api import get_input

input_str = get_input(2)


win = {"A": "Y", "B": "Z", "C": "X"}
eq = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}
score = {"X": 1, "Y": 2, "Z": 3}

e = map(lambda x: x.strip().split(), input_str.splitlines())

ans1 = ans2 = 0

for other, me in e:

    ans1 += score[me]
    if me == win[other]:
        ans1 += 6
    elif me == eq[other]:
        ans1 += 3

    if me == "X":
        play = lose[other]
    elif me == "Y":
        play = eq[other]
        ans2 += 3
    else:
        play = win[other]
        ans2 += 6
    ans2 += score[play]

print(ans1, ans2)
