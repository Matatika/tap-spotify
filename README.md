# tap-spotify

`tap-spotify` is a Singer tap for Spotify.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
# pip
pip install git+https://github.com/Matatika/tap-spotify

# pipx
pipx install git+https://github.com/Matatika/tap-spotify

# poetry
poetry add git+https://github.com/Matatika/tap-spotify
```

## Configuration

### Accepted Config Options

Name | Description
--- | ---
`client_id` | Your `tap-spotify` app client ID
`client_secret` | Your `tap-spotify` app client secret
`refresh_token` | Your `tap-spotify` app refresh token
`access_token` | Your `tap-spotify` app access token

### Valid Configurations

Option(s) | Description
--- | ---
`access_token` | Use supplied access token
`client_id`<br>`client_secret`<br>`refresh_token` | Use OAuth credentials to generate access tokens internally
`client_id`<br>`client_secret`<br>`refresh_token`<br>`access_token` | Use supplied access token and fallback to OAuth credentials if invalid or expired

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-spotify --about
```

### Source Authentication and Authorization

Before using `tap-spotify`, you will need to create an [app](https://developer.spotify.com/documentation/web-api/concepts/apps) from your [Spotify developer dashboard](https://developer.spotify.com/dashboard). We recommend restricting your use of this app to `tap-spotify` only. Provide an name, description and a redirect URI of `https://alecchen.dev/spotify-refresh-token` (explained below).

#### Get an Access Token and/or Refresh Token
Use [this web app](https://alecchen.dev/spotify-refresh-token?scope=user-top-read&scope=user-library-read) made by [Alec Chen](https://alecchen.dev/) to get an access token and/or refresh token with your Spotify app credentials:
- Provide your app client ID and secret in the appropriate fields
- Click 'Submit' and follow the Spotify login flow
- Copy the access token and/or refresh token

Each stream requires certain token scopes. By default (all streams selected), the following token scopes are required:
- [`user-top-read`](https://developer.spotify.com/documentation/web-api/concepts/scopes#user-top-read)
- [`user-library-read`](https://developer.spotify.com/documentation/web-api/concepts/scopes#user-library-read)

When specific streams are selected, the required token scopes may change.

Stream | Required scope(s)
--- | ---
`user_top_tracks_st_stream` | `user-top-read`
`user_top_tracks_mt_stream` | `user-top-read`
`user_top_tracks_lt_stream` | `user-top-read`
`user_top_artists_st_stream` | `user-top-read`
`user_top_artists_mt_stream` | `user-top-read`
`user_top_artists_lt_stream` | `user-top-read`
`global_top_tracks_daily_stream` |
`global_top_tracks_weekly_stream` |
`global_viral_tracks_daily_stream` |
`user_saved_tracks_stream` | `user-library-read`

If a required scope is not set, `tap-spotify` will encounter a `403 Forbidden` response from the Spotify Web API and fail. You must set all required scopes for the selected streams.

Any other scopes not listed here are **not required** by `tap-spotify`. Setting these will allow applications using the same Spotify app credentials to read more specific and possibly sensitive resource data, so do this at your own risk.

## Usage

You can easily run `tap-spotify` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-spotify --version
tap-spotify --help
tap-spotify --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
make init
```

### Lint your Code

Identify lint issues by running:

```bash
make lint
```

> If `make init` has been run, this command will execute automatically before a commit

You can also fix lint issues automatically with:

```bash
make lint-fix
```

### Create and Run Tests

Create tests within the `tap_spotify/tests` subfolder and
  then run:

```bash
make test
```

You can also test the `tap-spotify` CLI interface directly using `poetry run`:

```bash
poetry run tap-spotify --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-spotify
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-spotify --version
# OR run a test `elt` pipeline:
meltano elt tap-spotify target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
