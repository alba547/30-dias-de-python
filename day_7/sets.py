# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies)) #1
it_companies.add('Twitter') #2
it_companies.update(['TCS', 'Dell']) #3
it_companies.remove('Facebook') #4
print(f"La diferencia es que el método remove puede dar error si no encuentra item en el set dado, sin embargo el método discard no da ningún tipo de error")

print(A.union(B)) #1
print(A.intersection(B)) #2
print(A.issubset(B)) #3
print(A.isdisjoint(B))
print(A.union(B)) #4
print(B.union(A))
print(A.symmetric_difference(B)) #5
del A #6
del B
del it_companies