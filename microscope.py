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




# import cv2
# from datetime import datetime

# timestamp = datetime.now()
# timestamp_text = timestamp.strftime("%Y-%m-%d %H:%M:%S")
# output_path = "microscope_capture.jpg"

# cap = cv2.VideoCapture(0)  # try 0, 1, 2...
# if not cap.isOpened():
#     raise RuntimeError("Could not open camera")

# # Grab a single frame
# ok, frame = cap.read()
# cap.release()

# if not ok:
#     raise RuntimeError("Could not read frame from camera")

# # Put timestamp on the image
# cv2.putText(
#     frame,
#     timestamp_text,                 # text
#     (10, 30),                      # position: x, y
#     cv2.FONT_HERSHEY_SIMPLEX,      # font
#     1.0,                           # font scale
#     (255, 255, 255),               # color: white
#     2,                             # thickness
#     cv2.LINE_AA                    # smoother lines
# )

# # Save stamped image
# cv2.imwrite(output_path, frame)

# # Display stamped image
# img = cv2.imread(output_path)
# if img is None:
#     raise RuntimeError(f"Could not load saved image: {output_path}")

# cv2.imshow("Saved Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






import cv2
from datetime import datetime


def save_image():
    timestamp = datetime.now()
    timestamp_text = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    output_path = "microscope_capture.jpg"

    cap = cv2.VideoCapture(0)  # try 0, 1, 2...
    if not cap.isOpened():
        raise RuntimeError("Could not open camera")

    # Grab a single frame
    ok, frame = cap.read()
    cap.release()

    if not ok:
        raise RuntimeError("Could not read frame from camera")

    # Put timestamp on the image
    cv2.putText(
        frame,
        timestamp_text,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    # Save stamped image only
    success = cv2.imwrite(output_path, frame)
    if not success:
        raise RuntimeError(f"Could not save image: {output_path}")



save_image()