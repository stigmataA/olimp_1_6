from collections import Counter

n = int(input(f'Количество хозяйств: '))
ks = [int(input(f'Поголовье стада в хозяйстве {i+1}: ')) for i in range(n)]
kmax = max(ks)

big_farms = [ki for ki in ks if ki * 10 >= kmax]

if not big_farms:
    print(0)
else:
    freq = Counter(big_farms)
    max_freq = max(freq.values())
    modes = [ki for ki, count in freq.items() if count == max_freq]
    print(f'Наиболее часто встречающееся значение поголовья: {max(modes)}')