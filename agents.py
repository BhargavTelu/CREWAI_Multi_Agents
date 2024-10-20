from crewai import Agent, LLM
from litellm import OpenAIEmbedding
from tools import yt_tool
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain.chat_models import ChatOpenAI
import openai
from dotenv import load_dotenv
load_dotenv()
# LLM = ChatGroq( api_key = os.getenv('GROQ_API_KEY'),model_name = "llama3-8b-8192")
# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
# os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo-0125"

# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))


llm=ChatOpenAI(model="gpt-3.5",api_key=os.getenv("OPENAI_API_KEY"))

# create a senior blog youtube videos researcher

youtube_researcher =Agent(
    role='Senior youtube videos researcher',
    goal='get the relevant video content for thr topic {topic} from yt channel',
    backstory="""expert in understanding videos in AI, Machine Learning and Data science""",
    verbose=True,
    memory = True,
    allow_delegation=True,
    llm = llm,
    tools=[yt_tool]
)

#create a senior blog writer with yt tool

blog_writer=Agent(
    role='Senior blog writer',
    goal='write a blog about {topic} from the video content',
    backstory="""expert in writing blogs about AI, Machine Learning and Data science""",
    verbose=True,
    memory=True,
    allow_delegation=False,
    tools=[yt_tool],
    llm=llm,
)
