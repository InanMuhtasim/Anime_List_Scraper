import scrapy
import json
from ..items import AnimeItem


class MalSpiderSpider(scrapy.Spider):
    name = "mal_spider"

    # Save the deta in json format
    custom_settings = {
        "FEEDS": {
            "anime_list.json": {
                "format": "json",
                "overwrite": True,
            },
        },
    }

    ANIME_SERIAL_NUMBER = 0

    # Can be modified for users need
    MAL_USER_NAME = "Inan_kun"
    STATUS = "1"
    """
    Statues-> 
    1 - Currently Watching
    2 - Completed
    3 - On Hold
    4 - Dropped
    6 - Plan to Watch
    7 - All Anime
    
    """

    start_urls = [
        f"https://myanimelist.net/animelist/{MAL_USER_NAME}/load.json?offset={ANIME_SERIAL_NUMBER}&status={STATUS}"
    ]

    def parse(self, response):
        animes_dict = json.loads(response.text)

        if response.text != "[]":
            for n, anime_info in enumerate(animes_dict):
                anime_name_eng = anime_info["anime_title_eng"]
                anime_name = (
                    anime_name_eng
                    if anime_name_eng != ""
                    else anime_info["anime_title"]
                )
                anime_url = anime_info["anime_url"]

                anime = AnimeItem()

                anime["Serial"] = MalSpiderSpider.ANIME_SERIAL_NUMBER + n + 1
                anime["Name"] = anime_name
                anime["Full_Info"] = anime_info

                yield response.follow(
                    f"https://myanimelist.net{anime_url}",
                    callback=self.rating_parse,
                )
                yield anime

            # If there is more than 300 items it is needed because at a time only 300 items are received
            MalSpiderSpider.ANIME_SERIAL_NUMBER += 300
            yield response.follow(
                f"https://myanimelist.net/animelist/{MalSpiderSpider.MAL_USER_NAME}/load.json?offset={MalSpiderSpider.ANIME_SERIAL_NUMBER}&status={MalSpiderSpider.STATUS}",
                callback=self.parse,
            )

    def rating_parse(self, response):
        name = response.css(".title-name strong::text").get()
        rating = response.css(".score-label::text").get()
        url = response.url

        print(f"Name: {name} | Rating: {rating}\nlink: {url}\n")
