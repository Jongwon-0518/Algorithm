import re

s = input()
s = re.sub(r'\b0+(?!\b)', '', s)
s = s.replace("-", ")-(")
s = "(" + s + ")"
print(eval(s))