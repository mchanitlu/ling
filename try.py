import sys
import itertools
text = sys.stdin.read()	
z = text.splitlines()  
for i in range(len(z)):
	print("%d\t%s"%(i+1,z[i]))
def newlist(z):
	res = []
	for el in z:
		sub = el.split(',')
		res.append(sub)
		res = [ele for ele in res if ele != [' ']] 
		res = [ele for ele in res if ele != ['']]  
	return(res) 
w = newlist(z)
print("w")
print(w)
for i in range(len(w)):
	print("%d\t%s"%(i+1,w[i]))
a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
flat_list = []
for sublist in w:
	for item in sublist:
		ok = item.split(' ')
		flat_list.append(ok)
flatten = lambda w: [item for sublist in w for item in sublist]
a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
print(a)

for i in range(len(flat_list)):
	print('# sent_id = %s' % (i))
	nano = ' '.join(flat_list[i])
	print("# text = " + str(nano))
	flat_list[i] = list(filter(lambda item: item.strip(), flat_list[i]))
	for c in range(len(flat_list[i])):
		u = flat_list[i]
		print("%d\t%s\t_\t_\t_\t_\t_\t_\t_"%(c+1,u[c]))

#addresses = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
#print([el[:].split()[:] for el in w])		
#q = '\t'.join(z)
#print(q)
#k = q.split()
#for h in k:
	#if h == '\t':
		#print("ID")
#for o in q:
	#if o == '()",.':
		#'\n'.join(q)
#return 
#a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
#print(a) 
#for i in range(len(new)):
	# print("%d\t%s\t-\t-\t-\t-\t-\t-\t-"%(i+1,new[i]))

#import sys
#text = sys.stdin.read()
#z = text.split()
#print(z)
#a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
#print(a)
#for i in range(len(z)):
       # print("%d\t%s\t-\t-\t-\t-\t-\t-\t-"%(i+1,z[i]))







