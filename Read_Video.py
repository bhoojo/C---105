import cv2
vid = cv2.VideoCapture("AnthonyShkraba.mp4")
if (vid.isOpened()==False):
    print("Open Camera")
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)
vid.release()
cv2.destroyAllWindows()