from agents import Agent,Runner,AsyncOpenAI,set_default_openai_api,OpenAIChatCompletionsModel,set_default_openai_client,set_tracing_disabled
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
# set_default_openai_api(gemini_api_key)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client
)


def main():
    agent = Agent(
        name = "AgentDev",
        instructions="""You are EduDev, an educational assistant who helps users learn how to build AI agents using the OpenAI Agents SDK.

        Your role is to explain concepts clearly and simply, guide users through the steps of building agents, and answer technical questions in a supportive and encouraging tone.

        Avoid overwhelming users with too much jargon. Break complex ideas into simple terms, use examples where helpful, and always encourage curiosity.

        If a question is outside the scope of the OpenAI Agents SDK or basic AI agent development, politely explain that and steer the user back to relevant topics.

        Your goal is to help learners feel confident, supported, and motivated to keep experimenting with AI.""",
        model=model
    )

    result = Runner.run_sync(
        agent,
        "What is the purpose of the Runner.run_sync() method?"
    )
    print(result.final_output)
    with open("README.md", "a", encoding="utf-8") as readme_file:
        readme_file.write("\n\n## 💬 Sample Interaction\n")
        readme_file.write("**Prompt:**\n")
        readme_file.write(f"{repr('What is the purpose of the Runner.run_sync() method?')}\n\n")
        readme_file.write("**Response:**\n")
        readme_file.write(f"{result.final_output.strip()}\n")


if __name__ =="__main__":
    main()