from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, TypeVar


@dataclass
class Artist:
    name: str

    @classmethod
    def from_spotify_artist_dict(cls, artist_dict: Dict[str, Any]) -> Artist:
        """Creates artist dataclass from spotify artist dictionary.

        Parameters
        ----------
        artist_dict : Dict[str, Any]
            spotify artist dict to create artist dataclass with

        Returns
        -------
        Artist
            artist created from spotify dict
        """
        return cls(artist_dict["name"])


@dataclass
class Album:
    artists: List[Artist]
    name: str

    @classmethod
    def from_spotify_album_dict(cls, album_dict: Dict[str, Any]) -> Album:
        """Creates album dataclass from spotify album dictionary.

        Parameters
        ----------
        album_dict : Dict[str, Any]
            spotify album dict to create album dataclass with

        Returns
        -------
        Album
            album created from spotify dict
        """
        return cls(
            artists=[Artist.from_spotify_artist_dict(artist_dict) for artist_dict in album_dict["artists"]],
            name=album_dict["name"],
        )


@dataclass
class Track:
    artists: List[Artist]
    album: Album
    name: str
    track_no: int

    @classmethod
    def from_spotify_track_dict(cls, track_dict: Dict[str, Any]) -> Album:
        """Creates track dataclass from spotify track dictionary.

        Parameters
        ----------
        track_dict : Dict[str, Any]
            spotify track dict to create track dataclass with

        Returns
        -------
        Track
            track created from spotify dict
        """
        return cls(
            artists=[Artist.from_spotify_artist_dict(artist_dict) for artist_dict in track_dict["artists"]],
            album=Album.from_spotify_album_dict(track_dict["album"]),
            name=track_dict["name"],
            track_no=track_dict["track_number"],
        )
