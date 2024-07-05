from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
from textwrap import dedent
load_dotenv()

#call the gemini model
llm=ChatGoogleGenerativeAI(
                            model="gemini-1.5-flash",
                            verbose=True,
                            temperature=0.5,
                            google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a Senior researcher agent with memory and verbose

news_researcher=Agent(
                 role="Senior Researcher",
                 goal='Unccover ground breaking technologies in {topic}',
                 verbose=True,
                 memory=True,
                 backstory=dedent("""\
                           Driven by curiosity, you're at the forefront of
                           innovation, eager to explore and share knowledge that could change
                           the world."""),
                tools=[tool],
                 llm=llm,
                allow_delegation=True)

# Writing agent responsibile for new blog
news_writer=Agent(
            role="writer",
            goal="Narrate a compelling stories about a {topic}",
            verbose=True,
            memory=True,
            backstory=dedent("""\
                       With a flair of Simplifying topics,
                       you craft engaging narratives that captivate and educate,
                       bringing new discoveries to light in accessible manner."""),
            tools=[tool],
            llm=llm,
            allow_delegation=False)



