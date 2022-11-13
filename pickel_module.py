import pickle
l=[10,20,30]
file = open("write.txt","wb")
pickle.dump(l,file)
file.close()

file = open("write.txt","rb")
x=pickle.load(file)
print(x)
file.close()

