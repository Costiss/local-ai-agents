from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm


model = LiteLlm(model="ollama/llama3", api_base="http://localhost:11434")


name = "test_agent"

root_agent = Agent(
    model=model,
    name=name,
    description="A versatile agent capable of handling a wide range of tasks.",
    output_key=f"{name}_out",
)
