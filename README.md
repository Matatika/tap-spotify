# tap-spotify

`tap-spotify` is a Singer tap for Spotify.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

```bash
pipx install tap-spotify
```

## Configuration

### Accepted Config Options

- [ ] `Developer TODO:` Provide a list of config options accepted by the tap.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-spotify --about
```

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

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
