import cv2
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes
from PyPDF2 import PdfFileWriter, PdfFileReader
import uuid

#image = cv2.imread('DoraBootsForever.png')
text = None
images = convert_from_path('data.pdf')
for page in images:
    page.save('newout.jpg', 'JPEG')
image = cv2.imread('newout.jpg')
crop_img = image[990:1030, 1150:1600]
cv2.imwrite("cropped.jpg", crop_img)
#cv2.imshow("cropped", crop_img) 
text = pytesseract.image_to_string('cropped.jpg')
ans = ''.join([n for n in text if n.isdigit()])
print('Employer Identification Number : '+str(ans))
#print(text)
crop_img = image[270:310, 150:1600]
cv2.imwrite("cropped1.jpg", crop_img)
#cv2.imshow("cropped", crop_img) 
text = pytesseract.image_to_string('cropped1.jpg')
# ans = ''.join([n for n in text if n.isdigit()])
# print('Employer Identification Number :'+str(ans))
print('Name : '+text)