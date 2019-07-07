q = str(input())
print(''.join([q[x:x+2][::-1] for x in range(0, len(q), 2)]))
