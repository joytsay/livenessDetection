call conda.bat activate
call conda activate liveness
python train_liveness.py -d ./dataset -m liveness.model -l le.pickle
PAUSE