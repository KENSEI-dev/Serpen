def compression(string):
  freq={}

  for char in string:
    if char in freq:
      freq[char]+=1
    else:
      freq[char]=1
  formatted=""
  for char in freq:
    count=freq[char]
    formatted+=char+str(count)

  if len(string)<len(formatted):
    print(formatted)
  else:
    print(string)

if __name__=="__main__":
  s=input()
  compression(s)