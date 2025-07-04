from langgraph.prebuilt import create_react_agent
from ai.llms import get_openai_model
from ai.tools import document_tools
def get_document_agent(model=None, checkpointer=None):
    llm_model = get_openai_model()
    agent = create_react_agent(
        model=llm_model,
        tools= document_tools,
        prompt="You are a helpful assistant in managing the user documents within this app",
        checkpointer=checkpointer
    )
    return agent
   