import pickle
course_map = {}
user_map = {}
obj_map = {}


def retrive(key, dic):
	if key in dic:
		res = dic[key]
	else:
		res = len(dic)
		dic[key] = res
	return res

def clean_enroll(fn):
	print fn
	fin = open("raw/"+fn,'r')
	fout = open("clean/"+fn,'w')

	fin.readline()
	for row in fin:
		arg = row.strip().split(',')
		fout.write("%s,%d,%d\n" % (arg[0], retrive(arg[1], user_map), retrive(arg[2], course_map)))
	fin.close()
	fout.close()

def clean_log(fn):
	print fn
	fin = open("raw/"+fn,'r')
	fout = open("clean/"+fn,'w')

	fin.readline()
	for row in fin:
		arg = row.strip().split(',')
		#enrollment_id,username,course_id,time,source,event,object
		fout.write("%s,%d,%d,%s,%s,%s,%d\n" % (arg[0], retrive(arg[1], user_map),
			retrive(arg[2], course_map), arg[3], arg[4], arg[5], retrive(arg[6], obj_map)))
	fin.close()
	fout.close()

if __name__=="__main__":
	clean_enroll("enrollment_train.csv")
	clean_log("log_train.csv")
	clean_enroll("enrollment_test.csv")
	clean_log("log_test.csv")
	with open("umap",'w') as f:
		pickle.dump(user_map, f)
	with open("cmap", 'w') as f:
		pickle.dump(course_map, f)
	with open("omap", 'w') as f:
		pickle.dump(obj_map, f)
