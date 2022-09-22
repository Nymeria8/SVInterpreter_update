from sys import argv


def read_DOID(infile):#igual a read_MP
	f=open(infile)
	dic={}
	term=""
	desc=""
	for i in f:
		if "oboInOwl:id" in i and "DOID:" in i:
			a=i.split(">")[1]
			term=a.split("<")[0]
		if "label" in i:
			a=i.split(">")[1]
			desc=a.split("<")[0]
		if term!="" and desc!="":
			dic[term]=desc
			term=""
			desc=""
	f.close()
	return dic


def read_worns(infile, DOID):
	f=open(infile)
	dic={}
	for i in f:
		if i.startswith("!")==False:
			line=i.split("\t")
			if line[1]=="gene":
				if line[3] not in dic:
					dic[line[3]]=[line[8].replace("_"," ")+" "+DOID[line[10]]]
				else:
					dic[line[3]].append(line[8].replace("_"," ")+" "+DOID[line[10]])
	f.close()
	return dic

def wrr(dic):
	for key,value in dic.items():
		print(key+"\t"+"; ".join(value))
		
wrr(read_worns(argv[1], read_DOID(argv[2])))
