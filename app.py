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
        print(columns)
        content_str = contents.decode('utf-8')
        df = pd.read_csv(StringIO(content_str))
        df = df.head(10)
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        df.to_csv("data/data.csv")

        # Parse column headings into a list
        #column_headings = columns.split(',')
        #print(column_headings)

        data = datavalidation()
        df_dropped = data.intiatedatavalidation(columns)  # Pass the list of column headings
        barp="plots/barplots"
        if not os.path.exists(barp):
            os.makedirs(barp)
        barplot_images = os.listdir("plots/barplots")
        barp1="plots/cplots"
        if not os.path.exists(barp1):
            os.makedirs(barp1)
        barplot_images = os.listdir("plots/cplots")
        print("dddddddddddd")
        print(df_dropped)
        data.create_barplots(df_dropped)
        print("sssssssssss")
        data.create_cbarplots(df_dropped)

        clustering = Clustering()
        print("eeeeeeeeeeeeeeee")
        optimal_clusters = clustering.elbow_plot(df_dropped)
        dropped_dir = 'droped'
        if not os.path.exists(dropped_dir):
            os.makedirs(dropped_dir)
        df_with_clusters = clustering.create_clusters(df_dropped, optimal_clusters)
        df_with_clusters.to_csv(f"{dropped_dir}/data_with_clusters.csv", index=False)
       

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

    # Send back the image data as base64
        return JSONResponse(content={"images": image_data,'images1':image_data1}, status_code=200)
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
