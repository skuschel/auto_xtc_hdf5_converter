# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import pyplot as plt
from manual_svd_update import svd_rank_one_update
import IPython

def main():

	#making test data

	def y(t,f,a,tau,phi):
		return a*exp(-t/tau)*sin(2*pi*f*x+phi)

	x = arange (0,10,0.1)
	y_stack = y(x,1.0,1.0,3,0)
	for i in arange(1000):
		y_stack = vstack([y_stack,y(x,1.0*(0.9+rand()/5),1.0*(0.9+rand()/5),3*(0.9+rand()/5),0)])

	initial_stack_size = 5
	X = y_stack[:initial_stack_size].transpose()	

	#initialize svd strategies for comparison
	U,s,V = svd(X)

	U_updated,s_updated,V_updated = svd(X,full_matrices = False)

	plt.ion()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	line1, = ax.plot(x,X[:,-1])
	line2, = ax.plot(x,X[:,-1],'o')
	plt.pause(0.0001)
	
	for i in arange(initial_stack_size,y_stack.shape[0]):

		#standard SVD for baseline comparison

		X = y_stack[:(i+1)].transpose()

		U,s,V = svd(X,full_matrices=False)

		standard_svd_reconstructed = dot(dot(U,diag(s)),V)

		standard_L2_norm = sum((standard_svd_reconstructed-X)**2)

		#update SVD under test

		a = X[:,-1]
		U_updated,s_updated,V_updated = svd_rank_one_update(U_updated,s_updated,V_updated,a)	
		update_reconstructed = dot(dot(U_updated,diag(s_updated)),V_updated)
	
		update_L2_norm = sum((update_reconstructed-X)**2)
		
		print(str(standard_L2_norm)+", "+str(update_L2_norm))

		#visualization
		line1.set_ydata(a)
		line2.set_ydata(update_reconstructed[:,-1])
		plt.pause(0.0001)
		fig.canvas.draw()
		plt.pause(0.0001)
		fig.canvas.flush_events()
		plt.pause(0.0001)

	axarr[0,0].plot()

if __name__ == '__main__':
	main()
