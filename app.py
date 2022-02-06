import time
import threading
import concurrent.futures

def do(seconds):
    print(f'sleep {seconds} seconds')
    time.sleep(seconds)
    return f'{threading.current_thread().name} done sleeping {seconds} seconds'

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    times = [5, 4, 3, 2, 1]
    results = executor.map(do, times)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'\nfinished in {round(finish-start, 2)} seconds')
