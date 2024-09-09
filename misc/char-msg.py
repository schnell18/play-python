import requests
from bs4 import BeautifulSoup


def decode(url):
    resp = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(resp.text, "html.parser")
    recs = []
    for r in soup.select("#contents .doc-content table tr"):
        x = [e.text for e in r.select("tr td p span")]
        recs.append(x)

    map = {}
    max_x, max_y = -1, -1
    for rec in recs[1:]:
        x = int(rec[0])
        y = int(rec[2])
        map[f"{x}-{y}"] = rec[1]
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            c = map.get(f"{x}-{y}", " ")
            print(c, end="")
        print("")


def main():
    request_url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"  # noqa
    decode(request_url)


if __name__ == "__main__":
    main()
