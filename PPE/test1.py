from ultralytics import YOLO
import cv2
import time


safety = ['Glass', 'Helmet', 'Safety-Vest', 'Safety-Boots', 'Gloves']
model = YOLO('yolov8s_custom.pt')

cap = cv2.VideoCapture('2.mp4')  
#cap = cv2.VideoCapture(0)  

last_check_time = time.time()
conf=0.85
 

def gen(item):

  if item=='Glass':
    i=0
  if item=='Helmet':
    i=1
  if item=='Safety-Vest':
    i=2
  if item=='Safety-Boots':
    i=3
  if item=='Gloves':
    i=4  

  # while(cap.isOpened()):
  _, frame = cap.read()

  start_time = time.time()
  results = model(frame, verbose=False)
  detected_items = set()
  
  person_count = 0

  for r in results:
    for c in r.boxes:
      class_name = model.names[int(c.cls)]
      conf_score = float(c.conf)
      x1, y1, x2, y2 = map(int, c.xyxy[0])

      if conf_score > conf:
        cs = conf_score * 100
        print(class_name, cs)

        if class_name == "Person":
          person_count += 1
        if class_name in safety:
          if class_name in safety[i]:
              detected_items.add(class_name)
              cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 55, 255), 2)
              cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
              cv2.putText(frame, str(cs), (x1 + 150, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

  missing_items = [item for item in safety if item not in detected_items]

  for item in missing_items:
    print(f"Missing: {item}")

  end_time = time.time()
  fps = 1 / (end_time - start_time)

  cv2.putText(frame, f"FPS: {int(fps)}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
  cv2.putText(frame, f"People: {person_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
  for item in detected_items:
    print(f"Detected: {item}")

  frame = cv2.imencode('.jpg', frame)[1].tobytes()
  yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



  cap.release()
  cv2.destroyAllWindows()
  return {'done': True} 




def genall():

  # while(cap.isOpened()):
  _, frame = cap.read()

  start_time = time.time()
  results = model(frame, verbose=False)
  detected_items = set()
  
  person_count = 0

  for r in results:
    for c in r.boxes:
      class_name = model.names[int(c.cls)]
      conf_score = float(c.conf)
      x1, y1, x2, y2 = map(int, c.xyxy[0])

      if conf_score > conf:
        cs = conf_score * 100
        print(class_name, cs)

        if class_name == "Person":
          person_count += 1
        if class_name in safety:
              detected_items.add(class_name)
              cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 55, 255), 2)
              cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
              cv2.putText(frame, str(cs), (x1 + 150, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

  missing_items = [item for item in safety if item not in detected_items]

  for item in missing_items:
    print(f"Missing: {item}")

  end_time = time.time()
  fps = 1 / (end_time - start_time)

  cv2.putText(frame, f"FPS: {int(fps)}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
  cv2.putText(frame, f"People: {person_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
  for item in detected_items:
    print(f"Detected: {item}")

  frame = cv2.imencode('.jpg', frame)[1].tobytes()
  yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



  cap.release()
  cv2.destroyAllWindows()
  return {'done': True}  


