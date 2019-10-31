from operator import itemgetter
scores = [['Bruce',1000], ['Amber',12], ['Shane',-100],['Gayle',300]]
scores = sorted(scores, key=itemgetter(1))
print(list(reversed(scores)))
