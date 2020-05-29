### -------------------------------------------------------------------------------------------------------------------
### ddos puzzlehunt websites
### -------------------------------------------------------------------------------------------------------------------

import requests
from concurrent.futures import ThreadPoolExecutor

def get_url(i):
    url = "https://sites.google.com/view/the-food-pyramid-dessert-" + str(i) + "/"
    b = "puzzle" in requests.get(url).text
    if b:
        print('success!!!')
        print(b)
        print(url)
        assert(0)
    elif i % 100 == 0:
        print(i)
    return (url, b)

for i in range(1000):
    with ThreadPoolExecutor(max_workers=100) as pool:
        list(pool.map(get_url,range(4000+100*i,4000+100*(i+1))))