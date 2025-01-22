# searchurls
Just a list of URLs for searching and maybe some scripts using them
Replace '%s' with the search string, usually with pluses instead of spaces

## Example commands to create search string
`search="epic bingus"`
`printf "https://www.google.com/search?q=%s" $(echo $search | sed 's/ /+/g')`


## List of URLs

### Google
`https://www.google.com/search?q=%s`


### Google Maps
`https://www.google.com/maps/search/%s?hl=fr&source=opensearch`


### DuckDuckGo
`https://duckduckgo.com/?q=%s`


### Youtube 
`https://www.youtube.com/results?search_query=%s`


### Youtube Music
`https://music.youtube.com/search?q=%s`


### Twitch
`https://www.twitch.tv/search?term=%s`


### Reddit
`https://www.reddit.com/search/?q=%s`


### Reddit (through Google)
`https://www.google.com/search?q=%s+site%3Areddit.com`
`https://www.google.com/search?q=site%3Areddit.com+%s`


### Reddit (through DuckDuckGo)
`https://duckduckgo.com/?q=site%3Areddit.com+%s`
 

### Wikipedia 
`https://en.wikipedia.org/w/index.php?search=%s` 
 

### Steam
`https://store.steampowered.com/search/?term=%s`


### GOG
`https://www.gog.com/en/games?query=%s`


### Github
`https://github.com/search?q=%s`


### Archive.org
`https://archive.org/search?query=%s`


### Wayback Machine vague
`https://web.archive.org/web/*/%s`


### Wayback Machine specific
`https://web.archive.org/web/yyyymmddhhmmss/url/`
Example: `https://web.archive.org/web/20250119022516/https://cleartest.com/`
To get the date, use `date +%Y%m%d%H%M%S` on Linux/Unix


### Shodan
`https://www.shodan.io/search?query=%s`


### Manned (man pages)
`https://manned.org/browse/search?q=%s`


### Scryfall
`https://scryfall.com/search?q=%s`


### Java Docs (the 22 can be replaced with the version number)
`https://docs.oracle.com/en/java/javase/22/docs/api/search.html?q=%s`


### Trakt
`https://trakt.tv/search?query=%s`


### IMDB
`https://www.imdb.com/find/?q=%s`


### Rate Your Music
`https://rateyourmusic.com/search?searchterm=%s`


### Album of the Year
`https://www.albumoftheyear.org/search/?q=%s`


### MusicBrainz
`https://musicbrainz.org/search?query=%s`


