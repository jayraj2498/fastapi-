# Uploading files with FastAPI is quite simple and allows handling various types of files, 
# such as images, documents, or data files. FastAPI also supports validating file types, sizes, and more. 
# Here are some examples, starting with a basic file upload and then moving on to a more real-life example. 



# Example 1: Basic File Upload
# This example shows a simple file upload, where you can upload a file, and FastAPI will read it and provide its metadata in the response.


from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size": len(await file.read())
    }


# Example 2: Save the Uploaded File (Real-life Use Case) Like uploda Images 
# In real applications, you might want to save the uploaded file to a specific folder for later use. 
# Here’s an example where we upload an image, save it to a directory, and respond with the file path. 


from fastapi import FastAPI, File, UploadFile
import shutil
# import os

# app = FastAPI()

# # Directory to save files
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create directory if it doesn't exist

# @app.post("/upload-image/")
# async def upload_image(file: UploadFile = File(...)):
#     file_path = os.path.join(UPLOAD_DIR, file.filename)
    
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)  # Save file to disk
#     return {"file_path": file_path, "message": "File uploaded successfully"}


from fastapi import FastAPI , File , UploadFile 
import shutil
import os   

app = FastAPI() 

# Directory to save files
UPLOAD_DIR = "uploads" 
os.makedirs(UPLOAD_DIR, exist_ok=True) 

@app.post("/uploaded-images/") 
async def upload_ur_image(files: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, files.filename)
    
    # Save file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(files.file, buffer)
    
    return {"Your_file_path": file_path, "message": "File is uploaded successfully"}




# Example 3: Upload and Process a CSV File 
# Suppose you’re working with data science or analytics. A typical task is uploading a CSV file to analyze or process
# the data. Here’s how to handle a CSV file upload and read its contents.

from fastapi import FastAPI, File, UploadFile
import pandas as pd 
import io



app = FastAPI()

# @app.post("/upload-csv/")
# async def upload_csv(file: UploadFile = File(...)):
#     if file.content_type != 'text/csv':
#         return {"error": "File must be a CSV"}
    
#     # Read the CSV file using pandas
#     contents = await file.read()
#     data = pd.read_csv(io.StringIO(contents.decode('utf-8')))

#     # Example: return basic information about the data
#     return {
#         "columns": data.columns.tolist(),
#         "rows": len(data),
#         "sample_data": data.head().to_dict()  # Returns the first few rows as a dictionary
#     } 
    
    
@app.post("/csv_upload/") 
async def upload_csv_file(file :UploadFile=File(...)) :
    if file.content_type != "text/csv" :
        return {"error":"your File must have be CSV only "} 
    
    # read csv file usin pandas 
    contents = await file.read() 
    data = pd.read_csv(io.StringIO(contents.decode("utf-8"))) 
    
    return{ 
           "columns" : data.columns.tolist()  , 
           "len of rows  ":len(data) , 
           "sample_data": data.head().to_dict(orient="records")}

 
 
 
# Example 4: Secure File Upload with Image Validation
# In cases where only specific file types (e.g., images) should be allowed, 
# this example shows how to restrict the file type and validate the image size. 

from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io

app = FastAPI()

# @app.post("/upload-image-secure/")
# async def upload_image_secure(file: UploadFile = File(...)):
#     if file.content_type not in ["image/jpeg", "image/png"]:
#         raise HTTPException(status_code=400, detail="Only JPEG and PNG images are allowed")
    
#     # Validate image size
#     image = Image.open(io.BytesIO(await file.read()))
#     if image.width > 1920 or image.height > 1080:
#         raise HTTPException(status_code=400, detail="Image too large. Maximum allowed dimensions are 1920x1080.")

#     return {"filename": file.filename, "message": "Image uploaded and validated successfully"} 




from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io
import os

app = FastAPI()

# # Define the folder path where images will be saved
# UPLOAD_FOLDER = "uploaded_images"

# # Ensure the folder exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.post("/upload-image-secure/")
# async def upload_image_secure(file: UploadFile = File(...)):
#     # Check file type
#     if file.content_type not in ["image/jpeg", "image/png"]:
#         raise HTTPException(status_code=400, detail="Only JPEG and PNG images are allowed")
    
#     # Validate image size
#     image = Image.open(io.BytesIO(await file.read()))
#     if image.width > 1920 or image.height > 1080:
#         raise HTTPException(status_code=400, detail="Image too large. Maximum allowed dimensions are 1920x1080.")
    
#     # Save the image
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     image.save(file_path)

#     return {"filename": file.filename, "message": "Image uploaded, validated, and saved successfully"}





# ----------------------------------------------------------------------------------

# Example: Uploading a Document, Profile Image, and User's Name Together 


from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from typing import Optional
from PIL import Image
import io

app = FastAPI()

@app.post("/upload/")
async def upload_file(
    name: str = Form(...), 
    document: UploadFile = File(...), 
    profile_image: UploadFile = File(...)
):
    # Validate that the profile image is either JPEG or PNG
    if profile_image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Profile image must be in JPEG or PNG format")

    # Check and validate document file type if needed
    if document.content_type not in ["application/pdf", "text/csv"]:
        raise HTTPException(status_code=400, detail="Only PDF documents are allowed")

    # Read and save the profile image to the server (optional)
    image = Image.open(io.BytesIO(await profile_image.read()))
    if image.width > 1920 or image.height > 1080:
        raise HTTPException(status_code=400, detail="Image too large. Maximum allowed dimensions are 1920x1080.")
    
    # Optional: Save image or document locally
    with open(f"{profile_image.filename}", "wb") as f:
        f.write(await profile_image.read())

    with open(f"{document.filename}", "wb") as f:
        f.write(await document.read())
    
    return {
        "name": name,
        "document_filename": document.filename,
        "profile_image_filename": profile_image.filename,
        "message": "Files and information uploaded successfully!"
    }