from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uuid

from database import init_db, save_run, get_runs, get_trace
from agent import Agent


app = FastAPI()

# initialize database
init_db()

# enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = Agent()


class Query(BaseModel):
    prompt: str


@app.post("/run")
def run_agent(query: Query):

    run_id = str(uuid.uuid4())

    answer, reasoning = agent.run(query.prompt)

    # store run in database
    save_run(run_id, query.prompt, reasoning)

    return {
        "run_id": run_id,
        "answer": answer,
        "reasoning": reasoning
    }


@app.get("/runs")
def list_runs():
    return get_runs()


@app.get("/trace/{run_id}")
def get_run_trace(run_id: str):
    return get_trace(run_id)