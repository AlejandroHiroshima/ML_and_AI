from backend.constants import VECTOR_DB_PATH, DATA_PATH
from backend.data_models import Article
import lancedb
from pathlib import Path
import time

def setup_vector_db(path):
    path.mkdir(exist_ok=True)
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("articles", schema=Article, exist_ok=True)

    return vector_db

def ingest_docs_to_vector_db(table):
    for file_path in DATA_PATH.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        doc_id = file_path.stem
        table.delete(f"doc_id = '{doc_id}'")

        table.add([{
            "doc_id": doc_id,
            "filepath": str(file_path),
            "filename": file_path.stem,
            "content": content
        }])
        print(table.to_pandas()["filename"])
        time.sleep(20)

if __name__ == '__main__':
    vector_db = setup_vector_db(VECTOR_DB_PATH)
    ingest_docs_to_vector_db(vector_db["articles"])