import requests

url = "http://books.toscrape.com/"
response = requests.get(url)

# 把网页保存到本地
with open("web.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("网页已保存到 web.html")