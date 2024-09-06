from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import pandas as pd
from io import StringIO
import os
from src.components.datavavalidation import datavalidation
from src.components.clustering import Clustering
from fastapi.middleware.cors import CORSMiddleware
import shutil
import cv2
from pymongo.mongo_client import MongoClient
from src.components.modeltraining1 import modeltrainerclass
from src.components.datavisualization import datavisualizations


import numpy as np
import base64
from PIL import Image
from io import BytesIO

app = FastAPI()

# Setup static file serving
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/plots", StaticFiles(directory="plots"), name="plots")  # Mount plots directory for serving images

# Setup template rendering
templates = Jinja2Templates(directory="templates")
uri = "mongodb+srv://rithin:076ecHwHg60yETd9@cluster0.ctrleyy.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    # Confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Could not connect to MongoDB: {e}")

# Create or access the database and collection
db_1 = client['dataanalys']

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/train")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/barplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_barplots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
@app.post("/train1")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/hplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_histplots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/train2")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/h2plots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_hist2plots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/train3")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/boxplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_boxplots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/train4")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/heatplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_heatplots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/train5")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/countplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_countplots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/train6")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/pieplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_piechart(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/train7")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/scplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_scatterplots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/train8")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/sc2plots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_scatter2plots(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/train9")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        
        contents = await file.read()
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        #df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavisualizations()
        df_dropped = data.intiatedatavalidation(columns)
        barp="plots/boxplots2"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
        os.makedirs(barp)
        data.create_boxplots2(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            if img_path.lower().endswith('.png'):
                with open(os.path.join(barp, img_path), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                    image_data.append(b64_string)
        return JSONResponse(content={"images": image_data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/dataanalysis")
async def trainRouteClient(request: Request, file: UploadFile = File(...)):
    try:
       
        contents = await file.read()
        
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        
        data_dir = 'data'
        
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        df.to_csv("data/data.csv")
        df.isnull().sum()
            
            
        df=df.dropna()
        
        df = df.drop_duplicates()
        #data = datavalidation()
        #data = data.intiatedatavalidation(columns)
        data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        collection = db_1['dataanalyscollection']  # Replace with your desired collection name
        collection.delete_many({})  # This clears all documents in the collection
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")

        head = df.to_dict(orient='records')
        return JSONResponse(content={"data": head}, status_code=200)
       
        #return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
def export_collection_as_dataframe(collection_name: str, database_name: str) -> pd.DataFrame:
    try:
        collection = client[database_name][collection_name]
        df = pd.DataFrame(list(collection.find()))
        if "_id" in df.columns:
            df = df.drop(columns=["_id"], axis=1)
        df.replace({"na": np.nan}, inplace=True)
        return df
    except Exception as e:
        print(f"Error exporting collection to DataFrame: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if there's an error

db_name = 'dataanalys'
collection_name = 'dataanalyscollection'
@app.post("/dataanalysis1")
async def trainRouteClient(request: Request, columns: str = Form(...)):
    try:
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        
        
       
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        data = datavalidation()
        df = data.intiatedatavalidation(columns)
        print("output+++++++++++")
        print(df)
        data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        collection = db_1['dataanalyscollection1']  # Replace with your desired collection name
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
        head = df.to_dict(orient='records')
        
        return JSONResponse(content={"data": head}, status_code=200)
       
        #return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
@app.post("/dataanalysis1n")
async def trainRouteClient(request: Request, columns: str = Form(...), dataty: str = Form(...)):
    try:
        print('start')
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")
        
        data = datavalidation()
        print('end')
        df = data.intiatedatavalidationn(columns, dataty)
        print("output+++++++++++")

        # Convert datetime columns to string if necessary
        
        

#

# Convert the data types DataFrame to a dictionary
        head = df.to_dict(orient='records')
        print('all')
        d = {'all': 'updated'}
        #print(head)
        return JSONResponse(content={"data": head}, status_code=200)

    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
@app.post("/dataanalysis2")
async def trainRouteClient(columns1: str = Form(...)):
    try:
        # Export data from MongoDB to DataFrame
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        # Save the DataFrame to a CSV file
        data_dir = 'data1'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv(os.path.join(data_dir, "data.csv"), index=False)

        # Validate data and find unique values
        data_validation = datavalidation()  # Assuming datavalidation() is an instance that provides checkuniquevalues
        unique_values = data_validation.checkuniquevalues(columns1)
        print("Unique values output:", unique_values)

        # Insert the original data into MongoDB collection
        collection = db_1['dataanalyscollection']  # Ensure this collection is correctly defined in your DB
        data = df.to_dict(orient='records')
        collection.delete_many({})  # Optional: Clear the collection before inserting new data
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")

        # Return the unique values as JSON response
        return JSONResponse(content={"data": unique_values}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/dataanalysis6")
async def trainRouteClient(columns11: str = Form(...),columns111 = Form(...),orand1=Form(...),dataty1=Form(...)):
    try:
        # Export data from MongoDB to DataFrame
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        # Save the DataFrame to a CSV file
        data_dir = 'filter'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv(os.path.join(data_dir, "data.csv"), index=False)
        print(type(columns111))
        
        print(columns11,columns111)
        # Validate data and find unique values
        data_validation = datavalidation()  # Assuming datavalidation() is an instance that provides checkuniquevalues
        df = data_validation.filter(columns11,columns111,orand1,dataty1)
        

        # Insert the original data into MongoDB collection
          # Ensure this collection is correctly defined in your DB
        data = df.to_dict(orient='records')
        
        
        print('datasending',data)

        # Return the unique values as JSON response
        return JSONResponse(content={"data": data}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/dataanalysis7")
async def trainRouteClient(columns1a: str = Form(...),columns1b = Form(...),columns2a: str = Form(...),columns2b = Form(...),orand=Form(...),dataty=Form(...)):
    try:
        # Export data from MongoDB to DataFrame
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)
        print(df)
        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        # Save the DataFrame to a CSV file
        data_dir = 'filter2'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv(os.path.join(data_dir, "data.csv"), index=False)
        print("rrrrr")
    
        print(columns1a,columns1b,columns2a,columns2b,orand,dataty)
        print(type(columns1b))
        
        # Validate data and find unique values
        data_validation = datavalidation()  # Assuming datavalidation() is an instance that provides checkuniquevalues
        df = data_validation.filter2(columns1a,columns1b,columns2a,columns2b,orand,dataty)
        

        # Insert the original data into MongoDB collection
          # Ensure this collection is correctly defined in your DB
        data = df.to_dict(orient='records')
        
        
        print('datasending',data)

        # Return the unique values as JSON response
        return JSONResponse(content={"data": data}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/dataanalysis3")
async def trainRouteClient(request: Request):
    try:
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        
        
       
        data_dir = 'describe'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("describe/describe.csv")
        data = datavalidation()
        df = data.describe()
        print("output+++++++++++")
        print(df)
        data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        collection = db_1['dataanalyscollection2']  # Replace with your desired collection name
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
        head = df.to_dict(orient='records')
        
        return JSONResponse(content={"data": head}, status_code=200)
       
        #return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/dataanalysis4")
async def trainRouteClient(request: Request):
    try:
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        
        
       
        data_dir = 'info'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("info/info.csv")
        data = datavalidation()
        df = data.info()
        print("output+++++++++++")
       # print(df)
        #data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        #collection = db_1['dataanalyscollection4']  # Replace with your desired collection name
        #result = collection.info(data)
        #print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
        head = df.to_dict(orient='records')
        print(head)
        return JSONResponse(content={"data": head}, status_code=200)
       
        #return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/dataanalysis5")
async def trainRouteClient(request: Request):
    try:
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)

        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)

        
        
       
        df=df[df.duplicated()]
        
        print("output+++++++++++")
       # print(df)
        #data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        #collection = db_1['dataanalyscollection4']  # Replace with your desired collection name
        #result = collection.info(data)
        #print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
        head = df.to_dict(orient='records')
        print(head)
        return JSONResponse(content={"data": head}, status_code=200)
       
        #return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)


#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

@app.post("/modeltrainingdata")
async def trainRouteClient(request: Request, file: UploadFile = File(...)):
    try:
       
        contents = await file.read()
        
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        
        data_dir = 'modeldata'
        
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        df.to_csv("modeldata/data.csv")
        df.isnull().sum()
            
            
        df=df.dropna()
        
        df = df.drop_duplicates()
        #data = datavalidation()
        #data = data.intiatedatavalidation(columns)
        data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        collection = db_1['modeltrainingcollection']  # Replace with your desired collection name
        collection.delete_many({})  # This clears all documents in the collection
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
        df=df.head(10)
        head = df.to_dict(orient='records')
        return JSONResponse(content={"data": head}, status_code=200)
       
        #return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        # Return JSON with error message
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/modeltraining")
async def trainRouteClient(col1: str = Form(...),col2 = Form(...),col3: str = Form(...),col4 = Form(...)):
    try:
        # Export data from MongoDB to DataFrame
        print(col1,col2,col3,col4)
        collection_name='modeltrainingcollection'
        db_name='dataanalys'
        df = export_collection_as_dataframe(collection_name=collection_name, database_name=db_name)
        print(df)
        if df.empty:
            return JSONResponse(content={"error": "No data found in MongoDB collection"}, status_code=404)
        print('ddddo')
        n=modeltrainerclass()
        print('eoooooo')
        df,df1=n.trainmodel(df,col1,col2,col3,col4)
        
        data = df.to_dict(orient='records')
        data1 = df1.to_dict(orient='records')
        print('hhhhh')
        print(data)
        print('yyyy')
        print(data1)
        
        
        

        # Return the unique values as JSON response
        return JSONResponse(content={"data": data,"data1":data1}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)