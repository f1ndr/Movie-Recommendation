r = open("commentsseg.txt", "r")
sentence_depart = r.read()
r.close()
stopwords = [line.strip() for line in open('filmsw.txt', encoding='UTF-8').readlines()]
clean=""
count1=0
count2=0
for word in sentence_depart.split(" "):
    if word not in stopwords:
        clean=clean+word+" "
    clean=clean+""
    count1=count1+1

for word in clean.split(" "):
    count2=count2+1

w = open("commentsclean.txt", "w")
w.write(clean)
w.close()

print("共有词数：%d"%(count1))
print("清洗后词数：%d"%(count2))