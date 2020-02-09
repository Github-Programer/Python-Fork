from time import sleep
from threading import Thread

count = 0

def add():
	global count
	for i in range(10000):
		count += 1
		#print(count)

threads = []
for i in range(5):
	t = Thread(target=add)
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print(f"final: {count}")

