import cv2

def apply_filter(image):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0,-1,0]])
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image
