def vowels(s):
    count = 0
    vow=("aeiouAEIOU")
    for char in s:
      if char in vow:
        count += 1
    return count
s=input("enter a string: ")
res=vowels(s)
print(res)
