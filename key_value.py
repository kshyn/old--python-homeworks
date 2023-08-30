import argparse
import json
import tempfile
import os

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
keysklad = {}
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
keysklad[args.key] = args.val
if os.path.isfile(storage_path):
    with open(storage_path, 'r') as f:
        dictator = json.load(f)
        if args.val in locals():
            if args.key in dictator:
                dictator[args.key] += args.val
            else:
                dictator[args.key] = args.val
        else:
            try:
                dictator[args.key]
            except KeyError:
                print(None)
            else:
                print(dictator[args.key])
        f.close()
    with open(storage_path, 'w') as f:
        json.dump(dictator, f)
        f.close()
else:
    print('')
    with open(storage_path, 'w') as f:
        dictator = {'key': 'value'}
        json.dump(dictator, f)
        f.close
