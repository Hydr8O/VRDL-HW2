from pathlib import Path
from tqdm import tqdm
from collections import OrderedDict
import json

with open('answer-example.json', 'r') as answer_example:
    answer_example = json.load(answer_example)

with open('detections_val2017_best_results.json', 'r') as answer:
    answer = json.load(answer, object_pairs_hook=OrderedDict)

print(answer_example[0]['image_id'])

image_ids = [x['image_id'] for x in answer_example]
seen = set()
seen_add = seen.add
image_ids = [x for x in image_ids if not (x in seen or seen_add(x))]
final_answer = []
for id in tqdm(image_ids):
    for result in answer:
        if result['image_id'] == id:
            final_answer.append(result)

with open('answer.json', 'w') as final_file:
    json.dump(final_answer, final_file)
