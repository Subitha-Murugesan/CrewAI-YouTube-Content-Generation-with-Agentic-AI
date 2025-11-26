from crewai_tools import YoutubeChannelSearchTool

from dotenv import load_dotenv
load_dotenv()
##create a senor blog content researcher agent
#people who will be doing the task

# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_url="https://www.youtube.com/@freecodecamp"
)
