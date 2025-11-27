from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"

def query_duckdb(sql_code: str, parameters=None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:
        cursor = conn.execute(sql_code, parameters=parameters) # execute istället för sql. execute tar in parameters också, till skillnad mot sql. För att skydda mot sql injection

        if sql_code.strip().lower().startswith(("select", "from", "desc", "pragma", "with")):
            return cursor.df()