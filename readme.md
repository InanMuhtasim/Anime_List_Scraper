# Anime List Scraper

A simple scrapy spider to get the list of Anime from a MyAnimeList profile.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [About](#about)

## Project Description

With this project, It is possible to get a myanimelist.com user's "Currently Watching"/"Completed"/"On Hold"/"Dropped"/"Plan to watch"/"All" anime list and the status information of the animes.
There is no use of middlewares.py and pipelines.py in this project. Other than the spider only the items.py was modified from the default scrapy project.

## Installation

You will need scrapy to run this Programme

```
pip install scrapy
```

You can run the spider: (From Anime_list_Scraper directory)

```
scrapy crawl mal_spider
```

## Usage

- Track a friend's or someone's MyAnimeList updates
- Don't need to always open AyAnimeList to see your Anime list
- Get the status information of someone's anime

## About

This project is mainly my personal project. I made it to practice my web scraping skill and also.
