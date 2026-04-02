from pdf2image import convert_from_path
import cv2
import numpy as np

def pdf_to_image(pdf_path):
    images = convert_from_path(
        pdf_path,
        poppler_path=r"E:\Software\poppler\Library\bin"  # 👈 add this
    )
    return images[0]

def compare_images(img1, img2):
    img1 = np.array(img1)
    img2 = np.array(img2)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    difference_score = np.sum(thresh)

    return difference_score, thresh