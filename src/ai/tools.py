from langchain_core.runnables import RunnableConfig
from langchain_core.tools import  tool
from documents.models import Document
@tool(description="list the most recent 5 documents for the current user.")
def list_documents(config:RunnableConfig):
    #print(config)
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    qs = Document.objects.filter(owner_id=user_id, active=True).order_by("-created_at")
    response_data=[]
    for obj in qs[:5]:
        response_data.append(
            {
                "id": obj.id,
                "title": obj.title
            }
        )
    return response_data
@tool(description="get a document by id if its active'")
def get_document(document_id:int, config:RunnableConfig):
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    if user_id is None:
        raise Exception("invalid request for a user.")
    try:
        obj = Document.objects.get(id=document_id, owner_id=user_id, active=True)

    except Document.DoesNotExist:
        raise Exception("document not found, try again")
    except:
        raise Exception("invalid request for a document details, try again")
    response_data={
        "id": obj.id,
        "title": obj.title
    }
    return response_data

document_tools=[
    list_documents,
    get_document
]
