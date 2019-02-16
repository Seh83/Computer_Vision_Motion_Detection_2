import cv2
import numpy as np

# Read the video file / source
cap = cv2.VideoCapture(0)

# Capture the 1st & 2nd frames and store them in resp. variables:
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

# Loop the capture of frames:
while True:
    # Convert the frame1 & frame2 into gray scale to calculate differences:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Apply the Gaussian blur onto the gray scale frames
    # Kernel size is 21*21 which applies a stronger level of blurring:
    frame1_blur = cv2.GaussianBlur(frame1_gray, (21, 21), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

    # Calculate the difference between the two frames:
    frames_diff = cv2.absdiff(frame1_blur, frame2_blur)

    # Apply the threshhold too the frames_diff frame:
    thresh = cv2.threshold(frames_diff, 20, 255, cv2.THRESH_BINARY)[1]
    final = cv2.dilate(thresh, None, iterations=2)

    # Apply the mask:
    masked = cv2.bitwise_and(frame1, frame1, mask=thresh)

    white_pixels = np.sum(thresh) / 255
    rows, cols = thresh.shape
    total = rows * cols

    if white_pixels > 0.01 * total:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame1, 'Motion Detected', (10, 50),
                    font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the difference in an open window:
    cv2.imshow("Motion Captured:", frame1)

    # Repeat the same for the upcoming frames in the video:
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
