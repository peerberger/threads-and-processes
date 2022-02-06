import threading
import time
import requests
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c'
]

start = time.perf_counter()

for img_url in img_urls:
# def download_image(img_url):
    threading.current_thread.__name__ = f'{img_url[-2:]}'
    print(threading.current_thread.__name__)
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download_image, img_urls)

finish = time.perf_counter()

print(f'\nfinished in {round(finish-start, 2)} seconds')
