def encode(strs):
  res=""
  for s in strs:
    res+=str(len(s)) + "#" + s
  return res

def decode(str):
  res, i = [], 0
  while i<len(str):
    j=i
    while s[j] != "#":
      j+=1
    l = int(str[i:j])
    res.append(s[j+1:j+1+l])
    i=j+1+l
  return res
  
  
