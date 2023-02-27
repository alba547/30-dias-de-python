empty_tuple = tuple() #1

sisters = ('María', 'Ana') #2
brothers = ('Carlos')

siblings = sisters + brothers #3

print(f"I have {len(siblings)} siblings") #4

family_members = siblings + ('Carmen', 'Alberto') #5


siblings, father, mother = family_members #1

fruits = ('apple', 'watermelon', 'lemon') #2
vegetables = ('lettuce', 'tomato')
animals_products = ('milk', 'leather')
food_stuff_tp = fruits + vegetables + animals_products

food_stuff_lt = list(food_stuff_tp) #3

food_stuff_lt = food_stuff_lt[:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:] #4

first_three = food_stuff_lt[:3] #5
last_three = food_stuff_lt[len(food_stuff_lt) -3: ]
print(food_stuff_lt)

del food_stuff_lt #6

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') #7
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
