from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import FastAPI, UploadFile, File,Form
from fastapi.responses import JSONResponse
import pandas as pd
from io import StringIO
import os
from src.components.datavavalidation import datavalidation

app = FastAPI()

# Setup static file serving
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup template rendering
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/train")
async def trainRouteClient(
    file: UploadFile = File(...),
    columns: str = Form(...)
):
    try:
        # Read the file content
        contents = await file.read()
        content_str = contents.decode('utf-8')
        
        # Use StringIO to read the string as a CSV file
        df = pd.read_csv(StringIO(content_str))
        
        # Create directory if it doesn't exist
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # Save the DataFrame to a CSV file
        df.to_csv("data/data.csv", index=False)
        
        # Optionally process columns
        column_list = [col.strip() for col in columns.split(',')]
        print("Columns to process:", column_list)
        
        # Drop specified columns from DataFrame
        dropped_columns = [col for col in column_list if col in df.columns]
        df_dropped = df.drop(columns=dropped_columns, errors='ignore')
        
        # Save the modified DataFrame
        df_dropped.to_csv("data/data_dropped.csv", index=False)
        
        # Return the dropped columns and the first 5 rows of the modified DataFrame
        return {
            "message": "Training initiated with uploaded CSV.",
            "dropped_columns": dropped_columns,
            "data_head": df_dropped.head().to_dict()
        }
    
    except Exception as e:
        return JSONResponse(content={"error": f"An error occurred: {str(e)}"})
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
