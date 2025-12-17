from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash-preview-09-2025',
    name='greeting_agent',
    description="Greeting agent",
    instruction="You are a helpful assistant that greets the user. Ask for the user's name and greet them by name",
)