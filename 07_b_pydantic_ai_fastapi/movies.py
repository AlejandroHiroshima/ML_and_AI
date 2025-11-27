from fastapi import FastAPI

app= FastAPI()

@app.get("/movies")
async def read_movies():
    pass

@app.post("/movies/create_movie")
async def create_movies():
    pass
