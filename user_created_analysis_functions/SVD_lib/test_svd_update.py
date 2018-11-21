
# coding: utf-8

# In[1]:

from pylab import *
from SVDUpdate import *

DEBUG=False

# In[2]:


x = arange (0,10,0.1)


# In[3]:


def y(t,f,a,tau,phi):
    return a*exp(-t/tau)*sin(2*pi*f*x+phi)


# In[4]:

if(DEBUG):
    figure(0)
    plot(x,y(x,1.0,1.0,3,0))
    show()


# In[5]:


y_stack = y(x,1.0,1.0,3,0)
for i in arange(1000):
    y_stack = vstack([y_stack,y(x,1.0*(0.9+rand()/5),1.0*(0.9+rand()/5),3*(0.9+rand()/5),0)])


# In[6]:


y_stack.shape


# In[7]:
if(DEBUG):
    figure(1)
    plot(y_stack[:4].transpose())
    show()


# In[14]:


u,s,v = svd(y_stack[:4],full_matrices=False)


# In[15]:
if(DEBUG):
    figure(2)
    plot(v[0])
    show()


###########
### example
###########

#X = np.array([[1.0,2.0,3.0,4.0],[3.0,2.0,5.0,5.0],[5.0,3.0,1.0,1.0],[7.0,7.0,7.0,7.0]])
#U, s, V = np.linalg.svd(X, full_matrices = False)
#a = np.reshape(np.array([4.0,5.0,1.0,7.0]), (-1, 1))
#U, S, V = svd_update(U, np.diag(s), V, X, a, update = True)


# In[21]:

###########
### application
###########

X = y_stack[:5].transpose()
U, s, V = np.linalg.svd(X, full_matrices = False)
a = np.reshape(np.array(y_stack[5]), (-1, 1))
u_new, s_new, v_new = svd_update(U, np.diag(s), V, X, a, update = True)

