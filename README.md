# CrewAI-YouTube-Content-Generation-with-Agentic-AI

This project demonstrates **CrewAI**, a powerful **agent orchestration framework** that enables multiple AI agents to collaborate and autonomously complete complex tasks. Using CrewAI, we create a **Blog Researcher** agent to extract video insights from YouTube and a **Blog Writer** agent to generate engaging blog posts.  

---

## Why CrewAI?

CrewAI is at the heart of this project, providing:  

- **Multi-Agent Coordination:** Easily manage multiple agents with specialized roles.  
- **Task Orchestration:** Execute tasks sequentially or in parallel, with configurable dependencies.  
- **Memory & Context:** Agents can retain knowledge and share context for coherent outputs.  
- **Delegation:** Agents can delegate subtasks to other agents for efficiency.  
- **Scalability & Customization:** Add more agents, tools, and tasks seamlessly.  

With CrewAI, you can build complex workflows like content research, summarization, or even full-scale autonomous content creation pipelines.  

---

## Features

- **Autonomous Video Research:** Extract and summarize relevant YouTube video content automatically.  
- **Blog Writing:** Generate professional, readable blog posts from research outputs.  
- **Flexible Execution:** Choose sequential or parallel execution for tasks.  
- **Tool Integration:** Connect to any external tools, like YouTube channel search.  
- **Agentic AI Architecture:** Each agent has a defined role, memory, and backstory to enhance performance.  

---

## Usage

### 1. Define Agents (`agent.py`)

```python
from crewai import Agent, LLM
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="gemini/gemini-2.0-flash", temperature=0.1)

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get relevant video transcription for the topic {topic} from the provided YT channel',
    verbose=True,
    memory=True,
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)
```

### 2. Define Tasks (`tasks.py`)

```python
from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

research_task = Task(
    description="Identify the video {topic} and get detailed info.",
    expected_output="A 3-paragraph report based on the {topic} of video content.",
    tools=[yt_tool],
    agent=blog_researcher
)

write_task = Task(
    description="Summarize the info from the YouTube video on {topic}.",
    expected_output="Create a blog post from the video content.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
```

### 3. Run the Crew (`crew.py`)

```python
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,
  verbose=True,
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result = crew.kickoff(inputs={'topic':'GenAI tutorials'})
print(result)
```

---

## How CrewAI Works

1. **Create Agents:** Each agent has a role, goal, and access to tools.  
2. **Define Tasks:** Assign tasks to agents with expected outputs and tool integrations.  
3. **Assemble Crew:** Group agents and tasks using CrewAI.  
4. **Execution:** CrewAI manages the workflow, allowing sequential or parallel execution.  
5. **Delegation & Memory:** Agents can delegate subtasks and share memory for coherent results.  

CrewAI handles all orchestration, letting you focus on designing agents and workflows instead of managing task execution manually.  

---

## Example Output

The generated blog post will be saved in `new-blog-post.md`, containing a clear, well-structured article summarizing the YouTube content for your specified topic.  

---

## Tools

- **CrewAI:** Orchestrates multiple AI agents efficiently  
- **YoutubeChannelSearchTool:** Extracts video data from specific YouTube channels  
- **LLM (Gemini 2.0 Flash):** Generates text and summaries  

