from fastapi import FastAPI, responses
import uvicorn
from call_agent import call_agent

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/query/{query}")
async def query(query: str):
    return responses.JSONResponse(content= await call_agent(query))
    

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)