from bs4 import BeautifulSoup
# from langchain.agents import load_tools
# from langchain.agents import initialize_agent, Tool
# from langchain_openai import OpenAI
import requests, os


# note: premier league = fc
def search_statmuse(query, sport):
    URL = f'https://www.statmuse.com/{sport}/ask/{query}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    description_tag = soup.find('meta', attrs={'name': 'description'})
    description_content = description_tag.get('content') if "Instant answers" not in description_tag.get('content') else "Sorry, I dont't understand your question."
    return(description_content)

# statmuse_tool = Tool(
#     name = "Statmuse",
#     func = search_statmuse,
#     description = "A sports search engine. Use this more than normal search if the question is about NBA basketball, like 'who is the highest scoring player in the NBA?'. Always specify a year or timeframe with your search. Only ask about one player or team at a time, don't ask about multiple players at once."
# )

# llm = OpenAI(temperature=0, api_key=os.environ.get("openai_key"))
# tools = load_tools(["serpapi", "llm-math"], llm=llm, serpapi_api_key=os.environ.get("serpapi_key")) + [statmuse_tool]
# agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# question = "Who has scored more points in the NBA this season, Jayson Tatum or Nikola Jokic? Can you subtract the difference in points between them?"
# print(question)
# print(agent.run(question))


