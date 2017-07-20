import os
import time
from slackclient import SlackClient
from nltk.tag import pos_tag

waiting_for_location = False
# bot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
    response = "Oh so you want a "
    tagged_sent = pos_tag(command.split())
    propernouns = [word for word,pos in tagged_sent if pos == 'NN']
    response+=str(propernouns[len(propernouns)-1])
    response+="! Is that correct?"
    if len(command.split()) < 2:
        if 'ye' in command:
            response = "Cool! What's your location?"
        else:
            response = "Sorry! I'm confused. Please tell me what you want again."

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Bot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
