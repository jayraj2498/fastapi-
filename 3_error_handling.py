# Error handling  

# Example of Basic Error Handling with HTTPException 


from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/item/{item_id}")
async def read_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Item ID must be greater than zero")
    return {"item_id": item_id}



@app.get("/input/{input_id}") 
async def use_data(input_id:int) :
    if input_id < 1 :
        raise HTTPException(status_code=401, detail="Your Input is not get recognize") 
    
    return {"Your item_id is":input_id}     


# Custom Error Handling with Exception Handlers   



@app.get("/error/handling") 
async def handle_error(item:int) :
    if item== 2: 
        return HTTPException(status_code=400 , detail="you have added 2 ie y you facing error")
    
    return{"Item number is":item}





from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse 


app = FastAPI()

# Step 1: Define a custom exception class
class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

# Step 2: Create the handler function for this custom exception
@app.exception_handler(ItemNotFoundException)
async def item_not_found_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Item with ID {exc.item_id} not found"},
    )

# Step 3: Use the custom exception in an endpoint
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id != 42:  # Assuming only item ID 42 exists
        raise ItemNotFoundException(item_id=item_id)
    return {"item_id": item_id, "name": "Sample Item"}  








from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred"},
    )