from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import requests
import telegram
from bestitem.models import Deal


headers = {'User-Agent':'Mozilla/5.0'}
url = 'https://bebedepino.com/category/on-sale/120/'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

BOT_TOKEN = "1778976525:AAE1YoJxdTMqGGoJl5gllNHow_60EQnNexE"
bot = telegram.Bot(token=BOT_TOKEN)

def run():

    for item in soup.find_all("li", {'class':["xans-record-", "aos-init"]}):
        try:
            thumb_img = item.find("img", class_="listImage").get("src")[2:]
            thumb_img = "http://" + thumb_img
            title = item.find("div", class_="name").text
            title = title.strip()
            link = item.find("img", class_="listImage").parent.get("href")
            link = "http://bebedepino.com" + link
            price = item.find("li", class_="xans-record-").parent.text
            wish_cart = item.find("img", class_="ec-product-listwishicon").get("icon_status")
            discount = item.find("div", class_="discountBox").text
            discount = ''.join(filter(str.isalnum, discount))
            discount = int(discount)
            if discount >= 30:
                if (Deal.objects.filter(link__iexact=link).count() == 0):
                    Deal(thumb_url=thumb_img, title=title, link=link, price=price, discount=discount).save()
                    bot.sendMessage(-1001583868305, '{} {}'.format(title, link))
        except Exception as e:
            continue
