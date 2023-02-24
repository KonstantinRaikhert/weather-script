class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates"""


class ApiServiceError(Exception):
    """Program can't get API OpenWeather"""


class PathServiceError(Exception):
    """Program can't write file in directory"""
