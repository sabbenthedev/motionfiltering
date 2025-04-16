import cv2 as cv

# input video
video = cv.VideoCapture("movement.mp4")

# get frame size and fps from input video
frame_width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv.CAP_PROP_FPS))

# creating videowriter object for mp4 output
fourcc = cv.VideoWriter_fourcc(*"mp4v")
output = cv.VideoWriter("output_mask.mp4", fourcc, fps, (frame_width, frame_height), isColor=False)

# background subtractor for motion filtering
subtractor = cv.createBackgroundSubtractorMOG2(150, 300)

while True:

    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame) #apply subtractor
        cv.imshow("Mask", mask) # display mask
        output.write(mask) # save mask

        if cv.waitKey(24) == ord("x"): # speed of video and exit on pressing "x"
            break
    else:
        video = cv.VideoCapture("movement.mp4")

# clean up
cv.destroyAllWindows()
video.release()
output.release()