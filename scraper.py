import requests
from bs4 import BeautifulSoup

# scrap = requests.get("http://ogungovt.plexada-si-apps.com/projects/implementation")

soup = BeautifulSoup(
    requests.get("https://distrowatch.com/").content,
    "html.parser")

top_ten_distros = []
distro_tds = soup("td", class_="phr2", limit=10)
for td in distro_tds:
    top_ten_distros.append(td.find("a").contents[0])


print(top_ten_distros)