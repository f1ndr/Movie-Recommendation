import pkuseg
stopwords = [line.strip() for line in open('filmsw.txt', encoding='UTF-8').readlines()]
clean=''
seg = pkuseg.pkuseg()           # 以默认配置加载模型
r = open("oridictionary.txt", "r")
content = r.read()
r.close()
text = seg.cut(content)  # 进行分词
w = open("dictionaryseg.txt", "w")
w.write(" ".join(text))
w.close()

r1 = open("dictionaryseg.txt", "r")
sentence_depart = r1.read()
r1.close()

for word in sentence_depart.split(" "):
    if word not in stopwords:
        clean=clean+word+" "
    clean=clean+""

w1 = open("xxxx-dictionary.txt", "w")
w1.write(clean)
w1.close()

print("successful!")