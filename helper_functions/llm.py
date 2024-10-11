import os
from dotenv import load_dotenv
from openai import OpenAI
from crewai import Agent, Task, Crew
from crewai_tools import WebsiteSearchTool
import pandas as pd
import tiktoken


load_dotenv('.env')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def generate_response_to_user_query(user_input):

    tool_websearch1 = WebsiteSearchTool("https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-hdb")
    tool_websearch2 = WebsiteSearchTool("https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-financial-institutions")

    qa_agent = Agent(
        role="Q&A assistant",
        goal="Write a relevant and factually accurate response to a flat buyer's query from HDB: {user_input}",

        backstory="""As a customer service officer, you are incredibly resourceful in searching for relevant information and engage customers with a huge dose of empathy and an ever-cheerful attitude.
        You're writing a response to a flat buyer's query: {user_input}.
        You collect information from HDB's official website on what are the different housing loan options in order to answer flat buyer's query.
        If the answer can be found on HDB's official website, include the URL and quote the exact words from which the information was extracted from.
        If the answer cannot be found on HDB's official website, respond that you are unable to assist with the query.""",
        tools = [tool_websearch1, tool_websearch2],
        allow_delegation=False,
        verbose=False,
    )

    task = Task(
        description="""\
        1. Write a response to the flat buyer's query: {user_input}.
        2. Proofread for grammatical errors.
        3. Use bolding to emphasize key words and phrases.
        4. Adopt a soothing and pleasant tone in the response, especially if the query cannot be answered.
        """,

        expected_output="A factually accurate and pleasant response to the query.",
        agent=qa_agent
    )

    crew = Crew(
        agents=[qa_agent],
        tasks=[task],
        verbose=False
    )

    return crew.kickoff(inputs={"user_input": user_input})

def generate_options(min, max, area):

    min_value = float(min)
    max_value = float(max)
    
    # Read the CSV file
    df = pd.read_csv("Resale flat prices based on registration date from Nov 2023 onwards.csv")

    filtered_df = df[(df['town'] == area) & (df['resale_price'] >= min_value) & (df['resale_price'] <= max_value)]  # Replace accordingly

    return filtered_df


