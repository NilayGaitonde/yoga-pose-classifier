import cv2
import numpy as np
from persondetection import check_objs,load_yolo, draw_boxes
from yogaClassifier import classify_yoga_pose, load_yoga_model
import mediapipe as mp


vid = cv2.VideoCapture(1)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('op/output.mp4', fourcc, 30.0, (640, 480))
model=load_yolo()
yoga_model = load_yoga_model(3)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
while True:
    ret, frame = vid.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # fps = vid.get(cv2.CAP_PROP_FPS)
    # h, w = frame.shape[:2]
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # keypoints = pose.process(image)
    classification,score = classify_yoga_pose(model=yoga_model,img=frame)
    results=check_objs(model=model,image=frame,n_classes=1)
    # out.write(frame)
    frame = draw_boxes(model, frame, results,classification,score)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()