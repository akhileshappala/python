
# coding: utf-8

# In[5]:


import numpy as np 
a = np.array([1,2,3])
print (type(a), a.shape,a[0],a[1],a[2])
a[0]= 5 
print (a) 


# In[41]:


import numpy as np
b = np.array ([[1,2,3],[4,5,6]])
print (b)
print (b.shape)
print (b[0,0],b[0,1],b[1,0])
print (a) 
b = np.ones((1,2))
print (b)
c = np.full((2,2),7)
print (c)
c= np.eye(2)
print(c)
e = np.random.random((2,2))
print (e)




# In[51]:


a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print (a)
b= a[:2,1:3]
print (b)
print (a[0,1])


# In[53]:


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print (a)
row_r1 = a[1,:]
row_r2 = a[1:2, :]
row_r3 = a[[1],:]
print (row_r1 , row_r1.shape)
print (row_r2 , row_r2.shape) 
print (row_r3, row_r3.shape) 


# In[61]:


a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print (a)
b= np.array([0,2,0,1])
print (a[np.arange(4),b])


# In[64]:


import numpy as np 
a = np.array([[1,2],[3,4],[5,6]])
bool_idx = (a>2)
print (bool_idx)
print (a[a>2])


# In[69]:


x= np.array([[1,2],[3,4]],dtype = np.float64)
y = np.array([[5,6],[7,8]],dtype = np.float64)
z= np.array([[1,2],[3,4]],dtype = np.float64)
print (x+y+z )
print (np.add(x,y,z))


# In[73]:


x= np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v= np.array([1,0,1])
y = np.empty_like(x)

for i in range(4):
    y[i,:] = x[i ,:] +v
    
print (y)    
vv = np.tile(v,(4,1))
print (vv)

