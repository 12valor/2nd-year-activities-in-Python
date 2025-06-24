import cv2

# Load the pre-trained MobileNet SSD model for object detection
net = cv2.dnn.readNetFromCaffe(
    "https://github.com/chuanqi305/MobileNet-SSD/raw/master/deploy.prototxt",
    "https://github.com/chuanqi305/MobileNet-SSD/raw/master/mobilenet_iter_73000.caffemodel"
)

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert the image to a blob
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)

    # Perform object detection
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            idx = int(detections[0, 0, i, 1])
            if idx == 84:  # Class ID for 'book' in COCO dataset
                cv2.putText(frame, "📖 Book Detected!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the video feed
    cv2.imshow("Book Detector", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
