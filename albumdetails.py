import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_song_details(link):
    """
    Gathers the details of each song such as artist name and song name etc...
    :param link: Link to the soundcloud song
    :return: Dictionary including the song url, name, artist and artwork url
    """
    r = requests.get(link)
    song_url = r.url
    # artist_name, song_name = urlparse(song_url).path[1:].split("/") if urlparse(song_url).path[0] == "/" \
    #     else urlparse(song_url).path.split("/")
    if "soundcloud" in urlparse(song_url).netloc:
        song_domain = "soundcloud"
    else:
        song_domain = "youtube"
    song_artwork_url, song_name, song_artist = sc_scraper(r.content)

    return {
        "song_url": song_url,
        "song_artist": song_artist,
        "song_name": song_name,
        "song_artwork_url": song_artwork_url
    }


# def get_artwork(song_url, song_domain):
#     if song_domain == "soundcloud":
#         soundcloud_artwork(song_url)


#def soundcloud_artwork(song_url):


def sc_scraper(content):
    """
    Use Beautiful Soup to parse through the content of the doc and find relevant details
    :param content: The content of the request to the song url
    :return: artwork url, song name and song artist
    """
    soup = BeautifulSoup(content, "html.parser")
    images = soup.find_all("img", src=True)
    for image in images:
        if "i1.sndcdn" in image["src"]:
            song_artwork_url = image["src"]
            break
    song_name = soup.find("a", itemprop=True).get_text()
    song_artist = soup.find("a", itemprop=True).next_sibling.next_sibling.get_text()
    return song_artwork_url, song_name, song_artist


details = get_song_details("https://soundcloud.com/fareoh/withoutyou")
print(details)
