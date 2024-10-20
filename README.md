
# CrewAI

🤖 CrewAI: Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

## Why CrewAI?

The power of AI collaboration has too much to offer. CrewAI is designed to enable AI agents to assume roles, share goals, and operate in a cohesive unit - much like a well-oiled crew. Whether you're building a smart assistant platform, an automated customer service ensemble, or a multi-agent research team, CrewAI provides the backbone for sophisticated multi-agent interactions.
## Getting Started
To get started with CrewAI, follow these simple steps:


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. CrewAI uses UV for dependency management and package handling, offering a seamless setup and execution experience.

First, install CrewAI:

```bash
  pip install 'crewai[tools]'
```
    
## Code

crew.py

```bash
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
```

Agents.py

```bash
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
```

Task.py

```bash
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
```

Tools.py

```bash
from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@@@@@@@@')
```


##  Running Your Crew
Before running your crew, make sure you have the following keys set as environment variables in your .env file:

An OpenAI API key (or other LLM API key): OPENAI_API_KEY=sk-...

## Features

- Role-Based Agent Design: Customize agents with specific roles, goals, and tools.
- Autonomous Inter-Agent Delegation: Agents can autonomously delegate tasks and inquire amongst themselves, enhancing problem-solving efficiency.
- Flexible Task Management: Define tasks with customizable tools and assign them to agents dynamically.
- Processes Driven: Currently only supports sequential task execution and hierarchical processes, but more complex processes like consensual and autonomous are being worked on.
- Works with Open Source Models: Run your crew using Open AI or open source models refer to the Connect CrewAI to LLMs page for details on configuring your agents' connections to models, even ones running locally!


## 

![App Screenshot](https://github.com/crewAIInc/crewAI/blob/main/docs/crewAI-mindmap.png?raw=true)


## How CrewAI Compares

CrewAI's Advantage: CrewAI is built with production in mind. It offers the flexibility of Autogen's conversational agents and the structured process approach of ChatDev, but without the rigidity. CrewAI's processes are designed to be dynamic and adaptable, fitting seamlessly into both development and production workflows.

- Autogen: While Autogen does good in creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows.

- ChatDev: ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications.