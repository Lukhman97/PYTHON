from fastapi import FastAPI,Request

app=FastAPI()


fruit_dict = {
    "1": "Apple",
    "2": "Banana",
    "3": "Orange",
    "4": "Mango",
    "5": "Grapes"
}

@app.get("/lukhman/")
def read_root():
    return fruit_dict 

from fastapi import FastAPI, Request

app = FastAPI()

# Initial dictionary
fruit_dict = {
    "1": "Apple",
    "2": "Banana",
    "3": "Orange",
    "4":"jack fruit",
    "5":"cuted apple",
}

@app.post("/postlukhman/")
async def read_root(request: Request):
    global fruit_dict  # <-- important
    data = await request.json()
    

    fruit_dict.update(data)
    
    return fruit_dict
