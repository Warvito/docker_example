# Instructions
First pull the image with 
```
docker pull python:3.6-slim
```
In order to run a validation in a specific BIDS dataset, run the following command
```
docker run -v $PATH/TO/DATASET/ROOT:/dataset -v $PATH/TO/CODE/REPOSITORY:/project -v $PATH/TO/OUTPUT/FOLDER:/outputs python:3.6-slim "/bin/bash /project/bash_scripts/run_analysis.sh"
```
where *$PATH/TO/DATASET/ROOT* is the path to a BIDS dataset (for example could be */nfs/project/AMIGO/OASIS*), *$PATH/TO/CODE/REPOSITORY* is the path for this repository (for example */nfs/home/wds20/docker_example*),
 and *$PATH/TO/OUTPUT/FOLDER:/outputs* is where you want to store the outputs.
 
All of these volumes mounted inside the container (e.g. /dataset, /project, and /outputs) are being accessed by the scripts (e.g. run_analysis.sh and my_python_script.py)

example:
```
docker run -v ~/Desktop/docker_example:/dataset -v ~/Desktop/docker_example:/project -v ~/Desktop/docker_example:/outputs python:3.6-slim "/project/bash_scripts/run_analysis.sh"
```

NOTE: It might be necessary to change the the permissions of the run_analysis.sh. If you get any error related, try chmod 755 run_analysis.sh