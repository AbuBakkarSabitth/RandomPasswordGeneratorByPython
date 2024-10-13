import random
import string
# print(string.ascii_letters) #American standard code for information interchange
# print(string.digits)
# print(string.punctuation)
# print(random.choice("hello"))
# # val= random.choice(['a','b','c','d'])
# # print(val)
#We have to ascii_letters,digits,punctuation in a single format for password
charValues=string.ascii_letters+ string.digits+string.punctuation
# print(charValues)
pass_len=12
# print(random.choice(charValues))
#list comprehension[function]
# password =""
# for i in range(pass_len):
#     password+=(random.choice(charValues))





password ="".join([random.choice(charValues) for i in range(pass_len)])

print("your random password is:",password)