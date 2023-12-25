from fastapi import FastAPI, Body  
  
app = FastAPI()  
  
@app.post("/")  
async def read_post():  
    return {"message": "Hello"}  

def test_demo():
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=8080)