1)
# importing Python library
import numpy as np
# define Unit Step Function
def unitStep(v):
if v >= 0:
return 1
else:
return 0
# design Perceptron Model
def perceptronModel(x, w, b):
v = np.dot(w, x) + b
y = unitStep(v)
return y
# NOT Logic Function
# wNOT = -1, bNOT = 0.5
def NOT_logicFunction(x):
wNOT = -1
bNOT = 0.5
return perceptronModel(x, wNOT, bNOT)
# AND Logic Function
# here w1 = wAND1 = 1,
# w2 = wAND2 = 1, bAND = -1.5
def AND_logicFunction(x):
w = np.array([1, 1])
bAND = -1.5
return perceptronModel(x, w, bAND)
# OR Logic Function
# w1 = 1, w2 = 1, bOR = -0.5
def OR_logicFunction(x):
w = np.array([1, 1])
bOR = -0.5
return perceptronModel(x, w, bOR)
# XOR Logic Function
# with AND, OR and NOT 
# function calls in sequence
def XOR_logicFunction(x):
y1 = AND_logicFunction(x)
y2 = OR_logicFunction(x)
y3 = NOT_logicFunction(y1)
final_x = np.array([y2, y3])
finalOutput = AND_logicFunction(final_x)
return finalOutput
# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])
print("XOR({}, {}) = {}".format(0, 1, XOR_logicFunction(test1)))
print("XOR({}, {}) = {}".format(1, 1, XOR_logicFunction(test2)))
print("XOR({}, {}) = {}".format(0, 0, XOR_logicFunction(test3)))
print("XOR({}, {}) = {}".format(1, 0, XOR_logicFunction(test4)))

print("AND({}, {}) = {}".format(0, 1, AND_logicFunction(test1)))
print("AND({}, {}) = {}".format(1, 1, AND_logicFunction(test2)))
print("AND({}, {}) = {}".format(0, 0, AND_logicFunction(test3)))
print("AND({}, {}) = {}".format(1, 0, AND_logicFunction(test4)))


2)
print("Enter the Initial Weights:")
w = list(map(int,input().split()))
# N = [[0,0,0]]
# P = [[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
N=[[1,0,0,0]]
P=[[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
while True:
temp = w[:]
for x in N:
sum = 0
for y in range(len(x)):
sum+=temp[y]*x[y]
if sum>=0:
for y in range(len(temp)):
temp[y]-=x[y]
for x in P:
sum = 0
for y in range(len(x)):
sum+=temp[y]*x[y]
if sum<0:
for y in range(len(temp)):
temp[y]+=x[y]
if temp==w:
break
w = temp[:]
print(w)
