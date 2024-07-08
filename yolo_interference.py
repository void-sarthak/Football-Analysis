from ultralytics import YOLO

model = YOLO('models/best.pt', 'device = 0')

results = model.predict('input_videos/video2.mp4', save = True)
print(results[0])
print('========================')
for box in results[0].boxes:
    print(box)
