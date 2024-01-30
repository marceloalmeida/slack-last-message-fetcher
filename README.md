# Slack last message fetcher
Fetch the last message timestamp of all slack public channels

## Usage
1. Install the application using the [app manifest](./assets/slack-app-manifest.yaml) on the Slack workspace
2. Export as environment variable the Oauth Token that can be fetched from the workspace installation
   1. Visit https://api.slack.com/apps
   2. Select the application by clicking in the name (e.g.: `Get public channels last message timestamp`)
   3. View token clicking in "Install app" (e.g. [https://api.slack.com/apps/<installation_id>/install-on-team](https://api.slack.com/apps/<installation_id>/install-on-team))
   4. `export SLACK_USER_TOKEN="xopx-***"`
3. Run application - `docker run -it --rm -e "SLACK_USER_TOKEN=$SLACK_USER_TOKEN" ghcr.io/marceloalmeida/slack-last-message-fetcher:latest`
