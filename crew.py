from crewai import Crew, Process
from agents import youtube_researcher,blog_writer
from tasks import youtube_search_task,blog_writing_task
from langchain.chat_models import ChatOpenAI
import openai
import os 
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-3.5",api_key=os.getenv("OPENAI_API_KEY"))
crew=Crew(
    agents=[youtube_researcher,blog_writer],
    tasks=[youtube_search_task,blog_writing_task],
    process=Process.sequential,
    cache=True,
    max_rpm=100,
    share_crew=True,
    llm=llm
)

#start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'Is generative Ai going to replace human?'})
print(result)