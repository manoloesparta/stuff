from bs4 import BeautifulSoup

with open("fbpages.html", "r") as pages:
    soup = BeautifulSoup(pages, 'html.parser')

links = soup.find_all('a')

cleaned = []
for link in links:
    if '?__tn__=%3C' in link.get('href'):
        continue
    if 'l.php?' in link.get('href'):
        continue
    if 'mailto' in link.get('href'):
        continue
    if '/support/?surface' in link.get('href'):
        continue
    if 'developers.facebook' in link.get('href'):
        continue
    if 'shop/?ref_code' in link.get('href'):
        continue
    cleaned.append(link.get('href'))

with open('pages', 'w+') as whatever:
    whatever.write("\n".join(cleaned[16:]))
