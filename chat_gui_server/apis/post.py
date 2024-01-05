from fastapi import FastAPI, Body
from starlette.middleware.cors import CORSMiddleware  
  
app = FastAPI()  
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
  
@app.post("/")  
async def read_post():  
    return {"data": "Hello"}  

def test_demo():
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=5001)