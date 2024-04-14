import os
from dotenv import load_dotenv
from rich.console import Console

# load the envirornment variables
load_dotenv()

con = Console()

# get the azure api key
azure_api_key= os.getenv("AZURE_API_KEY")
endpoint = os.getenv("azure_endpoint")
api_version = os.getenv("api_version")
deployment_name = os.getenv("deployment_name")

# groq key
groq_key = os.getenv("groq_key")

# anthropic key
anthropic_key = os.getenv("anthropic_key")

# set azure api key in the environment
os.environ["AZURE_API_KEY"] = azure_api_key


# GPT-4 llm config
llm_config ={
    "model":"gpt-4",
    "api_key": azure_api_key,
    "api_type": "openai",
}

# Groq llm config (mixtral-8x7b-32768)
groq_llm_config_mixtral = {
    "model": "mixtral-8x7b-32768",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": groq_key,
    "api_type": "openai",
}

# groq llm config (llama2-70b-4096)
groq_llm_config_llama2 = {
    "model": "llama2-70b-4096",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": groq_key,
    "api_type": "openai",
}

# groq llm config (gemma-7b-it)
groq_llm_config_gemma = {
    "model": "gemma-7b-it",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": groq_key,
    "api_type": "openai",
}

# athropic llm config (Pending proper Configuration)
anthropic_llm_config = {
    "model": "claude-3-opus-20240229",
    "api_key": anthropic_key,
    "base_url": "https://api.anthropic.com/v1",
    "api_type": "openai",
}

# azure llm config
azure_llm_config = {
    "model": deployment_name,
    "api_key": azure_api_key,
    "api_type": "azure",
    "base_url": endpoint,
    "api_version": api_version,
}


# function to log (console.log) all the initialized keys
def log_initializations():
    con.log(f"Azure API Key: {azure_api_key}")
    con.log(f"Azure Endpoint: {endpoint}")
    con.log(f"API Version: {api_version}")
    con.log(f"Deployment Name: {deployment_name}")
    con.log(f"Groq Key: {groq_key}")
    con.log(f"Anthropic Key: {anthropic_key}")


# Create an initially empty configs list
configs = []

def add_config(configs):
    configs.append({"instance": "llm_config", "config": llm_config})
    configs.append({"instance": "groq_llm_config_mixtral", "config": groq_llm_config_mixtral})
    configs.append({"instance": "groq_llm_config_llama2", "config": groq_llm_config_llama2})
    configs.append({"instance": "groq_llm_config_gemma", "config": groq_llm_config_gemma})
    configs.append({"instance": "anthropic_llm_config", "config": anthropic_llm_config})
    configs.append({"instance": "azure_llm_config", "config": azure_llm_config})



# function selects the config object based on the instance name
def getAndSet_config(instance):
    for config in configs:
        if config["instance"] == instance:
            return config["config"]
    return None

# add the config objects
add_config(configs)
con.log(f"Configurations Loaded")

# log the initialization
log_initializations()
con.log(f"Configurations Initialized")