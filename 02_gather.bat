call conda.bat activate
call conda activate liveness
python gather_examples.py -i ./videos/fake.mp4 -o ./dataset/fake -d ./face_detector -c 0.9 -s 1 -f 0
python gather_examples.py -i ./videos/real.mp4 -o ./dataset/real -d ./face_detector -c 0.9 -s 1 -f 0
PAUSE