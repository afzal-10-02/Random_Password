# Random-Password-Generator
# import important module
import random
import string

# Taking all the uppercase letters (A to Z)
upper = string.ascii_uppercase

# Taking all the lowercase letters (a to z)
lower = string.ascii_lowercase

# Taking all the digits (0 to 9)
digits = string.digits

# Taking all the punctuation
punc = string.punctuation

# Creating random password 
password = (random.choices(upper , k=random.rand(2,5))+
            random.choices(lower , k=random.rand(2,5))+
            random.choices(digits , k=random.rand(2,5))+
            random.choices(punc , k=random.rand(2,5)))
random.shuffle(password)

# Print the Password
print("".join(password))