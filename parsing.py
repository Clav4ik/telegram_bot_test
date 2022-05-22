
from bs4 import BeautifulSoup
import urllib.request
from requests_html import HTMLSession
import time

def check_time(mes_time: int) -> bool:
    with open("time.txt", "r", encoding='utf-8') as file:
        time_late = file.read()

    check_hour = time.strftime('%H:%M:%S', time.gmtime(mes_time - int(time_late))).split(':')[0]
    if check_hour == "00":
        return True
    else:
        with open("time.txt", "w", encoding='utf-8') as file:
            file.write(str(mes_time))
        return False

def get_local_photo(animal: str) -> list:
    list_url_images = []
    for i in range(1, 4):
        with open(f"local-funny-{animal}{i}.jpg", "rb") as file:
            list_url_images.append(file.read())
    return list_url_images

class Parser:

    def get_images(self, key_word: str)-> list:

        url, animal = '',''
        if key_word=='Funny Cats':
            url = 'https://www.google.com/search?q=%D0%BC%D0%B8%D0%BB%D1%8B%D0%B5+%D0%BA%D0%BE%D1%88%D0%BA%D0%BE+%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&rlz=' \
                  '1C1GGRV_enUA771UA771&sxsrf=ALiCzsbTW0RAw-5B0qbVdeapECdenY3tZg:1652809723781&source=lnms&tbm=' \
                  'isch&sa=X&ved=2ahUKEwjelt6DjOf3AhVs-SoKHXv7DzMQ_AUoAXoECAEQAw&biw=619&bih=937&dpr=1'
            animal = 'cat'
        elif key_word=='Funny Dogs':
            url = 'https://www.google.com/search?q=%D0%BC%D0%B8%D0%BB%D1%8B%D0%B5+%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B8&rlz=' \
                  '1C1GGRV_enUA771UA771&sxsrf=ALiCzsYKaWggQ-u5JkMdMhJ52fWLvbMmzg:1653215593526&source=lnms&tbm=isch&sa=' \
                  'X&ved=2ahUKEwjSx8GB9PL3AhXos4sKHZITDzUQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1'
            animal = 'dog'
        session = HTMLSession()
        response = session.get(url)

        if response.status_code != 200:
            return get_local_photo(animal)


        pars_html = BeautifulSoup(response.content, "html.parser")
        a_tag = pars_html.find('div', 'FAZ4xe FoDaAb').find_all('div', 'tzVsfd PKhmud sc-it')

        num = 1
        list_url_images = []
        for i in a_tag:
            step = i.find('img', 'rHLoR')
            if step == None:
                continue
            if step.get('data-src'):
                urllib.request.urlretrieve(str(step.get('data-src')), f"local-funny-{animal}{num}.jpg")
                with open(f"local-funny-{animal}{num}.jpg", "rb") as file:
                    list_url_images.append(file.read())

                if num == 4:
                    break
                num+=1
        return  list_url_images
#main container google search
# <-----parsing------>
#
# a_tag = pars_html.find('div', 'mJxzWe').find_all('div', 'bRMDJf islir')
# #print(a_tag)
#
# #print(a_tag)
# num = 1
# for i in a_tag:
#     #print(i)
#     step = i.find('img', 'rg_i Q4LuWd')
#     print(step)
    # if step.get('data-src'):
    #
    #     print(step.get('data-src'))
    #     urllib.request.urlretrieve(str(step.get('data-src')), f"local-filename{num}.jpg")
    #     num+=1



