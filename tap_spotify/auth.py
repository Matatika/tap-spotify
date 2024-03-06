"""Spotify Authentication."""

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta
from typing_extensions import Self, override


class SpotifyAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for Spotify."""

    @property
    @override
    def oauth_request_body(self):
        return {
            "grant_type": "refresh_token",
            "refresh_token": self.config["refresh_token"],
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
        }

    @classmethod
    def create_for_stream(cls, stream) -> Self:
        """Create authenticator instance for a stream."""
        return cls(
            stream=stream,
            auth_endpoint="https://accounts.spotify.com/api/token",
        )
