times=int(input())
first=[]
second=[]
for i in range(times):
    coords=input()
    coords = [int(i) for i in coords.split()]
    first.append(int(coords[0]))
    second.append(int(coords[1]))

firstmax=max(first)
#print(firstmax)
secondmax=max(second)
#print(secondmax)
firstmin=min(first)
#print(firstmin)
secondmin=min(second)
#print(secondmin)
print(abs(firstmax-firstmin)*abs(secondmax-secondmin))
    
