import os
import time
import api_functions
from slackclient import SlackClient

# dogeBot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("dogeBot connected and running!")
        while True:
            command, channel = api_functions.parse_slack_output(
                                slack_client.rtm_read()
                                , AT_BOT
                                )
            if command and channel:
                api_functions.handle_command(
                    command
                    , channel
                    , EXAMPLE_COMMAND
                    , slack_client
                )
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
