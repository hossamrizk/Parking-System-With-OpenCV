import cv2

# Read the image
image = cv2.imread('carParkImg.png')

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(x) + ", " + str(y)
        cv2.putText(image, text, (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow("Image", image)

cv2.imshow("Image", image)
cv2.setMouseCallback('Image', mouse)  # Ensure 'Image' matches the window name in imshow

cv2.waitKey(0)
cv2.destroyAllWindows()
