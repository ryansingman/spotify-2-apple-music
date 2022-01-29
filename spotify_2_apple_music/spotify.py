from typing import Any, Callable, Dict, Iterable, List

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from . import constants
from .types import Track


def get_saved_tracks() -> List[Track]:
    """Gets list of saved tracks using Spotify API.

    Returns
    -------
    List[Track]
        list of users saved tracks
    """
    spotify = _get_spotify_session()
    return [
        Track.from_spotify_track_dict(track_dict["track"])
        for track_dict in _paginated_iter(spotify.current_user_saved_tracks)
    ]


def _paginated_iter(iter_callable: Callable[[int, int], Dict[str, Any]], limit: int = 20) -> Iterable[Dict[str, Any]]:
    """Paginated iterator for spotiy paginated return.

    Parameters
    ----------
    iter_callable : Callable[[int, int], Dict[str, Any]]
        paginated iterable callable to iterate over
    limit : int
        limit of results to send in single API call, by default 20

    Yields
    -------
    Generator[Dict[str, Any], None, None]
        yields items for iterable callable
    """
    # init offset and loop condition
    offset: int = 0
    is_next: bool = True

    while is_next:
        paginated_dict = iter_callable(limit=limit, offset=offset)
        for item in paginated_dict["items"]:
            yield item

        is_next = paginated_dict["next"]
        offset += limit


def _get_spotify_session(scope: str = "user-library-read") -> spotipy.Spotify:
    """Gets spotify session.

    Parameters
    ----------
    scope : str
        scope of session, by default "user-library-read"

    Returns
    -------
    spotipy.Spotify
        spotify session
    """
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=constants.SPOTIPY_CLIENT_ID,
        client_secret=constants.SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://localhost:8080",
        scope=scope,
    ))
    