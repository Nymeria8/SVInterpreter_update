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


def read_zfin(infile, DOID):
	f=open(infile)
	dic={}
	for i in f:
		line=i.split("\t")
		if line[0] not in dic:
			if line[4]!="":
				dic[line[0]]=[line[4]]
			elif line[6]!="":
				dic[line[0]]=[line[6]]
			else:
				dic[line[0]]=[DOID[line[5]]]			
		else:
			if line[4]!="":
				dic[line[0]].append(line[4])
			elif line[6]!="":
				dic[line[0]].append(line[6])
			else:
				dic[line[0]].append(DOID[line[5]])
	f.close()
	return dic

def wrr(dic):
	for key,value in dic.items():
		print(key+"\t"+"; ".join(value))
		
wrr(read_zfin(argv[1], read_DOID(argv[2])))
