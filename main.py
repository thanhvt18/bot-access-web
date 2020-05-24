import requests
import time
import random
import os
from app.webfaker import driver


def choose_proxies():
    """choose proxy"""
    ran_num = random.randint(0, 123)
    proxy = ''
    file = open("./asset/proxies.json")
    for i, line in enumerate(file):
        if ran_num == i:
            proxy = line
            break
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    file.close()
    return proxies


def choose_header():
    """choose header"""
    # headers = {}
    # path_header = ''
    # ran_num = random.randint(1,2)
    # file


website = 'https://dogoquochiep.com/sap-ngu-phuc-s01/'

if __name__ == '__main__':

    proxies = choose_proxies()

    # session = requests.Session()
    # res = session.get(website, proxies=proxies, timeout=5, verify=False)
    # session.close()
    # print(res)

    driver.get(website)
    time.sleep(5)
    print(f'access {driver.current_url}')
    time.sleep(5)
    driver.execute_script("document.querySelector('#colophon').scrollIntoView({behavior: 'smooth' })")
    time.sleep(10)
    driver.close()