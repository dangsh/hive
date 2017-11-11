# import pandas

# #任意的多组列表
# a = [1,2,3]
# b = [4,5,6]    

# #字典中的key值即为csv中列名
# data =[{'a_name':a,'b_name':b}]
# dataframe = pandas.DataFrame(data)

# #将DataFrame存储为csv,index表示是否显示行名，default=True
# dataframe.to_csv("test.csv",index=False,sep='')

import csv
c=open("url.csv","w")
writer=csv.writer(c)
writer.writerow(['name','address','city','state'])

