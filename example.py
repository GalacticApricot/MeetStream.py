from meetstream import MeetstreamAPI

# Initialize with your API key
api = MeetstreamAPI(api_key="your_api_key_here")

# Create a bot
bot_data = api.create_bot(
    meeting_link="https://meet.google.com/your-meeting-id",
    bot_name="My Meeting Bot",
    bot_message="Hello everyone!"
)

# Get bot status
status = api.get_bot_status(bot_data["bot_id"])
