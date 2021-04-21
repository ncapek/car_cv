from urllib.request import urlopen
from PIL import Image
from pandas import DataFrame
import requests
from bs4 import BeautifulSoup
from more_itertools import unique_everseen


def get_car_pages(page_num):
    url = f'https://www.aaaauto.cz/cz/cars.php?carlist=1&page={str(page_num)}&modern-request&origListURL=%2Fojete-vozy%2F'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    car_urls = list(unique_everseen([el['href'] for el in soup.find_all("a", {"class": "fullSizeLink"})]))
    return car_urls

def get_car_image_urls(res, limit=1):
    soup = BeautifulSoup(res.text, 'html.parser')
    pics = list(unique_everseen([el['src'] for el in soup.find_all("img", {"class": "pswp__photo"})]))
    return pics[:limit]

def get_car_color(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    car_specs = soup.find("table", attrs={"class": "transparentTable"})

    if car_specs:
        tr_res = car_specs.find_all("tr")
        if tr_res:
            for tr in tr_res:
                if tr.th.text == 'Barva':
                    return tr.td.text
    return None

def save_pic(url, filename, res=(256,192)):
    img = Image.open(urlopen(url)).resize(res)
    img.save(filename, "png")
    #img.show()
    img.close()

def main():
    pic_id = 0
    colors = []
    for page_number in range(1, 900):
        print(f'page_numbers: {page_number}\n')
        for car_page in get_car_pages(page_number):
            res = requests.get(car_page)
            color = get_car_color(res)
            if color:
                try:
                    color_id = colors.index(color)
                except:
                    colors.append(color)
                    color_id = colors.index(color)
                for car_image_url in get_car_image_urls(res):
                    save_pic(car_image_url, f'color_classification/assets/{pic_id}_{color_id}.png')
                    pic_id += 1
            print(colors)

        with open('color_classification/colors_dump.txt', 'w', encoding='UTF-8') as writer:
            writer.write(str(colors))


if __name__ == "__main__":
    main()
