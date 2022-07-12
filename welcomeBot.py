
print("Welcome to Collins Academy")

name = input('What is Your name: ')
print(f"welcome {name} to Collin's Academy")
age = int(input("How are old are you: "))

'''
if visitor is not up to 18 years, we will not accept the visitor,
otherwise we will accept the visitor
'''
if age < 18:
    print(f"Sorry {name} you must be up to 18 years")
else:
    print(f'Thank you {name} your age which is {age} is eligible to use our academy')



