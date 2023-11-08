from math import ceil


class PhotoAlbum:
    photos_on_page = 4
    dashes_per_line = 11

    def __init__(self, pages: int):
        self.pages = pages

        self.photos = [[] for _ in range(pages)]
        self.page_number = 0
        self.count = 0
        self.is_full = False

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.photos_on_page)
        return cls(pages)

    def add_photo(self, label: str):
        if self.is_full:
            return "No more free slots"
        self.photos[self.page_number].append(label)
        result = f"{label} photo added successfully on page " \
                 f"{self.page_number + 1} " \
                 f"slot {self.count % PhotoAlbum.photos_on_page + 1}"
        self.count += 1
        if self.count % PhotoAlbum.photos_on_page == 0:
            if self.page_number + 1 == self.pages:
                self.is_full = True
            else:
                self.page_number += 1
        return result

    def display(self):
        draw_line = '-' * PhotoAlbum.dashes_per_line
        result = [draw_line]

        for i in range(self.pages):
            s = ['[]' for j in range(len(self.photos[i]))]
            result.append(' '.join(s))
            result.append(draw_line)
        return '\n'.join(result)
