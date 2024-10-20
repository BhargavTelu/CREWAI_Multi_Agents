from crewai import Task
from tools import yt_tool
from agents import youtube_researcher,blog_writer
from langchain.chat_models import ChatOpenAI
import openai
import os
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-3.5",api_key=os.getenv("OPENAI_API_KEY"))
#research task
youtube_search_task=Task(
    description="Identify the video of {topic} . get detail information about the video",
    expected_output="A detailed research report on the topic",
    tools=[yt_tool],
    agent=youtube_researcher,
    llm=llm
)

blog_writing_task=Task(
    description="get the info from the youtube channel on {topic}",
    expected_output="A detailed research report on {topic}",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="blog_post.md",
    llm=llm
)