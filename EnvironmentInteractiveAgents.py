import tempfile
import autogen
from autogen import ConversableAgent, UserProxyAgent, AssistantAgent
from autogen.coding import LocalCommandLineCodeExecutor
from ModelConfigs import getAndSet_config

# select models to use
# Mistral (mixtral-8x7b-32768)
Gq_mistral = getAndSet_config("groq_llm_config_mixtral")

# azure
azure_OAI = getAndSet_config("azure_llm_config")

# temp directory
temp_dir = tempfile.TemporaryDirectory()

# create a local command line code executor
executor =  LocalCommandLineCodeExecutor(
    timeout=300,
    work_dir='workspace',
)

# create an agent with the local executor
code_executor_agent = ConversableAgent(
    "Terminal Administrator",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",

)
# sampel message.
message_with_code_block = """This is a message with code block.
The code block is below:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(0, 100, 100)
y = np.random.randint(0, 100, 100)
plt.scatter(x, y)
plt.savefig('scatter.png')
print('Scatter plot saved to scatter.png')
```
This is the end of the message.
"""

reply = code_executor_agent.generate_reply([
    {
        "role": "user",
        "content": message_with_code_block,
    }
])

print(reply)