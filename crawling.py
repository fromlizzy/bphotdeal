from bs4 import BeautifulSoup
import requests

response = requests.get("http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu")
soup = BeautifulSoup(response.text, "html.parser")

print(soup)

for item in soup.find_all("tr", {'class':["list1", "list0"]}):
    try:
        image = item.find("img", class_="thumb_border").get("src")[2:]
        title = item.find("font", class_="list_title").text
        title = title.strip()
        link = item.find("font", class_="list_title").parent.get("href")
        link = "http://www.ppomppu.co.kr/zboard/" + link
        reply_count = item.find("span", class_="list_comment2").text
        reply_count = int(reply_count)
        up_count = item.find_all("td")[-2].text
        up_count = up_count.split("-")[0]
        up_count = int(up_count)
        if up_count >= 5:
            print(image, title, link, reply_count, up_count)
    except Exception as e:
        # print(e)
        continue