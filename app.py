import os
from dotenv import  load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "llama-3.2-1b-preview", groq_api_key = groq_api_key)
messages = [
    SystemMessage(content ="Translate the following from english to hindi"),
    HumanMessage(content = "hello how are you?")
]
result = model.invoke(messages)
parser = StrOutputParser()

###using LCEL-chain components
# chain = model|output
# chain.invoke(messages)

### prompt template
generic_template = "translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]
)
chain = prompt|model|parser
output = chain.invoke({"language":"hindi","text":"hello"})
print(output)