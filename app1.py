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

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/train")
async def trainRouteClient(request: Request, file: UploadFile = File(...), columns: str = Form(...)):
    try:
        # Read and process the file
        contents = await file.read()
        
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        df = df.head(100)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")

        # Parse column headings into a list
        #column_headings = columns.split(',')
        #print(column_headings)

        data = datavalidation()
        df_dropped = data.intiatedatavalidation(columns)


        print("hiiiiiiiiiii")  # Pass the list of column headings
        barp="plots/barplots"
        if  os.path.exists(barp):

            shutil.rmtree(barp)
       
        os.makedirs(barp)
        #barplot_images = os.listdir("plots/barplots")
        barp1="plots/cplots"
        barp2="plots/ccplots"
        barp3="plots/cccplots"
        barp4="plots/ccccplots"
        barp5="plots/cccccplots"
        barp6="plots/ccccccplots"
        barp7="plots/cccccccplots"
        barp8="plots/boxplots"


        print("rithinkumar")
        if os.path.exists(barp1):
            shutil.rmtree(barp1)
        os.makedirs(barp1)
        #barplot_images = os.listdir("plots/cplots")
        if os.path.exists(barp2):
            shutil.rmtree(barp2)
        os.makedirs(barp2)
        if os.path.exists(barp3):
            shutil.rmtree(barp3)
        os.makedirs(barp3)
        #os.makedirs(barp4)
        if os.path.exists(barp4):
            shutil.rmtree(barp4)
        os.makedirs(barp4)
        if os.path.exists(barp5):
            shutil.rmtree(barp5)
        os.makedirs(barp5)
        if os.path.exists(barp6):
            shutil.rmtree(barp6)
        os.makedirs(barp6)
        if os.path.exists(barp7):
            shutil.rmtree(barp7)
        os.makedirs(barp7)
        if os.path.exists(barp8):
            shutil.rmtree(barp8)
        os.makedirs(barp8)
        #barplot_images = os.listdir("plots/ccplots")
        print("dddddddddddd")
        print(df_dropped)
        data.create_barplots(df_dropped)
        print(df_dropped)
        print("sssssssssss")
        data.create_cbarplots(df_dropped)
        data.create_ccbarplots(df_dropped)
        data.create_cccbarplots(df_dropped)
        data.create_ccccbarplots(df_dropped)
        data.create_cccccbarplots(df_dropped)
        data.create_ccccccbarplots(df_dropped)
        data.create_cccccccbarplots(df_dropped)
        data.create_boxplots(df_dropped)


        
        print("eeeeeeeeeeeeeeee")
        
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        
        df_dropped.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
       

        #if os.path.exists(barp):
        #    shutil.rmtree(barp)

        
        #image_paths = [f"/plots/barplots/{img}" for img in barplot_images]

        image_paths = os.listdir(barp)
        image_data = []
        for img_path in image_paths:
            with open(f"{barp}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data.append(b64_string)
        image_paths1 = os.listdir(barp1)
        image_data1 = []
        for img_path in image_paths1:
            with open(f"{barp1}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data1.append(b64_string)
        image_paths2 = os.listdir(barp2)
        image_data2 = []
        for img_path in image_paths2:
            with open(f"{barp2}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data2.append(b64_string)
        image_paths3 = os.listdir(barp3)
        image_data3 = []
        for img_path in image_paths3:
            with open(f"{barp3}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data3.append(b64_string)
        image_paths4 = os.listdir(barp4)
        image_data4 = []
        for img_path in image_paths4:
            with open(f"{barp4}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data4.append(b64_string)
        image_paths5 = os.listdir(barp5)
        image_data5 = []
        for img_path in image_paths5:
            with open(f"{barp5}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data5.append(b64_string)
        image_paths6 = os.listdir(barp6)
        image_data6 = []
        for img_path in image_paths6:
            with open(f"{barp6}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data6.append(b64_string)
        image_paths7 = os.listdir(barp7)
        image_data7 = []
        for img_path in image_paths7:
            with open(f"{barp7}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data7.append(b64_string)
        image_paths8 = os.listdir(barp8)
        image_data8 = []
        for img_path in image_paths8:
            with open(f"{barp8}/{img_path}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data8.append(b64_string)
        


    # Send back the image data as base64
        #print(image_data2)
        return JSONResponse(content={"images": image_data,'images1':image_data1,'images2':image_data2,'images3':image_data3,'images4':image_data4,'images5':image_data5,'images6':image_data6,'images7':image_data7,'images8':image_data8}, status_code=200)
    except Exception as e:
        # Return JSON with error message
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
