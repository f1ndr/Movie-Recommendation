import pkuseg

seg = pkuseg.pkuseg()           # 以默认配置加载模型
r = open("comments.txt", "r")
content = r.read()
r.close()
text = seg.cut(content)  # 进行分词

w = open("commentsseg.txt", "w")
w.write(" ".join(text))
w.close()
print("successful!")