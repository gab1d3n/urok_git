import time

def create_file(file_number):
    time.sleep(1)  
    with open(f'file_{file_number}.txt', 'w') as f:
        f.write(f'Это файл номер {file_number}')

start_time = time.time()

for i in range(100):
    create_file(i)

end_time = time.time()
print(f"Время выполнения в одном потоке: {end_time - start_time} секунд")
