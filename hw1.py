import random
import time
import threading

def write_random_number(file_index):
    filename = f'random_number_{file_index}.txt'
    with open(filename, 'w') as f:
        random_number = random.randint(1, 100)
        f.write(str(random_number))
    time.sleep(1)

start_time = time.time()

for i in range(1000):
    write_random_number(i)

end_time = time.time()
print(f"Время выполнения без потоков: {end_time - start_time} секунд")

def threaded_execution():
    threads = []
    for i in range(1000):
        thread = threading.Thread(target=write_random_number, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

start_time = time.time()
threaded_execution()
end_time = time.time()

print(f"Время выполнения с потоками: {end_time - start_time} секунд")
