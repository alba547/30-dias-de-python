space = ""
print(space)
print(len(space))
word1 = 'thirty'
print(word1)
print(len(word1))
word2='days'
print(word2)
print(len(word2))
word3='of'
print(word3)
print(len(word3))
word4='python'
print(word4)
print(len(word4))
string= space + word1 + word2 + word3 + word4
print(string)
print(len(string))

space=""
word5 = 'coding'
print(word5)
print(len(word5))
word6 = 'for'
print(word6)
print(len(word6))
word7 = 'all'
print(word7)
print(len(word7))
string2 = space + word5 + word6 + word7
print(string2)
print(len(string2))

company = string2

print(company)
print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

string3 = string2 - word5

print(string2.count('coding'))

print(string2.replace('coding', 'python'))

print(string2.replace('all' , 'everyone'))

print(string2.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

print(string2.index)
print(string2.rindex)
print(string2.index(10))

language = 'Python For Everyone'.split()
print(f"{language[0][0] + language[1][0] + language[2][0]}")


language2 = 'Coding For All'
print(f"{language2[0][0] + language2[1][0] + language2[2][0]}")

print("Coding For All".index('C'))

print("Coding For All".index('F'))

print("Coding For All People".rfind('l'))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ' '))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ' '))

