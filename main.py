from jieba.analyse import extract_tags
f = open("a.txt", encoding="utf-8")
news = f.read()
f.close()

print(extract_tags(news, 10))