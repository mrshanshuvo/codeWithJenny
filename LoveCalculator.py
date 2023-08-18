name1 = input("Enter your name: ")
name2 = input("Enter your GirlFriend's name: ")

combineName = name1 + name2
lowerCase = combineName.lower()

t = lowerCase.count('t')
r = lowerCase.count('r')
u = lowerCase.count('u')
e = lowerCase.count('e')

true = t + r + u + e

l = lowerCase.count('l')
o = lowerCase.count('e')
v = lowerCase.count('e')
e = lowerCase.count('e')

love = l + o + v + e

total = str(true) + str(love)
loveScore = int(total)
if loveScore < 30:
    print(f"Your Love Score is {loveScore}% and You guys are like Coke and Mentos")
elif loveScore >= 30 and loveScore < 60:
    print(f"Your Love Score is {loveScore}% and You guys are Alright, Can be Together for Short time")
else:
    print(f"Your Love Score is {loveScore}% and You guys are Soulmate made in Heaven")