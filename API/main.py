from fastapi import FastAPI

dicttt={
    "name":["lukhman","naveen"],
    "age":[23,34]
}

app=FastAPI()

@app.get("/lukhman786")

def read_only():
    return "i am naveen",dicttt.json()
