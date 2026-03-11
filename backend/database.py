import sqlite3
import json

DB_NAME = "traces.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id TEXT PRIMARY KEY,
        prompt TEXT,
        trace TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_run(run_id, prompt, trace):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO runs (id, prompt, trace) VALUES (?, ?, ?)",
        (run_id, prompt, json.dumps(trace))
    )

    conn.commit()
    conn.close()


def get_runs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, prompt FROM runs")

    rows = cursor.fetchall()
    conn.close()

    return [{"id": r[0], "prompt": r[1]} for r in rows]


def get_trace(run_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT trace FROM runs WHERE id=?", (run_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return json.loads(row[0])

    return []