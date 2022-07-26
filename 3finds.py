import csv 
 
h=["0" for i in range(6)] 
print(h)
with open("1.csv") as f: 
  data=csv.reader(f) 
  print(data)
  data=list(data) 
  print(data)
  
  for i in data: 
    if i[-1]=="Yes": 
      for j in range(6): 
        if h[j]=='0': 
           h[j]=i[j] 
        elif h[j]!=i[j]: 
           h[j]='?' 
      print(h) 