import os 
from autogen import ConversableAgent, register_function
from Tools.calc import calculator
from ModelConfigs import getAndSet_config, con

# set the models to use
azure_llm_config = getAndSet_config("azure_llm_config")

# mistral llm config
mistral_llm_config = getAndSet_config("groq_llm_config_mixtral")

# gemar-7b-it
gemma_llm_config = getAndSet_config("groq_llm_config_gemma")

# Let's first define the assistant agent that suggests tool calls.

assistant = ConversableAgent(
    name="assistant",
    system_message="""
    I am an assistant that suggests tool calls you help with doing basic calculations.
    
    # NOTE
    After you have complered the calculations return 'TERMINATE' when the task is done. 
    as well if you receive no question or input please return 'TERMINATE' to end the conversation.
    """,
    llm_config=azure_llm_config,
)


# user proxy agent
user_proxy = ConversableAgent(
    name="user",
    system_message="""
    You assist in getting things done, advise and let the other agent know when to terminate the conversation, ensure they respond with 'TERMINATE' when the task is done.
    """,
    llm_config=mistral_llm_config,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)


def check_tool_schema(agent):
    info = agent.llm_config["tools"]
    return info

def register_tool_per_agent():

    #  register the calculator tool with the assistant.
    assistant.register_for_llm(
        name="calculator",
        description="A simple calculator tool that performs basic calculations.",
    )(calculator)

    # register the tool function for the user proxy agent.
    user_proxy.register_for_execution(
        name="calculator"
    )(calculator)

    print("Tool registration complete.")
    return True

def register_for_all_agents():
    
    # register the calculator tool for all agents.
    register_function(
        calculator,
        caller=assistant,
        executor=user_proxy,
        name="calculator",
        description="A simple calculator tool that performs basic calculations.",
    )

    print("Tool registration complete.")
    return True


# register with all agents
register_for_all_agents()


con.log(check_tool_schema(assistant))