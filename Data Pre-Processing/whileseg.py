import pkuseg

seg = pkuseg.pkuseg()           # 以默认配置加载模型
i=n
all=[]
while i<n:
    filename=str(i)+".txt"
    r = open(filename, "r")
    content = r.read()
    r.close()
    text = seg.cut(content)  # 进行分词
    all.extend(text)
    i=i+1

w = open("result.txt", "w")
w.write(" ".join(all))
w.close()

print("successful!")
