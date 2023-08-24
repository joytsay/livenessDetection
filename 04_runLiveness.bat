call conda.bat activate
call conda activate liveness
python liveness_demo.py -m liveness.model -l le.pickle -d ./face_detector -c 0.5
PAUSE