from langchain_core.runnables import RunnableConfig
from langchain_core.tools import  tool
from documents.models import Document
@tool(description="list all active documents.")
def list_documents(config:RunnableConfig):
    #print(config)
    metadata = config.get('metadata') or config.get('configurable')
    user_id = metadata.get('user_id')
    qs = Document.objects.filter(active=True)
    response_data=[]
    for obj in qs:
        response_data.append(
            {
                "id": obj.id,
                "title": obj.title
            }
        )
    return response_data
@tool(description="get a document by id if its active'")
def get_document(document_id:int, config:RunnableConfig):
    metadata = config.get('metadata') or config.get('configurable')
    user_id = metadata.get('user_id')
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
