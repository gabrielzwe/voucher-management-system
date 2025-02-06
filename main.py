from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Voucher Management System API is running!"}
