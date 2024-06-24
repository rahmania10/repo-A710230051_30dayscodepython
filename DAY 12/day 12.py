def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} season(s)")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(tv_show)
