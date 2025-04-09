from warcio.archiveiterator import ArchiveIterator
import gzip
import json
from tqdm import tqdm
import time
import uuid
import os
# import uuid.UUID as u

ground_truth = set()

def write_json(input_path, output_path):
    with gzip.open(input_path, 'rb') as stream, open(output_path, 'w', encoding='utf-8') as out_file:
        for record in tqdm(ArchiveIterator(stream), desc="Extracting WARC documents"):
            if record.rec_type == 'conversion':
                url = record.rec_headers.get_header('WARC-Target-URI')
                text = record.content_stream().read().decode('utf-8').strip()
                doc_id = record.rec_headers.get('WARC-Record-ID')
                if text:  # only keep non-empty content
                    doc = {
                        "id": url,
                        "contents": text, 
                        "docid" : doc_id
                    }
                    out_file.write(json.dumps(doc) + '\n')
    os.remove(input_path)



def check_json(input_path, list_stuff):
    with gzip.open(input_path, 'rb') as stream:
        for record in tqdm(ArchiveIterator(stream), desc="Extracting WARC documents"):
        # for record in ArchiveIterator(stream):
            if record.rec_type == 'conversion':
                doc_id = record.rec_headers.get('WARC-Record-ID')[10:-1]
                other_doc_id = record.rec_headers.get('WARC-Refers-To')[10:-1]
                # print(input_path, other_doc_id)
                # time.sleep(10)
                if uuid.UUID(doc_id) in ground_truth: 
                    # print("\nfound! ", input_path)
                    list_stuff.add(input_path)
                if uuid.UUID(other_doc_id) in ground_truth: 
                    # print("\nfound (BAD)! ", input_path)
                    list_stuff.add(input_path)
    return list_stuff
                

if __name__ == "__main__":
    for i in range(1201, 1801):
        input_path = f"Dataset\\{i}.warc.wet.gz"
        output_path = f"Dataset_JSON\\{i}.jsonl"
        write_json(input_path, output_path)

    # file_paths = [
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels-binary.incorrect",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels-binary.useful",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels-binary.useful-correct",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels-binary.useful-credible",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels-graded.harmful-only",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels-graded.helpful-only",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels.2aspects.correct-credible",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels.2aspects.useful-credible",
    #     "Dataset/queries/qrels/2020-derived-qrels/misinfo-qrels.3aspects"
    # ]

    # for path in file_paths: 
    #     with open(path, 'r') as file: 
    #         for line in file: 
    #             if line is None: 
    #                 continue
    #             else: 
    #                 id = line.split()[2]
    #                 ground_truth.add(uuid.UUID(id))

    # # ground_truth.add(uuid.UUID("e8461a92-520d-4aeb-9a69-f127b2f90d9d"))
    # # print(ground_truth)


    # list_stuff = set()
    # # for i in range(1,301):
    # # for i in range(301,601):
    # # for i in range(601,901):
    # # for i in range(901,1201):
    # # for i in range(1201,1501):
    # # for i in range(1501,1801):
    # for i in range(1801,1889):
    #     input_path = f"Dataset\\{i}.warc.wet.gz"
    #     list_stuff = check_json(input_path, list_stuff)
    # print(list_stuff)


    