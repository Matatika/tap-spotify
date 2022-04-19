# tap-spotify

`tap-spotify` is a Singer tap for Spotify.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Note: Please check the [Releases](https://github.com/Matatika/tap-spotify/releases) page for a list of versions.

Installing a specific version (recommended for stability):

```bash
# Replace 'vX.Y.Z' in the below with the latest version number here:
#   https://github.com/Matatika/tap-spotify/releases
pipx install git+https://github.com/Matatika/tap-spotify.git@vX.Y.Z
```

Installing the latest repo version (recommended only for initial testing):

```bash
pipx install git+https://github.com/Matatika/tap-spotify.git@main
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-spotify --about
```

### Source Authentication and Authorization

You first will need to have a Spotify account and you will need to create a Spotify "App" though the Spotify Developer interface.

Once you have created a Spotify App, use Postman or the excellent [Thunderclient VS Code extension](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) to get an authorization token.

Create your Spotify App:

You can follow the Spotify Developers API instructions to create your spotify App. the only extra step you'll need to take is to add one or both of these to your allowed redirect URLs:

- `https://www.thunderclient.com/oauth/callback` (If using ThunderClient)
- `https://www.getpostman.com/oauth2/callback` (If using Postman)

From Thunderclient:

1. Click `New Request` to open a new Thunderclient tab.
2. Click `Auth` and then `OAuth2`.
3. In the `Generate New Token` section, complete the form using the following guide:
   - `Grant Type`: `Authorization Code` (the default)
   - `Auth URL`: `https://accounts.spotify.com/authorize`
   - `Token URL`: `https://accounts.spotify.com/api/token`
   - `Callback URL`: `https://www.thunderclient.com/oauth/callback` (the default)
   - `Client ID`: `<your app's client ID>`
   - `Client Secret`: `<your app's client secret>`
   - `Scope`: `playlist-read-private playlist-modify-private`
   - `State`: `(leave blank)` (the default)
   - `Send Auth`: `As Auth Header` (the default)
4. Click `Generate Token` to generate your token.
5. Store your newly generated token as the `refresh_token` value in tap config.

## Usage

You can easily run `tap-spotify` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-spotify --version
tap-spotify --help
tap-spotify --config CONFIG --discover > ./catalog.json
```

## Developer Resources

These resources are for repo contributors and developers.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_spotify/tests` subfolder and then run:

```bash
poetry run pytest
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
