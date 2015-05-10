import itertools
pred = open("pred", 'r')
enroll = open("clean/enrollment_test.csv",'r')

sub = open("sub.csv",'w')
for el,p in itertools.izip(enroll, pred):
	eid = el.split(",",1)[0]
	prob = float(p)
	sub.write("%s,%.10f\n" % (eid, prob))
pred.close()
enroll.close()
sub.close()
