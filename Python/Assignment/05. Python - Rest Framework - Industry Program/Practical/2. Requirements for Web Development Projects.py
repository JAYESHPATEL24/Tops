# 2) Write a Python script to set up a Django project and install packages like django, djangorestframework, requests, etc.:

#    - **Overview**:
#      - This script automates the creation of a new Django project and installs necessary packages using `pip`.

#    **Python Script**:
import os
import subprocess

def setup_django_project(project_name):
    try:
        print(f"Setting up Django project: {project_name}")

        # Step 1: Create a virtual environment
        print("Creating a virtual environment...")
        subprocess.run(["python", "-m", "venv", "env"], check=True)

        # Step 2: Activate the virtual environment
        activate_command = "env\\Scripts\\activate" if os.name == "nt" else "source env/bin/activate"
        print(f"Activating virtual environment: {activate_command}")

        # Step 3: Install required packages
        print("Installing required packages...")
        packages = ["django", "djangorestframework", "requests"]
        subprocess.run([f"{activate_command} && pip install " + " ".join(packages)], shell=True, check=True)

        # Step 4: Create a Django project
        print(f"Creating Django project: {project_name}...")
        subprocess.run([f"{activate_command} && django-admin startproject {project_name}"], shell=True, check=True)

        print(f"Django project '{project_name}' setup successfully!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")




project_name = "myproject"  
setup_django_project(project_name)
