from fastapi import FastAPI
import os
from fastapi.responses import FileResponse
from src.analysis import data
from src.viz import plot_average_duration


app = FastAPI()

@app.get('/average-duration')
def Average_Duration():
    plot_average_duration(data)
    
    image_path = './images/average_duration.png'
    
    if os.path.exists(image_path):
        return FileResponse(image_path,media_type = 'image/png')
    
    return {"Message": "Average Duration Plot Generated and Saved in the images folder."}
