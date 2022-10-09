str="aaacodebbb"
def count_code(str):
  x=["co"+i+"e" for i in str.lower()]
  count = 0
  index = 0
  for i in x:
      if i in str[index:]:
          index = str.find(i)+1
          count+=1
  return count
