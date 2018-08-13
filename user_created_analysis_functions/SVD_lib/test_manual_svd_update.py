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
	#fig = plt.figure()
	#ax = fig.add_subplot(111)
	fig, ax_list = plt.subplots(1, 2)
	line1, = ax_list[0].plot(x,X[:,-1])
	line2, = ax_list[0].plot(x,X[:,-1],'o')
	line3, = ax_list[1].plot(arange(2),arange(2))
	line4, = ax_list[1].plot(arange(2),arange(2))

	plt.pause(0.0001)
	
	update_L2_norm = []
	standard_L2_norm = []

	for i in arange(initial_stack_size,y_stack.shape[0]):

		#standard SVD for baseline comparison

		X = y_stack[:(i+1)].transpose()

		U,s,V = svd(X,full_matrices=True)

		try:
			S = zeros([U.shape[0],V.shape[0]])
			S[:len(s),:len(s)] += diag(s)
			standard_svd_reconstructed = dot(dot(U,S),V)
		except:
			IPython.embed()

		standard_L2_norm.append(sum((standard_svd_reconstructed-X)**2))

		#update SVD under test

		a = X[:,-1]
		
		U_updated,s_updated,V_updated = svd_rank_one_update(U_updated,s_updated,V_updated,a)	

		update_reconstructed = dot(dot(U_updated,diag(s_updated)),V_updated)
	
		update_L2_norm.append(sum((update_reconstructed-X)**2))
		
		#print(str(standard_L2_norm[-1])+", "+str(update_L2_norm[-1]))
		#print("V.shape = "+str(V_updated.shape)+", s_updated.shape = "+str(s_updated.shape)+", U.shape = "+str(U_updated.shape))
		print("V.shape = "+str(V.shape)+", s.shape = "+str(s.shape)+", U.shape = "+str(U.shape))

		#visualization
		line1.set_ydata(a)
		line2.set_ydata(update_reconstructed[:,-1])
		line3.set_xdata(arange(len(standard_L2_norm)))
		line4.set_xdata(arange(len(update_L2_norm)))
		line3.set_ydata(standard_L2_norm)
		line4.set_ydata(update_L2_norm)
		ax_list[1].set_xlim(0,len(standard_L2_norm))
		ax_list[1].set_ylim(0,max(update_L2_norm))
		plt.pause(0.0001)
		fig.canvas.draw()
		plt.pause(0.0001)
		fig.canvas.flush_events()
		plt.pause(0.0001)

if __name__ == '__main__':
	main()
