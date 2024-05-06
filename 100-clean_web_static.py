#!/usr/bin/env python3
"""Fabric script that distributes an archive to web servers"""

from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = ['54.90.29.192', '100.26.253.115']  # Replace with your server IPs

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")  # Current date and time
    archive_path = f"versions/web_static_{date_time}.tgz"

    try:
        local("mkdir -p versions")  # Create the versions directory if it doesn't exist
        local(f"tar -cvzf {archive_path} web_static")  # Create archive
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Distribute an archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Define the release directory path and the archive filename without extension
        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        release_path = f'/data/web_static/releases/{folder_name}'

        # Uncompress the archive to the release folder
        run(f'mkdir -p {release_path}')
        run(f'tar -xzf /tmp/{filename} -C {release_path}')

        # Delete the archive from the web server
        run(f'rm /tmp/{filename}')

        # Delete the symbolic link to the current release
        run('rm -f /data/web_static/current')

        # Create a new symbolic link to the new release
        run(f'ln -s {release_path} /data/web_static/current')

        return True
    except Exception as e:
        return False

def deploy():
    """
    Deploy the web_static content to the servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)

def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    if number < 2:
        number = 1  # Keep at least the most recent version

    try:
        local("ls -t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))
        run("ls -t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    success = deploy()
    if success:
        print("Deployment successful!")
        do_clean(2)  # Clean up old archives (keep 2 most recent versions)
    else:
        print("Deployment failed.")

