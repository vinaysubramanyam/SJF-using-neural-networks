from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet,UnsupervisedDataSet
from pybrain.structure import LinearLayer

ds=SupervisedDataSet(5,1)
ds.addSample(map(int,'1 2 3 4 5'.split()),map(int,'8'.split()))
ds.addSample(map(int,'2 3 4 5 6'.split()),map(int,'9'.split()))
ds.addSample(map(int,'8 2 6 9 1'.split()),map(int,'5'.split()))
ds.addSample(map(int,'3 6 1 9 4'.split()),map(int,'2'.split()))
ds.addSample(map(int,'4 8 1 5 3'.split()),map(int,'7'.split()))
ds.addSample(map(int,'9 1 6 4 8'.split()),map(int,'3'.split()))
ds.addSample(map(int,'5 6 7 3 2'.split()),map(int,'1'.split()))
ds.addSample(map(int,'7 3 5 1 9'.split()),map(int,'4'.split()))
ds.addSample(map(int,'6 8 2 4 1'.split()),map(int,'3'.split()))
ds.addSample(map(int,'1 3 2 7 9'.split()),map(int,'5'.split()))
ds.addSample(map(int,'2 4 6 8 3'.split()),map(int,'7'.split()))
ds.addSample(map(int,'8 3 5 8 1'.split()),map(int,'4'.split()))
ds.addSample(map(int,'3 5 7 2 8'.split()),map(int,'9'.split()))
ds.addSample(map(int,'9 5 7 3 8'.split()),map(int,'1'.split()))
ds.addSample(map(int,'7 3 6 9 1'.split()),map(int,'8'.split()))
ds.addSample(map(int,'4 3 6 7 8'.split()),map(int,'5'.split()))
ds.addSample(map(int,'2 4 5 6 7'.split()),map(int,'3'.split()))
ds.addSample(map(int,'1 7 3 9 2'.split()),map(int,'6'.split()))
ds.addSample(map(int,'7 1 7 9 6'.split()),map(int,'4'.split()))
ds.addSample(map(int,'4 5 5 4 5'.split()),map(int,'9'.split()))
ds.addSample(map(int,'5 5 6 5 6'.split()),map(int,'1'.split()))
ds.addSample(map(int,'2 2 3 3 3'.split()),map(int,'8'.split()))
ds.addSample(map(int,'6 6 7 7 7'.split()),map(int,'3'.split()))
ds.addSample(map(int,'2 1 1 2 1'.split()),map(int,'7'.split()))
ds.addSample(map(int,'5 6 5 6 5'.split()),map(int,'2'.split()))
ds.addSample(map(int,'4 5 4 5 4'.split()),map(int,'9'.split()))
ds.addSample(map(int,'7 8 7 8 7'.split()),map(int,'4'.split()))
ds.addSample(map(int,'4 4 4 4 4'.split()),map(int,'8'.split()))
ds.addSample(map(int,'3 5 3 5 3'.split()),map(int,'7'.split()))
ds.addSample(map(int,'3 4 5 6 7'.split()),map(int,'2'.split()))
ds.addSample(map(int,'6 8 6 8 6'.split()),map(int,'3'.split()))
ds.addSample(map(int,'1 2 1 2 1'.split()),map(int,'9'.split()))
ds.addSample(map(int,'4 6 4 6 4'.split()),map(int,'8'.split()))
ds.addSample(map(int,'2 5 9 3 5'.split()),map(int,'1'.split()))
net=buildNetwork(5,50,1,outclass=LinearLayer,bias=True,recurrent=True)
trainer=BackpropTrainer(net,ds)
trainer.trainEpochs(100)


n=input("Enter number of process:")
print "Enter the burst time of first five process:"
bt=[]
p=[]
for i in range(0,5):
    bt.append(int(input("p%(x)d :"%{"x":i+1})))
for i in range(0,n):
    p.append(i+1)
for l in range(5,n):
    a=str(bt[l-5])
    b=str(bt[l-4])
    c=str(bt[l-3])
    d=str(bt[l-2])
    e=str(bt[l-1])
    ts=UnsupervisedDataSet(5,)
    ts.addSample(map(int,[a,b,c,d,e]))
    x=net.activateOnDataset(ts)
    bt.append(int(x))

print "----------------------------------------------------------------"
print "                      FCFS                                      "
print "----------------------------------------------------------------"
wt=[0]
total=0
for i in range(1,n):
    wt.append(0);	
    for j in range(0,i):
        wt[i]+=bt[j]
    total+=wt[i]
avg_wt1=float(total)/n
total=0
print "Process    Burst time    waiting time    Turnaround Time"
tat=[]
for i in range(0,n):
    tat.append(bt[i]+wt[i])
    total+=tat[i]
    print "p%-9d %-13d %-15d %-10d"%(p[i],bt[i],wt[i],tat[i])
avg_tat1=float(total)/n
print "Average waiting time=%(k)f"%{"k":avg_wt1}
print "Average turnaround time=%(l)f"%{"l":avg_tat1}

print "---------------------------------------------------------------"
print "                      SJF                                      "
print "---------------------------------------------------------------"
k=0
for l in range(5,n):
    for i in range(k,l):
        pos=i
        for j in range(i+1,l):
            if bt[j]<bt[pos]:
                pos=j
	temp=bt[i]
        bt[i]=bt[pos]
        bt[pos]=temp
        temp=p[i]
        p[i]=p[pos]
        p[pos]=temp
    k=k+1
wt=[0]
total=0
for i in range(1,n):
    wt.append(0);	
    for j in range(0,i):
        wt[i]+=bt[j]
    total+=wt[i]
avg_wt2=float(total)/n
total=0
print "Process    Burst time    waiting time    Turnaround Time"
tat=[]
for i in range(0,n):
    tat.append(bt[i]+wt[i])
    total+=tat[i]
    print "p%-9d %-13d %-15d %-10d"%(p[i],bt[i],wt[i],tat[i])
avg_tat2=float(total)/n
print "Average waiting time=%(k)f"%{"k":avg_wt2}
print "Average turnaround time=%(l)f"%{"l":avg_tat2}
print "----------------------------------------------------------------"
print "Difference in average waiting time=%f"%(avg_wt1-avg_wt2)
print "Difference in average turnaround time=%f"%(avg_tat1-avg_tat2)
