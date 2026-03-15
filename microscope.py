import cv2

# for i in range(6):
#     cap = cv2.VideoCapture(i)
#     opened = cap.isOpened()
#     ok, frame = cap.read()
#     shape = None if frame is None else frame.shape
#     print(f"index={i} opened={opened} read_ok={ok} frame_shape={shape}")
#     cap.release()


# streaming
# import cv2

# cap = cv2.VideoCapture(0)  # try 0, 1, 2...
# if not cap.isOpened():
#     raise RuntimeError("Could not open camera")

# while True:
#     ok, frame = cap.read()
#     if not ok:
#         break

#     cv2.imshow("Microscope", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()




import cv2

output_path = "microscope_capture.jpg"

cap = cv2.VideoCapture(0)  # try 0, 1, 2...
if not cap.isOpened():
    raise RuntimeError("Could not open camera")

# Grab a single frame
ok, frame = cap.read()
cap.release()

if not ok:
    raise RuntimeError("Could not read frame from camera")

# Save to disk
cv2.imwrite(output_path, frame)

# Load it back from disk
img = cv2.imread(output_path)
if img is None:
    raise RuntimeError(f"Could not load saved image: {output_path}")

# Display the saved image
cv2.imshow("Saved Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()