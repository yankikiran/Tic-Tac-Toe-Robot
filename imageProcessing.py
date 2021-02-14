import cv2
import numpy as np


def imageToArray(img):
    #cv2.imshow("asd", img)
    #img = normallestir(img)
    
    images = divideArenaIntoNine(img)
    #cv2.imshow("ilk resim", images[0])

    letters = []
    for image in images:
        letter = readSmallSquare(image)
        letters.append(letter)

    return letters

def takePhoto():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # video capture source camera (Here webcam of laptop)
    ret = cap.set(3, 1920)
    ret = cap.set(4, 1080)
    ret, frame = cap.read()  # return a single frame in variable `frame`
    #cv2.imshow('Photo taken', frame)  # display the captured image
    cap.release()
    return frame

def warpImage(img):
    #img = takePhoto()
    #cv2.imshow("Photo before warp",img)
    width, height = 450, 450
    pts1 = np.float32([[301, 122], [1647, 57], [640, 804], [1447, 819]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow("Photo after warp", imgOutput)
    return imgOutput

def divideArenaIntoNine(img):
    images = []
    arenaHeight = img.shape[0]
    arenaWidth = img.shape[1]

    parlaklik=110

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, bigBlackAndWhiteImage) = cv2.threshold(grayImage, parlaklik, 255, cv2.THRESH_BINARY)

    cv2.imshow("kontrol",bigBlackAndWhiteImage)

    images.append(img[int(0.03 * arenaHeight):int(0.30 * arenaHeight), int(0.03 * arenaWidth):int(0.30 * arenaWidth)])
    #cv2.imshow("1.kare", images[0])

    images.append(img[int(0.03 * arenaHeight):int(0.30 * arenaHeight), int(0.36 * arenaWidth):int(0.63 * arenaWidth)])
    # cv2.imshow("2.kare", img2)

    images.append(img[int(0.03 * arenaHeight):int(0.30 * arenaHeight), int(0.69 * arenaWidth):int(0.97 * arenaWidth)])
    # cv2.imshow("3.kare", img3)

    images.append(img[int(0.36 * arenaHeight):int(0.63 * arenaHeight), int(0.03 * arenaWidth):int(0.30 * arenaWidth)])
    # cv2.imshow("4.kare", img4)

    images.append(img[int(0.36 * arenaHeight):int(0.63 * arenaHeight), int(0.36 * arenaWidth):int(0.63 * arenaWidth)])
    #cv2.imshow("5.kare", images[4])

    images.append(img[int(0.36 * arenaHeight):int(0.63 * arenaHeight), int(0.69 * arenaWidth):int(0.97 * arenaWidth)])
    # cv2.imshow("6.kare", img6)

    images.append(img[int(0.69 * arenaHeight):int(0.97 * arenaHeight), int(0.03 * arenaWidth):int(0.30 * arenaWidth)])
    # cv2.imshow("7.kare", img7)

    images.append(img[int(0.69 * arenaHeight):int(0.97 * arenaHeight), int(0.36 * arenaWidth):int(0.63 * arenaWidth)])
    #cv2.imshow("8.kare", images[7])

    images.append(img[int(0.69 * arenaHeight):int(0.97 * arenaHeight), int(0.69 * arenaWidth):int(0.97 * arenaWidth)])
    # cv2.imshow("9.kare", img9)

    return images


def readSmallSquare(img):
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    kernel = np.ones((5, 5), np.uint8)
    imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)
    img=imgDilated

    parlaklik=110

    iso="false"
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biseybuldummu = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            myimage=imgContour
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.rectangle(myimage, (x, y), (x + w, y + h), (0, 255, 0), 2)
            deltaw=int(w*0.25)
            deltah=int(h*0.25)
            myimage=myimage[y:y+h,x:x+w]
            cv2.rectangle(myimage, (int(0.5 * w) - deltaw, int(0.5 * h) - deltah),
                          (int(0.5 * w) + deltaw, int(0.5 * h) + deltah), (0, 0, 255), 2)
            #cv2.imshow("name",myimage)

            grayImage = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)
            (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, parlaklik, 255, cv2.THRESH_BINARY)
            #cv2.imshow('kontrol.jpg', blackAndWhiteImage)

            imgFinal=blackAndWhiteImage[(int(0.5 * h) - deltah):(int(0.5 * h) + deltah),(int(0.5 * w) - deltaw):(int(0.5 * w) + deltaw)]

            #cv2.imshow("final",imgFinal)
            kcontours, khierarchy = cv2.findContours(imgFinal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            myCounter=0

            for kcnt in kcontours:
                karea = cv2.contourArea(kcnt)
                if karea > 1:
                    myCounter=myCounter+1
            if myCounter > 1:
                biseybuldummu = 1
                return "X"
            elif myCounter == 1:
                biseybuldummu = 1
                return "O"
            else:
                print("hata")
    if biseybuldummu == 0:
        return " "




def test():

    img = takePhoto()
    print(imageToArray(warpImage(img)))

#test()
#cv2.waitKey(0)