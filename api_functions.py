"""
    Functions for interfacing with the Slack api.
"""
import text_functions
def handle_command(command, channel, EXAMPLE_COMMAND, slack_client):
    """
        Processes commands according to doge's top-level text_functions.process_text function. 
        Currently, Doge just repeats back anything you say at him.
    """
    response = text_functions.process_text(command)
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output
                      , AT_BOT):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None
