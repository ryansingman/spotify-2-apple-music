"""Gets spotify saved tracks and adds them to Apple Music playlist."""
from typing import List

from . import spotify
from .types import Track

if __name__ == "__main__":

    saved_tracks: List[Track] = spotify.get_saved_tracks()
