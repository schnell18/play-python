import requests
import re
import sys

def get_pages(link):
    pattern = re.compile('https?')
    links_to_visit = []
    links_to_visit.append(link)
    while links_to_visit:
        current_link = links_to_visit.pop(0)
        page = requests.get(current_link)
        for url in re.findall('<a href="([^"]+)">', str(page.content)):
            if url[0] == '/':
                url = current_link + url[1:]
            if pattern.match(url):
                links_to_visit.append(url)
        yield current_link


if __name__ == '__main__':
    url = sys.argv[1]
    webpage = get_pages(url)
    for result in webpage:
        print(result)
