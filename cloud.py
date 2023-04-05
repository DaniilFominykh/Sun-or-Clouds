import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshold_value = 150
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    num_white_pixels = cv2.countNonZero(binary)
    total_pixels = binary.shape[0] * binary.shape[1]
    white_pixel_percentage = num_white_pixels / total_pixels

    if white_pixel_percentage > 0.2:
        print("It's cloudy.")
    else:
        print("Sun.")

    cv2.imshow('Binary', binary)
    key = cv2.waitKey(1)
    if key == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()