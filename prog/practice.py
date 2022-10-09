# a=1253
# print("iam %s love you" %a )

import re

a=re.match(r'(\d+)','12345454h55')

print(a.span())

# data = ("John", "Doe", 53.44,[12,1253])
# format_string = "Hello %s %s. Your current balance is $%s,==%s."

# print(format_string % data)