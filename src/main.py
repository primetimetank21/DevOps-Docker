from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host="redis-db", port=6379)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/hits")
async def get_hits():
    r.incr("hits")
    return {"hits": r.get("hits")}