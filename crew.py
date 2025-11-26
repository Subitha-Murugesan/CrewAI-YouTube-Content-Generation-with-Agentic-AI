from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task

from dotenv import load_dotenv
load_dotenv()


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default 
  #sequential- one after another
  #parallel - at the same time
  verbose=True,
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'Genai tutorials'})
print(result)