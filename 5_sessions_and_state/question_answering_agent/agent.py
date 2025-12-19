from google.adk import Agent

question_answering_agent = Agent(
    name="question_answering_agent",
    model="gemini-2.5-flash-preview-09-2025",
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.
    
    Here is some information about the user:
    Name:
    {user_name}
    Preferences:
    {user_preferences}
    """
)
