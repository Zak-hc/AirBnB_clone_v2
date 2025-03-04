#!/usr/bin/python3
# fab
"""im the fab-__-"""


from fabric.api import *
from datetime import datetime


@task
def do_pack():
    """loool"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    mkdir = "mkdir -p versions"
    path = "/versions/web_static_{}.tgz".format(date)

    print("Packing web_static to", path)
    if local(
            "{} &&  tar -cvzf {}  web_static".format(mkdir, path)).succeeded:
        return path
        print("web_static packed: {} -> {} Bytes".format(path, size))
    else:
        return None
