# -*- coding: utf-8 -*-
##########################################
##########################################
# File and Version Information:
#  README 2019-08-11 18:54:12Z sioan@SLAC.STANFORD.EDU $
#
# Description:
#  README file for data analysis
#------------------------------------------------------------------------

#Package author: Sioan Zohar

#Brief description:
#==================
## based off of Linear Algebra and its Applications 415 (2006) 20–30
## www.elsevier.com/locate/laa
## Fast low-rank modifications of the thin singular
## value decomposition
## Matthew Brand
## MERL, 201 Broadway, Cambridge, MA 02139, USA
## Received 28 May 2003; accepted 27 July 2005
## Available online 27 September 2005
## Submitted by Kugazov
## equation numbers referenced in this implementation refer to the equations in the publication above 
## purpose is to validate functionality and reduce memory load
## speed optimization will be iplemented closer to silicon
##########################################
##########################################
##########################################

from pylab import *
import IPython

DEBUG = False

def svd_rank_one_update(U,s,V,a):

	##############################
    #####   Table 1   ############
    ##############################
 
	b = zeros(len(s)+1)
	b[-1] = 1

	##############################
    #####   equations 6   ########
    ##############################
	m  = dot(U.transpose(),a)			
	p  = a-dot(U,m)						
	Ra = dot(p.transpose(),p)**0.5
	P  = p/dot(p.transpose(),p)**0.5

	##############################
    #####   equations 7   ########
    ##############################
	
	V = vstack([V,zeros(len(V))])
	n  = dot(V.transpose(),b)
	q  = b-dot(V,n)
	Rb = dot(q.transpose(),q)**0.5
	Q  = q/Rb

	##############################
    #####   equation 9   #########
    ##############################
	K          = diag(zeros(len(s)+1))
	K[:-1,-1]  = m
	K[:-1,:-1] = diag(s)
	K[-1,-1]   = Ra

	##############################
    #####   equation 5   #########
    ##############################

	U_P = vstack([U.transpose(),P]).transpose()       #U_P = [U P] from equation 5
	V_Q = vstack([V.transpose(),Q]).transpose()       #V_Q = [V Q] from equation 5
	
	eig_vals , eig_vec = eig(K)                       #from text above equation 5 but after equation 4
													  #sparse matrix will improve performance

	U_P_dot_Up = dot(U_P,eig_vec)
	V_Q_dot_Vq = dot(inv(eig_vec),V_Q)

	return U_P_dot_Up,eig_vals,V_Q_dot_Vq             # udpated_u, updated_s,updated_v

def main():

	##########################################
	## creating test data
	##########################################

	def y(t,f,a,tau,phi):
		return a*exp(-t/tau)*sin(2*pi*f*x+phi)

	if(DEBUG):
		figure(0)
		plot(x,y(x,1.0,1.0,3,0))
		show()

	x = arange (0,10,0.1)
	y_stack = y(x,1.0,1.0,3,0)
	for i in arange(1000):
		y_stack = vstack([y_stack,y(x,1.0*(0.9+rand()/5),1.0*(0.9+rand()/5),3*(0.9+rand()/5),0)])

	##########################################
	## SVD update
	##########################################

	#selecting and conditioning data 
	X = y_stack[:5].transpose()	
	U,s,V = svd(X,full_matrices = False)
	a = y_stack[5]

	U_updated,s_updated,V_updated = svd_rank_one_update(U,s,V,a)

	reconstructed = dot(dot(U_updated,diag(s_updated)),V_updated)

	for i in arange(6):
		figure(i)
		plot(reconstructed[:,i])
		plot(y_stack[i],'o')

	show()

if __name__ == '__main__':
	main()

