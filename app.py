from typing import List
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel, validator

app = FastAPI()

class RequestBody(BaseModel):
    data: List[str]
    

class ResponseBody(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_lowercase_alphabet: List[str]

@app.post("/bfhl")
async def bfhl_post(body: RequestBody):
    
    for v in body.data:
        if v.isdigit():
            continue
            
        if len(v) == 1 and v.isalpha():
            continue

        raise HTTPException(
                        status_code=400, 
                        detail=f"Invalid item: '{v}'. Each item must be either a single lowercase letter or a valid number."
                    )


    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    for data in body.data:
        if data.isalpha():
            alphabets.append(data)
            if chr(97) <= data <= chr(122):
                if len(highest_lowercase_alphabet) == 0:
                    highest_lowercase_alphabet.append(data)
                else:
                    if highest_lowercase_alphabet[0] < data:
                        highest_lowercase_alphabet.pop()
                        highest_lowercase_alphabet.append(data)

        if data.isdigit():
            numbers.append(data)

    return ResponseBody(
                is_success = True,
                user_id = "john_doe_17091999",
                email = "john@xyz.com",
                roll_number = "ABCD123",
                numbers = numbers,
                alphabets = alphabets,
                highest_lowercase_alphabet = highest_lowercase_alphabet
            )

@app.get("/bfhl")
async def bfhl_get():
    return {
        "operation_code" : 1
    }
