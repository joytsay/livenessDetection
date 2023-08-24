call conda.bat activate
call conda create -n liveness python=3.8
call conda activate liveness
call pip install -r requirements.txt
PAUSE