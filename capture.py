import cv2, time

first_frame = None

while True:

    video = cv2.VideoCapture(0)
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) # Detta gör framen suddig och ökar träffsäkerheten

    if first_frame is None:
        first_frame = gray
        continue # Börjar loopen från början

    delta_frame = cv2.absdiff(first_frame, gray)

    # Om skillnaden är större än 30 från first_frame, gör det nya objektets pixel till vit
    frame_threshold = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # Ta bort hålen i en vit bild

    frame_threshold = cv2.dilate(frame_threshold, None, iterations=2)

    (cnts,_) = cv2.findContours(frame_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) > 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 3)

    #cv2.imshow("Me", frame)
    #cv2.imshow("Change", delta_frame)
    cv2.imshow("Threshold", frame_threshold)
    cv2.imshow("Colored", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break



video.release()
cv2.destroyAllWindows()