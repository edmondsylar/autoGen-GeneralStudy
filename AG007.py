#  this script is going to include local Execution.

import autogen
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
import os
from dotenv import load_dotenv
from rich.console import Console
# 
from ModelConfigs import getAndSet_config


con = Console()
# import autogen.agentchat.contrib.multimodal_conversable_agent as mca

# select models to use
# Mistral (mixtral-8x7b-32768)
Gq_mistral = getAndSet_config("groq_llm_config_mixtral")

# Llama2
Gq_llama2 = getAndSet_config("groq_llm_config_llama2")

# gemma
Gq_gemma = getAndSet_config("groq_llm_config_gemma")

# azure
azure_OAI = getAndSet_config("azure_llm_config")

# simple conversable agent
agent = ConversableAgent(
    "chatbot",
    llm_config=azure_OAI,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

msg = []

def buildMemory(content, role):
    _ = {
        "role": role,
        "content": content
    }
    msg.append(_)

def chat():
    while True:
        user_input = input("You: ")
        buildMemory(user_input, "user")
        
        response = agent.generate_reply(messages=msg)
        
        buildMemory(response, "assistant")
        
        print("Bot: ", response)


# agent cathy
cathy = ConversableAgent(
    "Caherine",
    system_message='''
    Your name is Cathy and you are a part of a duo of comedians.
    ''',
    llm_config=Gq_mistral,
    human_input_mode="NEVER",

)

# agent Joe.
joe = ConversableAgent(
    "Joe",
    system_message='''
    Your name is Joe and you are a part of a duo of comedians.
    ''',
    llm_config=azure_OAI,
    human_input_mode="NEVER",
)

# initiate the chat between the two agents
result = joe.initiate_chat(cathy, message="Catherine, tell me a joke about why we can't do withouth house flies", max_turns=5)