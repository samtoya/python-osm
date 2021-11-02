import json
import os


class FileWriter:
    @classmethod
    def save(cls, filename, data, directory='output'):
        filepath = f'{directory}/{filename}.json'
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(json.dumps(data))
        f.close()
