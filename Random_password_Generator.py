import random
import string

password_len = int(input("Enter password Length : "))
if password_len <4:
   print("Password length must ne 4!")
   quit()

password =[
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]
charvalues = string.ascii_letters + string.digits + string.punctuation


for i in range(password_len - 4):
   password.append(random.choice(charvalues))

random.shuffle(password)
print("Your random Password is : ","".join(password))
