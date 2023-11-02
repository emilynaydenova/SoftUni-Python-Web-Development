from project.song import Song
class Album:
    def __init__(self, name: str,  songs=None):  # songs is optional
        self.name = name
        if songs is None:
            self.songs = []
        elif isinstance(songs, list):
            self.songs = songs
        else:
            self.songs = []
            self.songs.append(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song in self.songs:
            return f'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        for ss in self.songs:
            if ss.name == song_name:
                self.songs.remove(ss)
                return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result
