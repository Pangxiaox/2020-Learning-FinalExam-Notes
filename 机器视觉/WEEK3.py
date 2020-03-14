from mxnet import nd
from mxnet import autograd
import numpy as np

x = nd.arange(12)
print(x)

X = x.reshape((3, 4))
print(X)

Y = nd.array([[2,1,4,3],[1,2,3,4],[4,3,2,1]])
print(Y)

print(X+Y)

print(X*Y)

print(X/Y)

print(Y.exp())

print(nd.dot(X, Y.T))

print(nd.concat(X,Y,dim=0))

print(nd.concat(X,Y,dim=1))

print(X == Y)

print(X.sum())

print(X.sum().asscalar())

A = nd.arange(3).reshape((3,1))
B = nd.arange(2).reshape((1,2))

print(A)

print(B)

print(A+B)

P = np.ones((2,3))

print(P)

D = nd.array(P)

print(D)

##########  自动求梯度
x = nd.arange(20).reshape((20,1))

print(x)

x.attach_grad()

with autograd.record():
    y = 2 * nd.dot(x.T,x)

y.backward()

print(x.grad)
