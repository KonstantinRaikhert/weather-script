import json
import urllib.request
from dataclasses import dataclass
from json.decoder import JSONDecodeError
from urllib.error import URLError

import config
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using ipinfo.io"""
    try:
        response = _get_ipinfo_response()
        ipinfo_dict = _parse_ipinfo_response(response)
        coordinates = _parse_coordinates(ipinfo_dict)
        return coordinates
    except KeyError as key_error:
        raise CantGetCoordinates(f"KeyError - {key_error}")


def _get_ipinfo_response() -> str:
    url = config.IP_INFO_URL
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise CantGetCoordinates


def _parse_ipinfo_response(ipinfo_response: str) -> dict:
    try:
        ipinfo_dict = json.loads(ipinfo_response)
    except JSONDecodeError:
        raise CantGetCoordinates
    return ipinfo_dict


def _parse_coordinates(ipinfo_dict: dict) -> Coordinates:
    try:
        latitude, longitude = map(float, ipinfo_dict["loc"].split(","))
    except (IndexError, KeyError):
        raise CantGetCoordinates
    if config.USE_ROUNDED_COORDS:
        latitude, longitude = map(
            lambda c: round(c, 1),
            [latitude, longitude],
        )
    return Coordinates(longitude=longitude, latitude=latitude)


if __name__ == "__main__":
    print(get_gps_coordinates())
