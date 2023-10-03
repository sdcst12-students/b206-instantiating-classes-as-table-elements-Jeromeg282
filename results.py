import random

teams = ['A','B','C','D','E','F','G']
results = []
for i in reversed(teams):
    for j in reversed(teams):
        if i == j:
            continue
        s1 = random.randint(0,4)
        s2 = random.randint(0,4)

        results.append( {
            't1' : i,
            's1' : s1,
            't2' : j,
            's2' : s2
        })

print(results)
