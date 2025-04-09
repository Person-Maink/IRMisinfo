from pyserini.search import SimpleSearcher
import os
import json
import xml.etree.ElementTree as ET
from tqdm import tqdm

# # Path to the directory where your index files are stored
# searcher = SimpleSearcher('TREC_MISINFO_index')  # change this to your index path

# # (Optional) You can set BM25 parameters manually if desired
# searcher.set_bm25(k1=0.9, b=0.4)

# # Your search query
# hits = searcher.search("Can lemon help COVID-19?", k=10)

# # Display results
# for i in range(len(hits)):
#     print(f'{i+1:2} {hits[i].docid:15} {hits[i].score:.5f}')
#     print(dir(hits[i]))



def eval_all_queries(query_file="Dataset/queries/topics/misinfo-2020-topics.xml", top_k=1000):
    # Build paths safely
    query_path = os.path.join(query_file)

    # Parse XML topic file
    tree = ET.parse(query_path)
    root = tree.getroot()

    searcher = SimpleSearcher('TREC_MISINFO_index')  # change this to your index path

    # (Optional) You can set BM25 parameters manually if desired
    searcher.set_bm25(k1=0.9, b=0.4)

    results_all = []
    # results_reranker = []

    # i = 0
    for topic in root.findall("topic"):
        # if i > 5: 
        #     return results_all
        # else: 
        #     i += 1 


        topic_results = []
        # topic_reranker = []

        topic_id = topic.find("number").text.strip()
        question = topic.find("description").text.strip()
        

            # Your search query
        results = searcher.search(question, k=top_k)

        for rank, doc in enumerate(results):
            trec_entry = {
                "topic_id": topic_id,
                "question": question,
                "url": doc.docid,
                "rank": rank + 1,
                "score": doc.score
            }
            topic_results.append(trec_entry)
            # results_reranker.append((str(rank), 0))
        results_all.append(topic_results)
        # print(topic_results)
        # results_reranker.append(topic_reranker)

    return results_all#, results_reranker

def map_urls_to_content_from_jsonl(jsonl_dir, urls, content_key="contents"):
    """
    Maps a list of URLs to their content using a directory of .jsonl files.

    Parameters:
        jsonl_dir (str): Directory containing JSONL files.
        urls (set or list): Set or list of URLs to find.
        url_key (str): Field name in JSONL for URL. Default is "url".
        content_key (str): Field name for content. Default is "contents".

    Returns:
        dict: {url: content, ...} for found URLs.
    """
    url_set = set(urls)
    url_to_content = {}

    for filename in os.listdir(jsonl_dir):
        if not filename.endswith(".jsonl"):
            continue

        file_path = os.path.join(jsonl_dir, filename)
        # for record in tqdm(ArchiveIterator(stream), desc="Extracting WARC documents"):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in tqdm(f, desc="Finding URLs in file"):
                try:
                    data = json.loads(line)
                    url = data.get("id")
                    content = data.get(content_key)
                    docid = data.get("docid")
                    if url in url_set and url not in url_to_content:
                        # print("found ", url)
                        url_to_content[url] = (content, docid)
                        if len(url_to_content) == len(url_set):
                            return url_to_content  # early exit if all found
                except json.JSONDecodeError:
                    continue

    return url_to_content


if __name__ == "__main__":
    results = eval_all_queries()
    bm25_urls = [doc['url'] for topic in results for doc in topic]  # flat list of all doc_ids
    print(bm25_urls[0])
    jsonl_dir = "Dataset_JSON"

    url_to_text = map_urls_to_content_from_jsonl(jsonl_dir, bm25_urls)

    # Example: print content for a specific doc_id
    some_id = bm25_urls[0]

    results_with_content = []
    for topic in results:
        topic_with_content = []
        for doc in topic:
            url = doc['url']
            doc['content'], doc['docid'] = url_to_text.get(url, "")  # fallback to empty string if not found
            topic_with_content.append(doc)
        results_with_content.append(topic_with_content)

output_path = "json_results.json"

with open(output_path, "w", encoding="utf-8") as out_f:
    json.dump(results_with_content, out_f)

print(f"Saved BM25 results with content to: {output_path}")



