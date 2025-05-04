import string
import random

init = string.ascii_lowercase
final = ""
for i in range(0,12):
    rand = random.randint(0,23)
    final += init[rand]
print(final)
