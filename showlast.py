fin = open('clean/log_train.csv') 
fout = open('headtail.csv','w')
tf = open("clean/truth_train.csv")

truth = {}
for line in tf:
	enr, pos = line.strip().split(',')
	truth[enr] = pos

prevenr = 0
prevlin = "\n"
for line in fin:
	enr = line.split(',',1)[0]
	if enr != prevenr:
		if prevenr in truth:
			fout.write(truth[prevenr]+'\t'+prevlin+"\n")
		if enr in truth:
			fout.write(truth[enr]+'\t'+line)
	prevenr = enr
	prevlin = line
fin.close()
fout.close()