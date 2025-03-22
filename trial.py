# from warcio.archiveiterator import ArchiveIterator

# with open('Dataset/1.warc', 'rb') as stream:
#     for record in ArchiveIterator(stream):
#         if record.rec_type == 'response':
#             print(record.rec_headers)
#             # print(record.content_stream())
#             # print(record.content_stream().read().decode('utf-8'))
#             exit()

# from warcio.archiveiterator import ArchiveIterator
# import re
# import nltk
# from nltk.tokenize import word_tokenize
# from tqdm import tqdm
# from rank_bm25 import BM25Okapi

# nltk.download('punkt')

def extract_documents_from_warc(warc_file):
    documents = []
    doc_ids = []  # Store unique document IDs

    with open(warc_file, 'rb') as f:
        for record in tqdm(ArchiveIterator(f), desc="Extracting WARC documents"):
            if record.rec_type == 'response':  # Extract only web page responses
                url = record.rec_headers.get('WARC-Target-URI')
                content = record.content_stream().read().decode('utf-8', errors='ignore')
                
                # Simple text cleaning
                text = re.sub(r'<[^>]+>', '', content)  # Remove HTML tags
                text = re.sub(r'\s+', ' ', text).strip()  # Normalize spaces
                
                if len(text) > 100:  # Filter out empty or very short pages
                    documents.append(text)
                    doc_ids.append(url)  # Use URL as document ID

    return documents, doc_ids

# # Load documents

# # Tokenize documents
# tokenized_documents = [word_tokenize(doc.lower()) for doc in documents]

# # Build BM25 index
# bm25 = BM25Okapi(tokenized_documents)

# print("BM25 index built successfully!")

# def query_bm25(query, top_n=5):
#     query_tokens = word_tokenize(query.lower())  # Tokenize query
#     scores = bm25.get_scores(query_tokens)  # Compute BM25 scores
    
#     # Get top N ranked documents
#     ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_n]
    
#     results = []
#     for i in ranked_indices:
#         results.append({
#             "rank": len(results) + 1,
#             "url": doc_ids[i],
#             "bm25_score": scores[i],
#             "snippet": documents[i][:300] + "..."  # Show a snippet
#         })
    
#     return results

# # Example query
# query = "Are lemons bad for COVID-19?"
# results = query_bm25(query, top_n=5)

# # Display results
# for res in results:
#     print(f"\nRank {res['rank']}: {res['url']}")
#     print(f"Score: {res['bm25_score']:.2f}")
#     print(f"Snippet: {res['snippet']}")

from warcio.archiveiterator import ArchiveIterator

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh.writing import AsyncWriter

import re, os
from tqdm import tqdm
import nltk
from nltk.tokenize import word_tokenize

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

nltk.download('punkt')
# Define schema for document storage
schema = Schema(title=ID(stored=True), content=TEXT(stored=True))
# Create an index directory
ix = create_in("indexdir", schema)

# Add documents to index
warc_file = "Dataset/1.warc"
documents, doc_ids = extract_documents_from_warc(warc_file)
print(f"Extracted {len(documents)} documents.")



chunk = 1000
with ix.writer() as writer:
    for i in tqdm(range(0,len(documents), chunk)):
        for j in range(i, i+chunk):
            docs = [{"title": doc_ids[j], "content": word_tokenize(documents[j].lower())} for i in range(len(documents))]

        for doc in docs:
            writer.add_document(title=doc["title"], content=doc["content"])

# Search for relevant documents using BM25
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("Artificial Intelligence")
    results = searcher.search(query, limit=5)

    for result in results:
        print(f"Title: {result['title']}, Score: {result.score}")
