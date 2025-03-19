# Sample documents (like web pages or articles)
documents = [
    "Python is a programming language",
    "JavaScript is used for web development",
    "Python is great for data science",
    "Machine learning is a field of artificial intelligence"
]

# Function to search for a keyword in the documents
def search(query):
    results = []
    index=1

    for doc in documents:

        if query.lower() in doc.lower():
            results.append(f"Document {index}: {doc}")
            
            index+=1
    return results

# User input for the search query
query = input("\nEnter your search query: ")

# Display the results with Indexing

if search(query):
    print("\nSearch Results:")
    
    for result in search(query):
        print(result)
    print('\n')    
else:
    print("\nNo results found.")
