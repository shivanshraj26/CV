import cv2
# Path to your image file
image_path = 'me.jpg'
# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Load the pre-trained Haarcascades face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

    # Check if faces are detected
    if len(faces) > 0:
        print("Human face detected!")
    else:
        print("No human face detected.")

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Resize the image for better visibility
    resized_image = cv2.resize(image, (800, 600))

    # Display the original image with faces highlighted
    cv2.imshow('Detected Faces', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()