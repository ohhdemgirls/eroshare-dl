#!/usr/bin/env python3

import click
import requests
from bs4 import BeautifulSoup

@click.command()
@click.argument("url")
def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    video_urls = [source.attrs["src"] for source in soup.find_all("source", attrs={"data-quality": "HD"})]
    for url in video_urls:
        print(url)


if __name__ == "__main__":
    main()
