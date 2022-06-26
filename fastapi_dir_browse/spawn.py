import os
from pathlib import Path


def spawn():
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
#spawn()