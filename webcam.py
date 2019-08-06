import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640,480))

while(True):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()