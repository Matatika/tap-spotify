"""Spotify Authentication."""

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


class SpotifyAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for Spotify."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the Spotify API."""
        return {
            "grant_type": "refresh_token",
            "refresh_token": self.config["refresh_token"],
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
        }

    @classmethod
    def create_for_stream(cls, stream) -> "SpotifyAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="https://accounts.spotify.com/api/token",
        )
