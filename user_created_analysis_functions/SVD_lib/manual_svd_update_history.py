##################
### working history of svd update of rank one.  Needs to be refined
### manual implementation. success happens in last few lines. 
##################
X.shape
b = zeros(X.shape[0])
b[-1]=1
a
plot(a)
show()
plot(a[:,0])
show()
a
plot(a[0,L])
plot(a[0,L])
plot(a[0,:])
show()
m = dot(U.transpose(),a)
m = dot(U.transpose(),y_stack[501])
a = np.reshape(np.array(y_stack[501]), (-1, 1))
m = dot(U.transpose(),a)
m
plot(m[0,:])
show()
plot(m[:,0])
show()
p=a-dot(U,m)
p
s.shape
n.shape
m.shape
diag(S)
diag(s)
diag(s).shape
U.shape
V.shape
p
dot(p,p)
dot(p,p.transpose())
dot(p.transpose(),p)
P = p/dot(p.transpose(),p)**0.5
P
plot(p[0,:])
show()
plot(p[:,0])
show()
Ra = dot(p.transpose(),p)**0.5
K = array([[diag(s),m],[zeros(len(s)),Ra]])
K
K[0]
K[0].shape
K[0,0].shape
K[0,1].shape
K = array([[diag(s),Ra],[zeros(len(s)),m]])
K
K.shape
diag(s).shape
S
S = diag(append(s,0))
S.shape
K = 0+ S
K.shape
K[-1,-1]=Ra
K[:-1,-1]=m
K[:-1,-1]
m
K[:-1,-1]=m[:,0]
K
K.shape
K[:,-1]
Ra
eig(K)
eig?
len(eig(K))
eig(K)[0].shape
eig(K)[1].shape
eig_vals , eig_vec = eig(K)
S
s
plot(s)
plot(eig_vals)
show()
plot(s)
show()
plot(s,eig_vals[:len(s)])
show()
clear
clear
X = y_stack[:5].transpose()                          #X.shape = (100,500)
U, s, V = np.linalg.svd(X, full_matrices = False)      #U.shape = (500,100), s.shape = (100,), V.shape = (100,500)
a = y_stack[6]
m = dot(U.transpose(),a)
p=a-dot(U,m)
plot(p)
show()
Ra = dot(p.transpose(),p)**0.5
P = p/dot(p.transpose(),p)**0.5
plot(P)
show()
n = dot(V.transpose(),b)
b = zeros(X.shape[0])
n = dot(V.transpose(),b)
X.shape
b = zeros(X.shape[1])
n = dot(V.transpose(),b)
q = b-dot(V,n)
Rb = dot(q.transpose(),q)
Q = q/Rb
Q
Rb
b[-1] = 1
n = dot(V.transpose(),b)
q = b-dot(V,n)
Rb
Rb
Rb = dot(q.transpose(),q)
Rb
Q = q/Rb
Q
Rb = dot(q.transpose(),q)**0.5
Q = q/Rb
Q
K = 0+ S
K = diag(zeros(len(s)+1))
K[:-1,:-1] = diag(s)
K[-1,-1]=Ra
K[:-1,-1]=m[:,0]
K[:-1,-1]=m
K.shape
m.shape
K
Ra
eig_vals , eig_vec = eig(K)
plot(s,eig_vals[:len(s)])
show()
eig_vals
s
Ra
K
K.shape
Ra
eig_vals , eig_vec = eig(K.transpose())
eig_vals
s
eig_vals , eig_vec = eig(K)
eig_vec
U.shape
P.shape
hstack([U,P])
vstack([U,P])
array([U,P])
U.shape
P.shape
append(U,P)
append(U,P).shape
append?
hstack([U.transpose(),P])
vstack([U.transpose(),P])
vstack([U.transpose(),P]).shape
vstack([U.transpose(),P]).transpose()
vstack([U.transpose(),P]).transpose().shape
U.shape
dot(vstack([U.transpose(),P]).transpose().shape,eig_vec)
eig_vec.shape
dot(vstack([U.transpose(),P]).transpose(),eig_vec)
dot(dot(vstack([U.transpose(),P]).transpose(),eig_vec),eig_vals)
temp = dot(dot(vstack([U.transpose(),P]).transpose(),eig_vec),eig_vals)
vstack([V,Q])
temp = dot(dot(vstack([U.transpose(),P]).transpose(),eig_vec.transpose()),eig_vals)
dot(vstack([V,Q]),inv(eig_vec))
dot(vstack([V,Q]).transpose(),inv(eig_vec))
dot(vstack([V,Q]).transpose(),inv(eig_vec)).shape
dot(vstack([V,Q]).transpose(),inv(eig_vec))
dot(temp,dot(vstack([V,Q]).transpose(),inv(eig_vec)))
temp.shape
S.shape
eig_vec.shape
temp = dot(dot(vstack([U.transpose(),P]).transpose(),eig_vec.transpose()),diag(eig_vals))
temp.shape
dot(temp,dot(vstack([V,Q]).transpose(),inv(eig_vec)))
dot(vstack([V,Q]).transpose(),inv(eig_vec)).shape
X.shape
U.shape
eig_vec.shape
U_P_dot_Up = dot(vstack([U.transpose(),P]))
U_P_dot_Up = dot(vstack([U.transpose(),P]),eig_vec)
U_P_dot_Up = dot(vstack([U.transpose(),P]).transpose(),eig_vec)
U_P_dot_Up.shape
V_Q_dot_Vq = dot(vstack([V,Q]).transpose(),inv(eig_vec))
V_Q_dot_Vq.shape
V.shape
eig_vec.shape
V_Q_dot_Vq = dot(vstack([vstack([V,zeros(len(vstack))]),Q]).transpose(),inv(eig_vec))
V_Q_dot_Vq = dot(vstack([vstack([V,zeros(len(V))]),Q]).transpose(),inv(eig_vec))
V.shape
V_Q_dot_Vq = dot(vstack([hstack([V,zeros(len(V))]),Q]).transpose(),inv(eig_vec))
V_Q_dot_Vq = dot(vstack([vstack([V,zeros(len(V))]),Q]).transpose(),inv(eig_vec))
V_Q_dot_Vq = dot(vstack([hstack([V,zeros(len(V))]),Q]).transpose(),inv(eig_vec))
hstack([V,zeros(len(V))])
vstack([V,zeros(len(V))])
vstack([V,zeros(len(V))]).shape
V.shape
V = vstack([V,zeros(len(V))])
n = dot(V.transpose(),b)
U, s, V = np.linalg.svd(X, full_matrices = False)
b.shape
b = zeros(X.shape[1]+1)
V = vstack([V,zeros(len(V))])
n = dot(V.transpose(),b)
q = b-dot(V,n)
Rb = dot(q.transpose(),q)**0.5
Q = q/Rb
Q
b = zeros(X.shape[1]+1)
b[-1] = 1
n = dot(V.transpose(),b)
q = b-dot(V,n)
Rb = dot(q.transpose(),q)**0.5
Q
Q = q/Rb
V_Q_dot_Vq = dot(vstack([vstack([V,zeros(len(V))]),Q]).transpose(),inv(eig_vec))
vstack([V,zeros(len(V))])
V.shape
)
V_Q_dot_Vq = dot(vstack([V,Q]).transpose(),inv(eig_vec))
V.shape
Q.shape
vstack([V,Q])
hstack([V,Q])
vstack([V.tanspose(),Q])
vstack([V.transpose(),Q])
vstack([V.transpose(),Q]).transpose()
vstack([V.transpose(),Q]).transpose().shape
V_Q_dot_Vq = dot(vstack([V.transpose(),Q]).transpose(),inv(eig_vec))
U_P_dot_Up = dot(vstack([U.transpose(),P]).transpose(),eig_vec)
dot(U_P_dot_Up,diag(eig_vals))
dot(U_P_dot_Up,diag(eig_vals)).shape
dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq)
dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq).shape
reconstructed = dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq)
reconstructed[:,0]
plot(reconstructed[:,0])
show()
%matplotlib
plot(reconstructed[:,0])
plot(y_stack[:,0,'o'])
plot(y_stack[:,0],'o')
plot(reconstructed[:,0])
plot(y_stack[0],'o')
plot(y_stack[5],'o')
plot(reconstructed[:,5])
plot(y_stack[1],'o')
plot(reconstructed[:,1])
plot(y_stack[2],'o')
plot(reconstructed[:,3])
U_P_dot_Up = dot(vstack([U.transpose(),P]).transpose(),inv(eig_vec))
history
################
##got it working somewhere here
#################
U_P_dot_Up = dot(vstack([U.transpose(),P]).transpose(),inv(eig_vec).transpose())
V_Q_dot_Vq = dot(vstack([V.transpose(),Q]).transpose(),(eig_vec))
reconstructed[:,0]
reconstructed = dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq)
plot(reconstructed[:,0])
plot(y_stack[2],'o')
plot(reconstructed[:,1])
plot(y_stack[1],'o')
plot(reconstructed[:,6])
plot(reconstructed[:,5])
reconstructed.shape
plot(y_stack[5],'o')
U_P_dot_Up = dot(vstack([U.transpose(),P]).transpose(),eig_vec)
V_Q_dot_Vq = dot(vstack([V.transpose(),Q]).transpose(),inv(eig_vec).transpose())
reconstructed.shape
reconstructed = dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq)
plot(reconstructed[:,5])
V_Q_dot_Vq = dot(vstack([V.transpose(),Q]).transpose(),inv(eig_vec))
U_P_dot_Up = dot(vstack([U.transpose(),P]).transpose(),eig_vec.transpose())
plot(reconstructed[:,5])
plot(reconstructed[:,0])
plot(reconstructed[:,4])
plot(reconstructed[:,2])
plot(reconstructed[:,1])
plot(reconstructed[:,5])
clear
eig_vals , eig_vec = eig(K)
K
dot(eig_vec.transpose(),eig_vec)
K
dot(dot(eig_vec,eig_vals),inv(eig_vec))
s
dot(dot(inv(eig_vec,eig_vals)),(eig_vec))
dot(dot(inv(eig_vec),eig_vals),(eig_vec))
K
s
dot(dot(inv(eig_vec),eig_vals),(eig_vec))
dot(dot(eig_vec,eig_vals),inv(eig_vec))
clear
clear
dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
K
U_P_dot_Up = vstack([U.transpose(),P]).transpose()
V_Q = vstack([V.transpose(),Q]).transpose()
U_P = vstack([U.transpose(),P]).transpose()
reconstructed = dot(U_P,K)
reconstructed = dot(dot(U_P,K),V_Q)
reconstructed.shape
plot(reconstructed[:,5])
plot(y_stack[5],'o')
plot(y_stack[0],'o')
plot(reconstructed[:,0])
plot(reconstructed[:,3])
plot(y_stack[3],'o')
plot(reconstructed[:,4])
plot(y_stack[4],'o')
a = np.reshape(np.array(y_stack[5]), (-1, 1))
a = y_stack[5]
m = dot(U.transpose(),a)
p=a-dot(U,m)
Ra = dot(p.transpose(),p)**0.5
P = p/dot(p.transpose(),p)**0.5
n = dot(V.transpose(),b)
q = b-dot(V,n)
Rb = dot(q.transpose(),q)**0.5
Q = q/Rb
K = diag(zeros(len(s)+1))
K[:-1,-1]=m
K[:-1,:-1] = diag(s)
K[-1,-1]=Ra
eig_vals , eig_vec = eig(K)
reconstructed = dot(dot(U_P,K),V_Q)
plot(y_stack[4],'o')
plot(reconstructed[:,4])
plot(reconstructed[:,5])
plot(y_stack[5],'o')
plot(reconstructed[:,6])
reconstructed = dot(dot(U_P,K),V_Q)
dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
K
dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
temp = dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
U_P_dot_Up = dot(U_P,eig_vec)
V_Q_dot_Vq = dot(V_Q,inv(eig_vec))
reconstructed = dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq.transpose())
plot(reconstructed[:,6])
plot(reconstructed[:,5])
plot(reconstructed[:,4])
temp = dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
clear
clear
dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
K
temp = dot(dot(eig_vec,diag(eig_vals)),inv(eig_vec))
reconstructed = dot(dot(U_P,K),V_Q)
plot(reconstructed[:,5])
plot(y_stack[5],'o')
dot(inv(eig_vec),V_Q)
V_Q_dot_Vq = dot(inv(eig_vec),V_Q)
reconstructed = dot(dot(U_P_dot_Up,diag(eig_vals)),V_Q_dot_Vq)
plot(y_stack[5],'o')
plot(reconstructed[:,5])
plot(reconstructed[:,0])
plot(reconstructed[:,0])
plot(y_stack[0],'o')
history

