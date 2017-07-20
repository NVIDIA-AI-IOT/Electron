# Running the slackbot
'''
cd Electron/slackbot
virtualenv slackbot
pip install slackclient
source slackbot/bin/activate
export SLACK_BOT_TOKEN='tokenfromslack'
python print_bot_id.py
export BOT_ID='bot id from print_bot_id.py'
python deliverybot.py
'''
