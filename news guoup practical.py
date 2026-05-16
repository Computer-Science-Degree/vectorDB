import chromadb
client = chromadb.Client()
print("ChromaDB version:", chromadb.__version__)
print("Client created successfully")

collection = client.create_collection(name="my_first_collection")
print(f"Collection '{collection}' created successfully")
print (f"Number of items: {collection.count()}")

collection.add(
  documents= [
      "The more data the machine holds the more advance it becomes",
      "Sigiriya is a place of historical significance in Srilanka",
      "Python is the most commonly used programmer tool",
     "The Middle east are consisted of deserts",
     "The dodo birds are extinct"  
  ],
  ids= ["doc1","doc2","doc3","doc4","doc5"],
 metadatas = [
    {"category":"AI","difficulty":"beginner"},
     {"category":"geography","difficulty":"intermediate"},
     {"category":"Programming","difficulty":"beginner"},
     {"category":"geography","difficulty":"beginner"},  
    {"category":"animals","difficulty":"intermediate"},
 ]
)

print(f"Inserted documents. Collection now has {collection.count()} items.")



results = collection.query(
    query_texts=["What is artificial intellignece?"],
    n_results=2
)

print ("\n-------query results -------\n")
for i ,(doc,distance,meta) in enumerate(zip(results["documents"][0],
                                           results["distances"][0],
                                           results["metadatas"][0])):
    print (f"\n Result{i+1}:")
    print(f"Document: {doc}")
    print(f"Distance :{distance:.4f} lower= more similar)")
    print(f"Metadata: {meta}")
