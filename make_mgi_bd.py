from sys import argv


def read_MP(infile):
	f=open(infile)
	dic={}
	term=""
	desc=""
	for i in f:
		if "oboInOwl:id" in i and "MP:" in i:
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

def read_oth(infile, mp):
	f=open(infile)
	dic={}
	for i in f:
		line=i.split("\t")
		if "|" not in line[-1] and line[3] in mp:
			if line[-1].strip() not in dic:
				dic[line[-1].strip()]=[mp[line[3]]]
			else:
				dic[line[-1].strip()].append(mp[line[3]])
	f.close()
	return dic
	
def write(dic):
	for key, value in dic.items():
		print(key+"\t"+";".join(value))

write(read_oth(argv[1], read_MP(argv[2])))
