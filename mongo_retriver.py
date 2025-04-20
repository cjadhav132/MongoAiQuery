from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch
from langchain_voyageai import VoyageAIEmbeddings

connection_string = "mongodb+srv://cjadhav132:v4dD1vZKIq4v9rUx@cluster0.yp7xx8y.mongodb.net/"
db = "nik"
collection = "llm"
namespace = f"{db}.{collection}"
# Instantiate the vector store using your MongoDB connection string
vector_store = MongoDBAtlasVectorSearch.from_connection_string(
    # Atlas cluster or local deployment URI
    connection_string=connection_string,
    namespace=namespace,  # Database and collection name
    embedding=VoyageAIEmbeddings(),                 # Embedding model to use
    # Name of the vector search index
    index_name="llmTest",
    # Other optional parameters...
)
