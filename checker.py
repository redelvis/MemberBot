# _*_coding: utf-8 _*_

"""
Checker takes movie_name from PostgreSQL and checks tracker or a site with release-feed about a movies every 24 hours.
Checking realised with Cron. If there's a new release, it saves a link to a related column on PostgreSQL DB and
gives a ready-signal to a main.py
Here's also described a filters to avoid fake-releases and trailers (keywords like trailer, DVDscreener, Еelesynch,
small file_size and so on)
"""

