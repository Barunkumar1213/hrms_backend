from bson import ObjectId

def serialize_doc(doc: dict) -> dict:
    doc["_id"] = str(doc["_id"])
    return doc

def serialize_docs(docs: list) -> list:
    return [serialize_doc(doc) for doc in docs]
