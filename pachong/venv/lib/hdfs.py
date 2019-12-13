import pyhdfs


fs = pyhdfs.HdfsClient(hosts='10.172.76.69:50070', user_name='root')
fs.list_status('/')
print(fs.listdir('/'))



#print(dir(fs))



#fs.mkdirs('/fruit/x/y')

#fs.mkdirs('/wangyuyan')


#fs.delete('/fruit/x')

#fs.create('/fruit/apple', 'delicious')

#fs.copy_from_local('123','/user/hadoop')
#fs.create('/fruit/', 'delicious')


#fs.copy_from_local('/Users/apple/Desktop/hadoop/1.txt','/user/hadoop')