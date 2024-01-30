#!/usr/bin/env python3

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime

USER_TOKEN = os.environ.get(
    "SLACK_USER_TOKEN",
    "xoxp-***",
)

def list_channels_and_last_message_date(token):
    try:
        client = WebClient(token=token)
        response = client.conversations_list()
        channels = response["channels"]

        for channel in channels:
            channel_id = channel["id"]
            history_response = client.conversations_history(channel=channel_id, limit=1)

            if history_response["messages"]:
                last_message = history_response["messages"][0]
                type = last_message["type"]
                subtype = last_message["subtype"] if "subtype" in last_message else ""
                last_message_date = last_message["ts"]
                print(
                    f"#{channel['name']},{datetime.datetime.fromtimestamp(float(last_message_date))},{type},{subtype}"
                )
            else:
                print(f"Channel: {channel['name']}, No messages in the channel")

    except SlackApiError as e:
        print(f"Error fetching channels: {e.response['error']}")


if __name__ == "__main__":
    list_channels_and_last_message_date(USER_TOKEN)
