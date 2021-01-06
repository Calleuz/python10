import cv2

img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)

resized_img = cv2.resize(img, (int(img.shape[0]*0.5), int(img.shape[1]*0.5)))
cv2.imwrite("new_image.jpg", resized_img)
cv2.imshow("A beautiful galaxy",resized_img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
