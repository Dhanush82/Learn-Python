import threading

def worker(num):
    print(f"Worker {num} started")

thread1 = threading.Thread(target=worker, args=(1,))
thread2 = threading.Thread(target=worker, args=(2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads have finished")
