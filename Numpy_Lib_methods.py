# Numpy Library
'''first type in console >> pip install numpy 
and import it used it as np and also i repeated variable a which is for good understanding which is bad for programmer'''

import numpy as np
# =============================================================================
# 
# =============================================================================
a = np.array((1,2,3,('a')))
# print(a)

a= np.array([1,2,3,('a')])
# print(a)

# a= np.array([1,2,3,('a','b')])
# print(a) # it ll cause error we ll talk later on it

'''above 2 result you can see array is in list either you feed in tuple or list'''

# print(type(a)) # its shows you type 
'''result (<class 'numpy.ndarray'>)'''

a= np.array([1,2,3,('a')])
a.shape
# print(a.shape)
 
'''its shows you rank and dimensions of array 
result provide you >>(4,) because it have 4 rank 
namely 1,2,3,a and none dimensions ''' 

b = np.array([[1,2],[3,'x'],[2,3]])
b.shape
# print(b.shape)

'''result>> (3,2) means its have 3 rank and every rank have 2 dimensions 
note* all rank should have same dimensions '''

# lets print x by indexing 

b = np.array([[1,2,3],[4,5,6],[7,8,9],[7,7,'x']])
b[3,2]
# print(b[3,2])

'''indexing start from 0 and input is 3 so we jumped into rank [7,7,'x']
and we provided 2 as index of rank which is x'''
# =============================================================================
# 
# =============================================================================
'''function to create numpy array'''

#creating array 

d = np.zeros((2,))
# print(d)

''' you are creating rank 2 array with zero dimension you may use commas or not for this'''

'''lets create 3 rank with four dimension'''

c= np.ones((3,4))
# print(c)

# lets create constant array

'''this required 2 postional argument shape and fill value
a constant number which is on 2nd postional arg  and array size on 1st'''

c = np.full((2,3),5)
# print(c)

'''create 2*2 identity matrix'''

'''.eye can take 4 max arg 1st example we take 2 in result we get 2*2 indentity matrix
we take (3,4) as a rank 3 with 4 dimension we provided 1 on its diagonal 
in last we provided (3,4,1) you can see result here 1 is behave like index of a dimension of first rank
so matrix created accordingly'''

c = np.eye(2)
# print(c)
c = np.eye(3,4)
# print(c)
c = np.eye(3,4,1)
# print(c)

'''number in a matrix are in float you can provided last argument dtype in above example''' 

# create random array filled

c = np.random.random((3,3))
# print(c)

'''getting started with array in numpy (contradiction)'''

'''arange: returns evenly spaced values within a given interval. step size is specified.
linspace: returns evenly spaced values within a given interval. num no. of elements are returned.
'''

a = np.arange(0,30,5)
# print(a)
'''result provide number in array start = 0 (end =30which ll not print) with a gap of 5'''
# =============================================================================
# 
# =============================================================================
''' let divide 0 to 10 by four parts'''

# parts(num) default value is 50

a= np.linspace(0,10)
# print(a)

a= np.linspace(0,10,4)
# print(a)

'''result 0 to 10 divided by 50 parts which is defualt
linspace req 2 compalsary positional arg start and stop and 5 optional arguement which is part(num),axis,dtype etc'''
# =============================================================================
# 
# =============================================================================
'''Reshaping array: We can use reshape method to reshape an array. 

Consider an array with shape (a1, a2, a3, ..., aN). 
We can reshape and convert it into another array with shape (b1, b2, b3, ....., bM). 
The only required condition is:    a1 x a2 x a3 .... x aN = b1 x b2 x b3 .... x bM . 
i.e original size of array remains unchanged'''

# a = np.array([[1,2,3],[4,5,7],[8,6,3]])
'''error str  cannot be interpreted not even list , '''

# b = a.reshape(1,1,1,1,6) 
'''ValueError: cannot reshape array of size 9 into shape (1,1,1,1,6)
you cant just feed any number inside of reshape method'''

arr = np.array([[11, 32, 31, 90],
                [4, 0, 41, 29],
                [12, 21, 1, 17]])
newarr = arr.reshape(12)
# print(newarr)
newarr = arr.reshape(1,12)
# print(newarr)
newarr = arr.reshape(12,1)
# print(newarr)
newarr = arr.reshape(1,1,12)
# print(newarr)
newarr = arr.reshape(12,1,1)
# print(newarr)
newarr = arr.reshape(1,1,12,1,1)
# print(newarr)
# newarr = arr.reshape(1,12,2) # error
# print(newarr)

'''by above experiment you ll see the difference in result
12 is the dimension number u cant reduced dimension or it ll cause error as we see in line 129 provided 6 intead of 9'''
# =============================================================================
# 
# =============================================================================
'''silicing and idexing'''

