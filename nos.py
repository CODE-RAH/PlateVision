import cv2
import numpy as np
#import imutils

class ImprovedLicensePlateDetector:
    def __init__(self):
        self.min_plate_aspect = 2.5
        self.max_plate_aspect = 4.5
        self.min_plate_area = 0.002
        self.max_plate_area = 0.05
        self.edge_thresh1 = 30
        self.edge_thresh2 = 120
        self.clahe_clip = 2.5
        self.dilation_iterations = 3

    def adjust_for_iranian_plates(self, image):
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=self.clahe_clip, tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv2.merge((cl,a,b))
        enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        hsv = cv2.cvtColor(enhanced, cv2.COLOR_BGR2HSV)
        hsv[:,:,1] = hsv[:,:,1]*1.2
        enhanced = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return enhanced

    def detect_edges(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.bilateralFilter(gray,11,17,17)
        edges = cv2.Canny(blurred,self.edge_thresh1,self.edge_thresh2)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        morphed = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel)
        morphed = cv2.dilate(morphed,kernel,iterations=self.dilation_iterations)
        return morphed

    def find_plate_contour(self, edges, image):
        contours = cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours,key=cv2.contourArea,reverse=True)[:15]
        for contour in contours:
            peri = cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,0.02*peri,True)
            if len(approx)==4:
                x,y,w,h = cv2.boundingRect(approx)
                aspect_ratio = w/float(h)
                if self.min_plate_aspect<aspect_ratio<self.max_plate_aspect:
                    area = cv2.contourArea(contour)
                    img_area = image.shape[0]*image.shape[1]
                    area_ratio = area/img_area
                    if self.min_plate_area<area_ratio<self.max_plate_area:
                        roi = image[y:y+h,x:x+w]
                        if self.has_valid_characters(roi):
                            return approx
        return None

    def has_valid_characters(self, plate_region):
        gray = cv2.cvtColor(plate_region,cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        contours = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        plate_height = plate_region.shape[0]
        char_count = 0
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            char_ratio = h/float(plate_height)
            if 0.3<char_ratio<0.8 and w/h<1.2:
                char_count+=1
                if char_count>=3:
                    #return True
        #return False

    def detect_plate(self, frame):
        processed = self.adjust_for_iranian_plates(frame)
        edges = self.detect_edges(processed)
        plate_contour = self.find_plate_contour(edges,processed)
        if plate_contour is not None:
            x,y,w,h = cv2.boundingRect(plate_contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            plate = frame[y:y+h,x:x+w]
            cv2.imshow("Plate",plate)
            return True
        return False

def main():
    detector = ImprovedLicensePlateDetector()
    cap = cv2.VideoCapture(0)
    video_path = "vf.mp4"
    cap = cv2.VideoCapture(video_path)
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        frame = imutils.resize(frame,width=800)
        detected = detector.detect_plate(frame)
        cv2.imshow("License Plate Detection",frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()