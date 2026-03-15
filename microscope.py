from datetime import datetime
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




from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os


SCOPES = ['https://www.googleapis.com/auth/drive.file']




def upload_to_drive(file_path):
   flow = InstalledAppFlow.from_client_secrets_file(
       'credentials.json', SCOPES
   )


   creds = flow.run_local_server(port=0)


   service = build('drive', 'v3', credentials=creds)


   file_metadata = {
       'name': os.path.basename(file_path)
   }


   media = MediaFileUpload(file_path, resumable=True)


   file = service.files().create(
       body=file_metadata,
       media_body=media,
       fields='id'
   ).execute()


   print("Uploaded file ID:", file.get('id'))




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
   # Display image
   # cv2.imshow("Saved Image", frame)
   # cv2.waitKey(0)
   # cv2.destroyAllWindows()
   # print("immediate")
   upload_to_drive(output_path)




save_image()
print("immediate2")