a= np.array([[1,2,10],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
b= a[0:]
# print(b)
b= a[1:3]
# print(b)
b = a[:2]
# print(b)
b = a[1:2,:1]
# print(b)
b = a[1:3,:1]
# print(b)
b = a[1:3,0:2]
# print(b)

''' its just making a new array what ever you provided rank number in 0 indexing and result of location
run one by one and see the differnce  '''

b =a[[5,5,5],[0,1,2]]
# print(b)
b =a[[5,5,5],[0,0,0]]
# print(b)
b =a[[5,5,5],[1,1,1]]
# print(b)

''' as you see 0,1,2 /0,0,0/1,1,1, are dimension indexing in a and what about 5,5,5 lets experiment more
'''
b =a[[5,5,5],[1,0,0]]
# print(b)
b =a[[5,3,4],[0,1,2]]
# print(b)

'''output is 16,11,15 why check out in line 184  5 in [5,3,4]and 0 in [0,1,2] ie 
([5,0],means 5th indexing rank which is [16,17,18] in this 0th indexing which is 16) so output is 16
similarly 3-1 gives you 11 and 4-2 gives you 15 hence provided you an array'''
# =============================================================================
# 
# =============================================================================
'''numpy operator'''
a= np.array([[1,2,10],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

#sum
a += 3
# print(a)

#qoutient
a //= 2
# print(a)

#exponential power
a **= 2
# print(a)

#Transpose of array
a = a.T
# print(a)

'''numpy operator part 2 '''

#maximum element of array 
a.max()
# print(a.max())
'''why result is 100 because you already applied to many operator above just comments those'''

#row wise maximum array
'''axix = 1 which is row axis = 0 which is cloumn''' 
a.max(axis = 1)
# print(a.max(axis = 1))

''' column wise min and max array'''
# print(a.min(axis = 0))
# print(a.max(axis = 0))
# =============================================================================
# 
# =============================================================================

'''sum of array on row '''
a= np.array([[1,2,10],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
# print(a)

'''it ll sum of all number in a row and print it seprately in array 
if your are confused with result just un-comment line 235 and your doubt ll be
clear'''

a.sum(axis = 1)
# print(a.sum(axis =1))

'''sum of array of coloum''' 
a.sum(axis =0)
# print(a.sum(axis = 0))

'''cumulative sum of row and coloum
it ll print whole array with cumulative sum'''

#along row
a.cumsum(axis=1)
# print(a.cumsum(axis=1))

# ALONG  cloumn 
a.cumsum(axis=0)
# print(a.cumsum(axis=0))

# =============================================================================
# 
# =============================================================================
'''operator in array 1.3'''

a= np.array([[1,2,10],[4,5,6]])
b= np.array([[1,1,11],[10,1,1]])

# print(a.dot(b)) Error
'''remeber the condition of multiplication of 2 matrix its failed here'''

a+b
# print(a+b)
a-b
# print(a-b)

'''it ll not multiply like matrix multiplication it ll simply multiply corresponding number'''
a*b
# print(a*b)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

'''multiplication of 2 maxtrix 
condition  = col of first matrix is equal to row of second matrix 
resulted matrix is remaining of row of first matrix and col of second matrix'''

a.dot(b)
# print(a.dot(b))

'''you have to call pi/2 from np'''

a = np.array([0,1,np.pi/2])

# print(a)

'''ypu have to define sin but its already defined in np
its provided you wiered number for np.pi'''

np.sin(a)
# print(np.sin(a))

'''its provide you exponential value which is e = 2.717...'''
np.exp(a)
# print(np.exp(a))

'''sqrt is square root defined in np'''
np.sqrt(a)
# print(np.sqrt(a))
# =============================================================================
# 
# =============================================================================
'''sorting
have 3 argument in which 1 positional arg and 1 keyward arg and 1 optional keyward argument'''


a= np.array([[123,656,78],[656,698,417],[354,656,664],[10,9,13],[13,14,9],[16,17,18]])

#sorted coloumn wise
np.sort(a,axis=0)
# print(np.sort(a,axis =0))

'''result ll provided you a new array which have lowest to highes column number'''

#sorted row wise 
np.sort(a,axis=1)
# print(np.sort(a,axis=1))

# sort none  it ll print as a single list 
np.sort(a,axis=None)
# print(np.sort(a, axis = None))

'''sorting '''

'''s3 means string with len 3 means i ll print only 3 letter of a string  
you man see 231 is integer feeded istead of string but as its place on name position which dtype is string
so python ll take it as string and provided you a name of 231 as string not integer '''


newType = [('name', 'S3'), ('grad_year', int), ('cgpa', float)]
myList = [('Alpha', 2019, 8.5), (231, 2018, 8.7), ('Gamma', 2018, 7.9), ('Delta', 2019, 9.0)]
arr = np.array(myList, dtype = newType)

# arr = np.array(myList) # its provide you simple matrix
# print(arr)

np.sort(arr,order='cgpa')
# print(np.sort(arr,order='cgpa'))

