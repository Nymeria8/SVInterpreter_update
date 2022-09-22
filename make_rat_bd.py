from sys import argv


def read_file(infile):
	f=open(infile)
	dic={}
	for i in f:
		if i.startswith("#")==False:
			line=i.split("\t")
			gg=line[3].split("; ")
			not_in=True
			dic[line[0]]=[]
			for el in gg:
				#print(el)
				nn=el.split(" ")[0]
				#print(nn)
				#print(nn.upper())
				if nn.isupper()==True and nn=="ASSOCIATED":
					#print("aa")
					not_in=False
					dic[line[0]].append(el.replace("ASSOCIATED WITH ",""))
				elif nn.isupper()==True:
					#print("bb")
					not_in=True
				elif not_in==Falqse:
					#print("CC")
					dic[line[0]].append(el)
	f.close()
	return dic
	
def wrtite_dic(dic):
	for key, value in dic.items():
		if len(value)>0:
			print(key+"\t"+"; ".join(value))


wrtite_dic(read_file(argv[1]))
				
