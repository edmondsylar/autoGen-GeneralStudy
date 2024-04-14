import os
import os 
from autogen import ConversableAgent
from Tools.calc import calculator
from ModelConfigs import getAndSet_config, con

# set the models to use
azure_llm_config = getAndSet_config("azure_llm_config")

# mistral llm config
mistral_llm_config = getAndSet_config("groq_llm_config_mixtral")

# gemar-7b-it
gemma_llm_config = getAndSet_config("groq_llm_config_gemma")

# Let's first define the assistant agent that suggests tool calls.

from autogen import ConversableAgent

student_agent = ConversableAgent(
    name="Student_Agent",
    system_message="You are a student willing to learn.",
    llm_config=gemma_llm_config,
)
teacher_agent = ConversableAgent(
    name="Teacher_Agent",
    system_message="You are a math teacher.",
    llm_config=azure_llm_config,
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    message="What is triangle inequality?",
    summary_method="reflection_with_llm",
    max_turns=2,
)

con.log(chat_result.summary)
print("\n")
con.log(chat_result.chat_history)
print("\n")
con.log(chat_result.cost)