coord = (3, 5)
print('X: {0[0]} ; Y: {0[1]} '.format(coord))
print("repr() shows quotes: {!r} ; str() doesn't: {!s} ".format('test1', 'test2')+'\n')
print('{:<30} '.format('left aligned')+'\n')
print('{:>30} '.format('right aligned')+'\n')
print('{:^30} '.format('centered')+'\n')
print('{:*^30} '.format('centered')+'\n')
print("int: {0:d} ; hex: {0:#x} ; oct: {0:#o} ; bin: {0:#b} ".format(42)+'\n')
points = 19.5
total = 22
print('Correct answers: {:.2%} '.format(points/total))

print("Units destroyed: {players[0]!r:*<20s} ".format(players=['1', '2', '3']))
