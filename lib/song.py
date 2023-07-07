class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.inc_count()
        self.add_artist_genre(artist, genre)
        self.update_genre_count(genre)
        self.artist_song_count(artist)

    @classmethod
    def inc_count(cls):
        cls.count += 1
    
    @classmethod
    def add_artist_genre(cls, new_artist, new_genre):
        cls.artists.append(new_artist)
        cls.genres.append(new_genre)

    @classmethod
    def update_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def artist_song_count(cls,artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
