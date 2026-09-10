# input id of voter (str)
# input vote selection -- 'A', 'B', 'C', 'D', if Something else was chosen  Input again until A,B,C,D
# if same user votes more than 1 time, change the vote to 'F'
# input until voter id is -999
# after the loop:
#   sum all of the votes,
#      print how many votes for each party
#      print the parties from highest to lowest
from itertools import count

# 1
# T
# party does nto exist
# D

# 2
# C

# 1
# disqualified -- 'F'

# {'1': 'D', '23978462' : 'B', '1234': 'D', '123': 'F', '22': 'B', '5': 'A'}
# {'D': 2, 'B': 2, 'A': 1}
# {'D' : 2, 'B': 2, 'A': 1}
# 'D', 'B', 'A'


votes = {}

while True:
    voter = input('enter id: ')
    if voter == '-999':
        break
    vote = input('enter vote: ')
    if vote in ['a','b','c','d']:
        votes[vote] = votes.get(vote,0)+1
    else:
        print('invalid input')
        continue
    if voter not in votes:
        votes[voter] = vote
    else:
        votes[voter] = 'f'
print(votes)
count = {}
for v in votes.values():
    if v == 'f':
        continue
    count[v]= count.get(v,0)+1
print(sorted(count, key=count.get, reverse=True))

