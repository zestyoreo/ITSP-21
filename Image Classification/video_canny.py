import cv2

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #uncomment below line to make vid stream come in greyscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Converting to sketch
    edges = cv2.Canny(frame, 100, 200)
    #inverting colour uncommentif want to
    ret, edges = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY_INV)
    # Display the resulting frame
    cv2.imshow('frame',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()