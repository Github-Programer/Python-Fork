from time import sleep
from threading import Thread

#小明要下载10个视频
tasks = ['movie1', 'movie2', 'movie3','movie4','movie5','movie6','movie7','movie8','movie9', 'movie10']

def download(movie):
	print(f'start downloading {movie}')
	sleep(1) #模拟下载电影需要的时间
	print(f'finished download {movie}')

threads = []
for task in tasks:
	t = Thread(target=download, args=(task,)) #创建线程
	t.start() #启动线程
	threads.append(t)

for t in threads:
	t.join() #当前线程等待线程t执行完成后再执行后面的代码

#都下载完成后，能够打印一句话
print("都下载完了!")