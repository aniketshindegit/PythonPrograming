lst1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
posslc=lst1[0:5] # in positive slicing last digit does not consider
print(posslc)

slc2=lst1[0:14]
print(slc2)

slc3=lst1[0:14:1]  #print all num

print(slc3)
slc4=lst1[0:15:2]   #print if step is 2 then gap is one num
print(slc4)

slc5=lst1[0:9:3]  #if step is3 then gap between no is 2
print(slc5)