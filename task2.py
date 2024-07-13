import time
import threading

def create_file(file_number):
    time.sleep(1)  
    with open(f'file_{file_number}.txt', 'w') as f:
        f.write(f'Это файл номер {file_number}')

start_time = time.time()

threads = []
for i in range(100):
    thread = threading.Thread(target=create_file, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Время {end_time - start_time} секунд")
