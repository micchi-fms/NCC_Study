def ngram(l,n):
	res=[]
	for i in range(0,len(l)-n+1):
		res.append(''.join(l[i:i+n]))
	return res
s="I am an NLper"
print(ngram(s.split(),2))