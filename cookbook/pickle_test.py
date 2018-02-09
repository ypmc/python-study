import pickle

data = {'foo': [1, 2, 3], 'bar': ('Hello', 'world!'), 'baz': True}
jar = open('data.pkl', 'wb')
pickle.dump(data, jar)  # 将pickle后的数据写入jar文件
jar.close()

pkl_file = open('data.pkl', 'rb')  # 与pickle后的数据连接
data = pickle.load(pkl_file)  # 把它加载进一个变量
print(data)
pkl_file.close()
