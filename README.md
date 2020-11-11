# Awsume Default Profile Plugin

_Awsume 4 only._

This is a plugin that let's you specify a different default profile to use when invoking `awsume` without a specified profile name.

## Installation

Clone this repo and run `pip install .`

## Configuration

Override the default profile name selected when no `profile_name` positional argument is specifed in the call to `awsume`. The plugin will use the following values:

1. The value of `AWSUME_DEFAULT_PROFILE` environment variable if set, or

2. The value of the `default-profile` key in `~/.awsume/config.yaml` if set, or

3. The value `"default"`.

If a `profile_name` argument is supplied, that will override this setting.

## Usage

I'm using [direnv](https://direnv.net/) to set the `AWSUME_DEFAULT_PROFILE` for specific directories so I can just use `awsume` without having to specific a specific profile each time (auto-complete just feels a little too slow for me).
