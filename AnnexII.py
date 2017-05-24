####Part I: This part of script gives out the outcomes for a, b, d and e in question 7. The outcome of c (the average number of TM segments) will be given in the second part.
f=open ('18.prot.shortoutput.txt')
total_seq_num=0
num_no_TM=0
num_with_TM=0
num_with_signal=0
num_sig_with_TM=0
for line in f:
	if line[0]=='.':
		total_seq_num+=1
		if line[32]=='0' and line[31]==' ':
			num_no_TM+=1
		if line[32]!='0' or line[31]!=' ':
			num_with_TM+=1
		if line[35]=='Y':
			num_with_signal+=1
			if line[32]!='0' or line[31]!=' ':
				num_sig_with_TM+=1
print ('The fraction of proteins with 0 TM segments in species 18=', num_no_TM/total_seq_num)
print ('The fraction of proteins with > 0 TM segments in species 18=', num_with_TM/total_seq_num)
print ('The fraction of proteins with > 0 signal peptide=', num_with_signal/total_seq_num)
print ('The fraction of those (with > 0 signal peptide) with > 0 TM segment=', num_sig_with_TM/num_with_signal)
#print ('The fraction of those (with > 0 signal peptide) with > 0 TM segment=', num_with_signal/num_with_TM)
f.close()

####Part II: This part of script gives out the outcomes for c in question 7. It has some overlapping function with Part I but has be used together with Part I, as the list "num_with_TM" is needed here.
f1=open ('18.prot.shortoutput.txt')
num_TM=[]
for line in f1:
	if line[0]=='.':
		line=line.strip().split(' ')
		line_ori_list=[]
		mediate1=[]
		mediate2=[]
		#topology_list1=[]
		for i1 in line:
			if i1!='':
				line_ori_list.append(i1)
		#print (line_ori_list)
		if line_ori_list[1]!='0':
			num_TM.append(int(line_ori_list[1]))
#print (num_TM)
total_num=0
for i3 in num_TM:
	total_num=total_num+i3
#print (total_num)
print ('The average number of TM segments for those with >0 segments=', total_num/num_with_TM)
f1.close()
