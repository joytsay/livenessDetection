::python gather_examples.py -i ./videos/joyFake.mp4 -o ./dataset/fake -d ./face_detector -c 0.9 -s 1 -f 0
::PAUSE
::python gather_examples.py -i ./videos/joyReal.mp4 -o ./dataset/real -d ./face_detector -c 0.9 -s 1 -f 0
::PAUSE
python gather_examples.py -i output.mp4 -o ./dataset/fake -d ./face_detector -c 0.9 -s 1 -f 0
PAUSE