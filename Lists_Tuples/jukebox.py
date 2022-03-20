from Nested_data import albums

SONG_TITLE_INDEX = 1

while True:
    print("please choose your album(invalid choice exits):")
    for index, (album,artist, year, song) in enumerate(albums):
        print("{}: {}"
              .format(index + 1,album))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][3]
    else:    
        break

    print("please choose your song:")
    for index, (track_number,song) in enumerate(songs_list):
        print("{} :{}".format(index + 1,song))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice- 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    print("=" * 40)
