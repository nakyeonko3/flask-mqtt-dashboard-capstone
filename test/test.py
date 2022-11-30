import re

str = "2022-11-30 16:25:19,762"
p = re.compile("/,^[0-9]*$/")
result = p.search(str).group()
print(result)