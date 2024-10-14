import os
from dotenv import load_dotenv
from openai import OpenAI
from crewai import Agent, Task, Crew
from crewai_tools import WebsiteSearchTool
import pandas as pd


load_dotenv('.env')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def generate_response_to_query(user_input):

    tool_websearch1 = WebsiteSearchTool("https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-hdb")
    tool_websearch2 = WebsiteSearchTool("https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-financial-institutions")
    tool_websearch3 = WebsiteSearchTool("https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter")

    qa_agent = Agent(
        role="Q&A assistant",
        goal="Write a relevant and factually accurate response to a flat buyer's query from HDB: {user_input}",

        backstory="""As a customer service officer, you are incredibly resourceful in searching for relevant information. You engage customers with a warm, friendly demeanor, and a generous dose of empathy and cheerfulness. 
        You're writing a response to a flat buyer's query: {user_input}. 
        You collect information from HDB's official website on the various housing loan options available to assist the flat buyer. 
        If you find the answer on HDB's official website, include the URL and quote the exact words from which the information was extracted. 
        If the answer cannot be found, respond with understanding and offer general advice, while gently encouraging the buyer to reach out again if they have further questions, without using formal greetings or sign-offs.""",
        tools = [tool_websearch1, tool_websearch2, tool_websearch3],
        allow_delegation=False,
        verbose=False,
    )

    task = Task(
        description="""\
            1. Write a thoughtful response to the flat buyer's query: {user_input}.
            2. Proofread the response for grammatical errors and clarity.
            3. Use bolding to emphasize key words and phrases.
            4. Ensure the response is polite but does not include salutations or sign-offs.
            5. If the query cannot be answered, respond pleasantly and encourage the user to check the HDB website for more details, avoiding any formal greetings or closures.""",
        expected_output="A factually accurate and pleasant response to the query, well-formatted and free of grammatical errors.",
        agent=qa_agent
    )

    crew = Crew(
        agents=[qa_agent],
        tasks=[task],
        verbose=False
    )

    return crew.kickoff(inputs={"user_input": user_input})

def get_price():

    df = pd.read_csv("Resale flat prices based on registration date from Nov 2023 onwards.csv")

    max = int(df['resale_price'].max())

    return max

def generate_options(min, max, area, flat_types):
    
    # Read the CSV file
    df = pd.read_csv("Resale flat prices based on registration date from Nov 2023 onwards.csv")

    # Assuming min and max are either None or float values
    filtered_df = df[
        ((area == "None") | (df['town'] == area)) & 
        ((min is None or df['resale_price'] >= min) if min is not None else True) & 
        ((max is None or df['resale_price'] <= max) if max is not None else True) &
        (df['flat_type'].isin(flat_types) if flat_types else True)
    ]

    return filtered_df
