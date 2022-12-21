'''
### Zip function( How to access in user id and suppose it combind user to names)

# user_id  = ('user1','user2','user3','user4')
# user_id  = ('user1','user2','user3') ## if user less than names than it read 
# #and print those user what is existed in user_id
# names = ('Ishak','Irfan','Anas','Ayisha')
# print(list(zip(user_id,names)))'

user_info = [('a',1),('b',2)]
print(dict(user_info))

## With two name list combined
user_id  = ('user1','user2','user3','user4')
name1 = ('Ishak','Irfan','Anas','Ayisha')
name2 =('Ahmed','Ahmed','Ahmed','Akther')

print(list(zip(user_id,name1,name2)))

### zip with *

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l = [(1,2),(5,6),(9,10)] ## if two value in just one list like (1,2) it will convert smaller list
print(list(zip(*l)))

l1,l2 = (list(zip(*l))) ## here l list value enter in l1,l2 and convert only two list
print(l1)
print(l2)

'''

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

new_list = []

for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list) ## here will print maixmum value list like [6,7,8,9,10]


