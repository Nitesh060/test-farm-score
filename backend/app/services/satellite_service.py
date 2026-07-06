class SatelliteService:
    """Wraps calls to satellite APIs (NASA POWER, Sentinel Hub, GEE)."""

    def fetch_ndvi(self, lat: float, lon: float, date_range: tuple):
        raise NotImplementedError
