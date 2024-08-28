from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
from io import StringIO
import os

app = FastAPI()

# Setup static file serving
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup template rendering
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/train")
async def trainRouteClient(file: UploadFile = File(...)):
    try:
        # Read the file content
        contents = await file.read()
        # Convert byte content to string
        content_str = contents.decode('utf-8')
        print("+++++++")
        print(content_str)
        print("+++++++")
        # Use StringIO to read the string as a CSV file
        df = pd.read_csv(StringIO(content_str))

        # Get the first 5 rows of the DataFrame
        head = df.head()
        
        # Return the DataFrame head as JSON
        print(head)
        

    except Exception as e:
        return JSONResponse(content={"error": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
