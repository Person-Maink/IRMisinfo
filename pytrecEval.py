import pytrec_eval
import csv
import json

def parse_qrels(file_path):
    qrels = {}
    with open(file_path, 'r') as f:
        for line in f:
            topic_id, _, doc_id, relevance = line.strip().split()
            if topic_id not in qrels:
                qrels[topic_id] = {}
            qrels[topic_id][doc_id] = int(relevance)
    return qrels

def parse_bm25_output(file_path):
    run = {}
    with open(file_path, 'r') as f:
        for line in f:
            topic_id, _, doc_id, rank, score, run_id = line.strip().split()
            if topic_id not in run:
                run[topic_id] = {}
            run[topic_id][doc_id] = float(score)
    return run

qrels_file = 'D:\\Delft\\Uni\\Mod3\\Information Retrieval\\Project\\qrel and more\\qrels\\2020-derived-qrels\\misinfo-qrels-binary.useful-correct-credible'
# qrels_file = 'D:\\Delft\\Uni\\Mod3\\Information Retrieval\\Project\\qrel and more\\qrels\\misinfo-2020-qrels'
# qrels_file = 'bm25\\modified_qrels.txt'
# bm25_output_file = 'bm25\\final\\bm25_results.txt'
bm25_output_file = 'bm25\\final\\reranker_results.txt'

# output_csv_file = "ndcg_bm25.csv"
output_csv_file = "ndcg_bm25_final.csv"
qrel = parse_qrels(qrels_file)
run = parse_bm25_output(bm25_output_file)

evaluator = pytrec_eval.RelevanceEvaluator(qrel, {'ndcg'})

evaluation = evaluator.evaluate(run)
total_ndcg = 0
count = 0
for topic in evaluation:
    if 'ndcg' in evaluation[topic]:
        total_ndcg += evaluation[topic]['ndcg']
    count += 1
average_ndcg = total_ndcg / count if count > 0 else 0
evaluation['average_ndcg'] = average_ndcg

ndcg_data = []

for topic in evaluation:
    if topic != "average_ndcg":
        if 'ndcg' in evaluation[topic]:
            ndcg_data.append({'topic_id': topic, 'ndcg': evaluation[topic]['ndcg']})
ndcg_data.append({'topic_id': 'average_ndcg', 'ndcg': evaluation['average_ndcg']})

with open(output_csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['topic_id', 'ndcg']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    writer.writerows(ndcg_data)  # Write the data

print(f"NDCG scores have been saved to {output_csv_file}")