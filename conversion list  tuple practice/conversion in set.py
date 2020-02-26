lst1=[1,2,3,2,4,'a','ab','ab','ab',3,2]  #list is convertwd into set
convset=set(lst1)
print(convset)

tup1=(1,2,3,4,5,1,2,3,'a','ab','a')    # also tuuple is converted into in set

convset=set(tup1)
print(convset)

set1={1, 2, 3, 4, 5, 'ab', 'a'}      #set is convert into list
lst1=list(set1)
print(lst1)


set1={1, 2, 3, 4, 5, 'ab', 'a'}     #set is convert into tuple
tup1=tuple(set1)
print(tup1)

lst1=[1,2,3,2,4,'a','ab','ab','ab',3,2]   #list is converted into tuple
tup1=tuple(lst1)
print(tup1)

lst1=tuple([1,2,2])
lst2=tuple([1,2,2])
lst3=tuple([1,3,2])
lst4=tuple([1,3,2])                     #dupcheck
dupcheck={lst1,lst2,lst3,lst4}
print (dupcheck)