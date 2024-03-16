import os
import requests
import subprocess

# path from where the api will run
api_dir = '/mnt/shareddrive/Research/Thesis/Thesis/lingo_clustering/carrot2-4.5.3/dcs'
# Set the URL of the Carrot2 REST API
url = 'http://localhost:8080/service/cluster'

try:
    response = requests.post(url=url)
except requests.exceptions.ConnectionError:
    command_cd = f"cd {api_dir}"
    command_api = f"./dcs"
    # Combine the commands into a single command using && to run them sequentially
    combined_command = f"{command_cd} && {command_api}"
    
    # Create a subprocess for changing directory
    process_cd = subprocess.Popen(f"cd {api_dir}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the cd process to finish
    process_cd.wait()

    # Check if the cd process was successful
    if process_cd.returncode == 0:
        print("Changed directory successfully")

        # Create a subprocess for running the Java application
        process_api = subprocess.Popen(command_api, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the Java application process to finish
        process_api.wait()

        # Check if the Java application process was successful
        if process_api.returncode == 0:
            print("Java application executed successfully")
            print("Output:\n", process_api.stdout.read())
        else:
            print("Java application execution failed")
            print("Error:\n", process_api.stderr.read())
    else:
        print("Changing directory failed")
        print("Error:\n", process_cd.stderr.read())
