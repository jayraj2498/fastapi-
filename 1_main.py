from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Union 
from enum import Enum

app = FastAPI()


# @app.get("/") 
# async def root() : 
#     return {"message":"Hello from Fastapi first time "} 


# @app.get("/hi") 
# async def hey() : 
#     return {"message":"Hello How are you : "} 



# ------------------- ---------------------------- ------------------------

# # Path Parameters : 

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"your item_id is : ": item_id}  


# @app.get("/count/{std_count}") 
# async def school(std_count):
#     return{"Total number of count is:": std_count} 

# @app.get("/info") 
# def data(name:str , city:str , age:int) : 
#     var_name = {"name is":name , "age is":age , "from city":city} 
#     return var_name 


# @app.get("/new_info") 
# def new_data(name:str , city:str , age:int) : 
#     return f"your name is {name} from {city} and your age is {age}" 


# @app.get("/union") 
# def fun(name:str , age:Union[int,None]=None) : 
#     return f"your name is {name} your age is {age}"



# class choice_name(str,Enum) : 
#     one="one" 
#     two="two"
#     three="three" 
    
    
# @app.get("/model/{model_name}") 
# async def get_model(model_name:choice_name):
#     return{"Your select model  is ": model_name}



# # Define an enum for product categories
# class ProductCategory(str, Enum):
#     electronics = "electronics"
#     clothing = "clothing"
#     books = "books"

# # Endpoint to get products by category
# @app.get("/products/{category}")
# async def get_products_by_category(category: ProductCategory):
#     # Dummy data for illustration
#     products = {
#         "electronics": ["Laptop", "Smartphone", "Headphones"],
#         "clothing": ["T-Shirt", "Jeans", "Jacket"],
#         "books": ["The Great Gatsby", "1984", "To Kill a Mockingbird"]
#     }
#     return {"category": category, "products": products[category.value]} 







# # Define an Enum with different types of fruits
# class Fruit(str, Enum):
#     apple = "apple"
#     banana = "banana"
#     orange = "orange"

# # Define an endpoint that accepts a fruit name
# @app.get("/fruits/{fruit_name}")
# async def get_fruit_info(fruit_name: Fruit):
#     if fruit_name == Fruit.apple:
#         return {"fruit_name": fruit_name, "message": "An apple a day keeps the doctor away!"}
    
#     elif fruit_name == Fruit.banana:
#         return {"fruit_name": fruit_name, "message": "Bananas are high in potassium."}
    
#     elif fruit_name == Fruit.orange:
#         return {"fruit_name": fruit_name, "message": "Oranges are a great source of Vitamin C."}

#     # This line will never be reached because we've covered all enum values
#     return {"fruit_name": fruit_name, "message": "Unknown fruit"} 




# class war(str,Enum):
#     army ="army" 
#     airforce="airforce" 
#     navy="navy" 
    
    
# @app.get("/strike/{attack}") 
# async def strike_force(attack:war) :
#     if attack == war.army:
#         return{"strike_by":attack , "message":"We gonna strike by Special forces Keep them Alert" } 
    
#     elif attack == war.airforce :
#         return{"strike_by":attack , "message":"We decide to Bombard enemies imp location keep piolot ready"} 
    
#     elif attack==war.navy:
#         return{"strike_by":attack , "message":"we have have decided to strike by Cruise missile keep navy on alert"} 
    
#     return{"strike_by":attack , "message":"wait for command over & Out"}
    
    



# #topic 3 
# # request body 

# from pydantic import BaseModel 


# class schema(BaseModel):
#     name:str 
#     roll_no : int 
#     div:str
 
 
# @app.post("/items/")
# async def create_item1(item:schema):
#     return item




# #ex2 

# class Item(BaseModel):
#     name:str 
#     description:Union[str,None] = None 
#     price:float 
#     tax:Union[float,None]=None 
    
    
# @app.post("/items1")
# async def create_item(item:Item):
#     return item  




from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional 




# # Define the User model
# class UserRegistration(BaseModel):
#     name: str = Field(..., example="John Doe")
#     email: EmailStr = Field(..., example="john.doe@example.com")
#     age: Optional[int] = Field(None, gt=0, le=120, example=30)
#     subscriptions: List[str] = Field(..., example=["Basic", "Premium"])

# # Define an endpoint to register a new user
# @app.post("/register/")
# async def register_user(user: UserRegistration):
#     # Here we can add logic to save the user data to a database, etc.
#     return {
#         "message": "User registered successfully",
#         "user": user
#     }  
    
    
    
    
# #  Validating Query Parameters    
    
from fastapi import FastAPI, Query, Path
from typing import Optional



# @app.get("/search/")
# async def search_items(
#     name: Optional[str] = Query(None, min_length=3, max_length=50, regex="^[a-zA-Z]*$"),
#     count: Optional[int] = Query(1, gt=0, le=100)):
#     return {"name": name, "count": count}



# # Path Parameter Validation


# @app.get("/items/{item_id}")
# async def get_item(
#     item_id: int = Path(..., gt=0),
#     category: Optional[str] = Query(None, min_length=3, max_length=20)
# ):
#     return {"item_id": item_id, "category": category}  




# # Numerical Validation in Query and Path Parameters


# @app.get("/products/{product_id}")
# async def get_product(
#     product_id: int = Path(..., gt=0, lt=1000),  # Path param with range 1-999
#     price: Optional[float] = Query(None, gt=0.0, lt=10000.0)  # Query param with range 0-10,000
# ):
#     return {"product_id": product_id, "price": price}  



# @app.get("/input/{your_ip}")
# async def get_ip( 
#     sr_no :int = Path(...,gt=0 , le=101)  , 
#     name: str = Query(None, min_length=3, max_length=50, regex="^[a-zA-Z\s]*$"),

#     price:Optional[float] = Query(None , gt=1000 , lt=9999) ) :
    
#     return {"serial_no is ": sr_no , "your_name":name , "price is ":price}  




# # topic 4 :

# # Post request with form data   

from fastapi import FastAPI, Form , HTTPException


# @app.post("/form/data") 
# async def form_data(username:str = Form(...) ,
#                     id_number:int = Form(...)) :  
    
#     return{"username":username , "your_id":id_number}
    
    
    


# @app.post("/login/")
# async def login(
#     username: str = Form(...),
#     password: str = Form(...),
# ):
#     if username == "admin" and password == "password123":
#         return {"message": "Login successful!"}
#     else:
#         raise HTTPException(status_code=401, detail="You Have Invalid credentials")
    
    
    
    
    
# ex 2 .     

# In-memory storage for registered users
users_db = {}

@app.post("/register1/")
async def register(
    username: str = Form(...), 
    password: str = Form(...)):
    if username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Store the user in the in-memory "database"
    users_db[username] = password
    return {"message": "User registered successfully!"}


@app.post("/login1/")
async def login1(
    username: str = Form(...), 
    password: str = Form(...)):
    # Check if the username exists and if the password matches
    if username not in users_db or users_db[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful!"}           










## Topic 5 . 

# How to upoad file through fastapi framework  



