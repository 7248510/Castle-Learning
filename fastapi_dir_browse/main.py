#uvicorn main:app --reload
import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from spawn import spawn

def generate():
    # This is only used for refreshing after a request. The plan is to use this in a C2
    path = "cars"
    dir_list = os.listdir(path)
    f = open("templates/cars.html", "w")
    f.write("<!DOCTYPE html>" + "\n")
    track = 0
    for x in dir_list:
        holder = dir_list[track].rsplit(".", 1 )[0]   
        content = '<a href="/cars/'+dir_list[track]+'">'+holder+"</a>" + "<br>"
        track +=1
        f.write(content)
    f.write("</html>" + "\n")
    f.close()
    #print("Completed")



def init():
    templateDir = "templates"
    if len(os.listdir(templateDir)) == 0:
        spawn()
    else:
        print("Already populated")



init()
app = FastAPI()



app.mount("/cars", StaticFiles(directory="cars"), name="cars")
templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #generate() #This is only to refresh the file/folder upon a request
    return templates.TemplateResponse("cars.html", {"request": request})
