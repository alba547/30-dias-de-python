empty_list = list() #1

more_than_5_items = ['a', 'b', 'c', 'd', 'e', 'f'] #2

print(len(more_than_5_items)) #3

print(more_than_5_items[0], more_than_5_items[len(more_than_5_items) // 2], more_than_5_items[-1]) #4

mixed_data_types = ['Alba', 16, 158, 'single', 'Jerez'] #5

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] #6

print(it_companies) #7

print(len(it_companies)) #8

print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1]) #9

it_companies[0] = 'YouTube'
print(it_companies) #10

it_companies.append('Facebook') #11

it_companies = it_companies[0:len(it_companies) // 2] + ['TCS'] + it_companies[len(it_companies) // 2:] #12

it_companies[1] = it_companies[1].upper #13

it_companies_hash = '#'.join(it_companies) #14

print('Amazon' in it_companies) #15

it_companies.sort() #16

it_companies.reverse() #17

it_companies = it_companies[2:] #18

it_companies = it_companies[:len(it_companies) -3] #19

it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:] #20

it_companies.pop(0) #21

it_companies.pop([len(it_companies) // 2]) #22

it_companies.pop(len(it_companies) -1) #23

it_companies.clear() #24

del it_companies #25

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.append(front_end) #26

full_stack = front_end
indx = full_stack.index('Redux')
full_stack.append('Python', 'SQL') #27