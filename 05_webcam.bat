call conda.bat activate
call conda activate liveness
python webcam.py -m liveness.model -l le.pickle -d ./face_detector -c 0.5