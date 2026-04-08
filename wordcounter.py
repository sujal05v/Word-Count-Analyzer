
filename = input("Enter file name: ")
"""READ MODE"""
try:
 file = open(filename,"r")       #Here r = readmode file ko sirf read ke leye open kr rhe hai
except:
 print("File not Found")

lines = file.readlines()          #readlines() -> saari lines list me aa gye hai
file.close()


word_count = {}

for line in lines:
  words = line.split()    # It is used to split the line's eg: "hello world" -> ["hello","world"]

  for word in words:
    if word in word_count:
       word_count[word] += 1
    else:
     word_count[word] = 1

for word in word_count:
  print(word,":",word_count[word])