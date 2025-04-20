import pymongo
import requests

connection_string = "mongodb+srv://cjadhav132:v4dD1vZKIq4v9rUx@cluster0.yp7xx8y.mongodb.net/"
client = pymongo.MongoClient(connection_string)
# "mongodb+srv://beau:bngeFBqJJoEWqRNd@cluster0.svcxhgj.mongodb.net/?retryWrites=true&w=majority")
db = client.nik
collection = db.llm


embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:

    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(
            f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# for doc in collection.find().limit(50):
#   doc['EmploymentStatus_embedding_hf'] = generate_embedding(doc['EmploymentStatus'])
#   collection.replace_one({'_id': doc['_id']}, doc)


# query = "imaginary characters from outer space at war"
query = "unemployed"

# results = collection.aggregate([
#     {"$vectorSearch": {
#         "queryVector": generate_embedding(query),
#         "path": "EmploymentStatus_embedding_hf",
#         "numCandidates": 100,
#         "index": "PlotSemanticSearch",
#     }}
# ])

query = "Show me the top 10 loan defaulters with high loan amounts.",
# query = "What is the average credit score of borrowers who defaulted in the last 2 years?"

results = collection.aggregate([
    {
        "$search": {
            "index": "default",
            "text": {
                "query": query,
                "path": {
                    "wildcard": "*"
                }
            }
        }
    }
])

print(len(list(results)))

# for document in results:
#     print(document['EmploymentStatus'])
    # print(
    #     f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
