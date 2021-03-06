import numpy as np 
import time 

def add_y_intercept(X):
	m = X.shape[0]
	return np.column_stack([np.ones([m,1]), X])

def normalise(X):
	mu = np.mean(X, 0)
	Xnorm = X - mu
	sigma = Xnorm.std(0, ddof = 1)
	return np.divide(Xnorm, sigma)

def cost(X, y, theta):
	
	m = y.shape[0]
	h = X * theta
	error = h - y
	cst = (1./(2.*m)) * np.sum(np.square(error))
	return cst

def gradient_descent(X, y, theta, alpha,  iters):
	cs = np.zeros(iters)
	m = float(y.shape[0])
	for i in range(iters):
		gradient= (1. / m) * (((X * theta) - y).T * X)
		theta= theta - (gradient.T * alpha)
		cs[i] = cost(X, y, theta)
	
	return theta,cs
	

