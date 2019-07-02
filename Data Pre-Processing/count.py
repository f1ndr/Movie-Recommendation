r = open("xxx-dictionary.txt", "r")
sentence_depart = r.read()
r.close()
count=0
for word in sentence_depart.split(" "):
    count=count+1
print("the number of words：%d"%(count))