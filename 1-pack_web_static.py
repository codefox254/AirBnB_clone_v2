#!/usr/bin/env python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder """

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")  # Current date and time
    archive_path = "versions/web_static_{}.tgz".format(date_time)
    
    try:
        local("mkdir -p versions")  # Create the versions directory if it doesn't exist
        local("tar -cvzf {} web_static".format(archive_path))  # Create archive
        return archive_path
    except Exception as e:
        return None

if __name__ == "__main__":
    do_pack()

