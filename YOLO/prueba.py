from ultralytics import YOLO

model = YOLO("yolo26n.pt")


source = "https://omes-va.com/wp-content/uploads/2025/02/Datasets_720x405.jpg"

result = model(source)

print(result)
result[0].show()
