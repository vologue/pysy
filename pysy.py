import pysynth
import numpy as np
import math
import time
#l=np.random.randint(low=97, high=103, size=10)
#k=np.random.randint(low=1, high=6, size=10)
w1=np.random.randint(low=100,high=2000,size=3)/1000
w2=np.random.randint(low=100,high=2000,size=3)/1000
w3=np.random.randint(low=100,high=2000,size=3)/1000
w4=np.random.randint(low=100,high=2000,size=1)/1000
wa=[]
wa.append(w2)
wa.append(w3)
song = [['c', 4],
  ['c', 4],['e', 4], ['g', 4],
  ['g', 2],['g', 4],['g', 4],['r', 4], ['e', 4],['e', 4],['c', 4],
  ['c', 4],['e', 4], ['g', 4],
  ['g', 2],['g', 4],['g', 4],['r', 4], ['e', 4],['e', 4] ]
def train(out,i):
	sdif=out[1]-song[i][1]
	ndif=ord(out[0])-ord(song[i][0])
	ndif=ndif/7
	sdif=sdif/6
	tdif=sdif+ndif
	tdif=tdif/30
	for itr in range(0,3):
		w1[itr]=w1[itr]+tdif
		w2[itr]=w2[itr]+tdif
		w3[itr]=w3[itr]+tdif
	for itr in range(0,1):
		w2[itr]=w2[itr]+tdif

def nextnotetrain(las):
	l=np.random.randint(low=97, high=103, size=1)
	k=np.random.randint(low=1, high=6, size=1)
	fi=[las]
	l1=[]
	l2=[]
	l3=[]
	temp=[0,0]
	for i in range(0,3):
		l1.append(nodeval(fi,w1[i]))
	for i in range(0,3):
		l2.append(nodeval(l1,w2[i]))
	for i in range(0,3):
		l3.append(nodeval(l2,w3[i]))
	note=nodeval(l3,w2[0])
	note[0]=chr(note[0])
	return note
def starttrain():
	print("Tentative Neural Net:")
	print(w1)
	print(w2)
	print(w3)
	print(w4)
	for i in range(0,19):
		o=nextnotetrain([ord(song[i][0]),song[i][1]])
		train(out=o,i=i+1)
		print('Training nn epoch %d'%(i))
		print(w1)
		print(w2)
		print(w3)
		print(w4)

	print('Generated Neural Net:')
	print(w1)
	print(w2)
	print(w3)
	print(w4)

def nodeval(ic,w):
	summ=0
	octet=0
	for j in ic:
		summ=summ+j[0]*w
		octet=octet+j[1]*w
	summ=math.floor(summ)
	octet=math.floor(octet)
	summ=(summ%7)+97
	octet=octet%9 +1
	o=[summ,octet]
	return o
keys=[]
starttrain()
fnot=input("Enter first note :")
sc=int(input("Enter the scale :"))
numno=int(input("Enter length of music (number of notes):"))
keys.append((fnot,sc))

def nextnote(las):
	l=np.random.randint(low=97, high=103, size=1)
	k=np.random.randint(low=1, high=6, size=1)
	fi=[las]
	fi.append([l[0],k[0]])
	l1=[]
	l2=[]
	l3=[]
	temp=[0,0]
	for i in range(0,3):
		l1.append(nodeval(fi,w1[i]))
	for i in range(0,3):
		l2.append(nodeval(l1,w2[i]))
	for i in range(0,3):
		l3.append(nodeval(l2,w3[i]))
	note=nodeval(l3,w4[0])
	note[0]=chr(note[0])
	return note


for i in range (0,numno):
	last=[ord(keys[-1][0]),keys[0][1]]
	nn=nextnote(last)
	keys.append((nn[0],nn[1]))

print(keys)
pysynth.make_wav(keys, fn = "class.wav")
