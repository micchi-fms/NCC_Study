# d="paraparaparadise"
# res=[]
# for i in range(0,len(d)):
# 	res.append(d[i])
# print(res);
def ngram(l,n):
	res=[]
	for i in range(0,len(l)-n+1):
		res.append("".join(l[i:i+n]))
	return res
x="paraparaparadise"
y="paragraph"
print(ngram(x,2))
print(ngram(y,2))
x=ngram(x,2);
y=ngram(y,2);

x=set(x)#集合が扱える
y=set(y)
print(x)
print(y)
print(x | y)
print(x & y)
print(x-y)
print("se"in(x&y))