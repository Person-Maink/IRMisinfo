from warcio.archiveiterator import ArchiveIterator
import gzip
import json
from tqdm import tqdm
import time
import uuid
import os

uuids = set()

def check_json(input_path, docid_to_refersto):
    with gzip.open(input_path, 'rb') as stream:
        for record in tqdm(ArchiveIterator(stream), desc="Reading WARC documents"):
        # for record in ArchiveIterator(stream):
            if record.rec_type == 'conversion':
                doc_id = record.rec_headers.get('WARC-Record-ID')[10:-1]
                other_doc_id = record.rec_headers.get('WARC-Refers-To')[10:-1]
                # print(input_path, other_doc_id)
                # time.sleep(10)
                if uuid.UUID(doc_id) in uuids: 
                    # print("\nfound! ", input_path)
                    # list_stuff.add(input_path)
                    docid_to_refersto[doc_id] = other_doc_id
                # if uuid.UUID(other_doc_id) in uuids: 
                #     # print("\nfound (BAD)! ", input_path)
                #     list_stuff.add(input_path)
    return docid_to_refersto
                


if __name__ == "__main__":

    file_paths = [
        "json_results_newest.json"
    ]

    for path in file_paths: 
        with open(path, 'r') as file: 
            for line in file: 
                if line is None: 
                    continue
                else: 
                    data = json.loads(line)
                    for doc in data:
                        for thing in doc:
                            uuids.add(uuid.UUID(thing["docid"][10:-1]))
    print(len(uuids))


    docid_to_refersto = {}

    with open("pls.json", 'r') as fi:
        docid_to_refersto = json.load(fi)
    
    for i in range(1201,1801):
        input_path = f"Dataset\\{i}.warc.wet.gz"
        docid_to_refersto = check_json(input_path, docid_to_refersto)
        if(len(docid_to_refersto) >= 42452): 
            break
    print(docid_to_refersto)
    print(len(docid_to_refersto))

    with open("pls.json", 'r') as fi: 
        json.dump(docid_to_refersto, fi)




