immutable_var = 5, 6,7,'кортеж'
print(immutable_var)
#immutable_var [0] =8
#print(immutable_var) # кортеж нельзя изменить если он несодержит изменяемых элементов.
mutable_list = ([5,6], 2,3,4 )
print(mutable_list)
mutable_list [0][0]= 7
print(mutable_list)