import matplotlib.pylab as plt
import numpy as np
import cv2
noktalar = np.array([[(150, 630), (1200, 600), (780, 450), (550, 450)]])
def maske(resim):
    maske = np.zeros_like(resim)
    noktalar = np.array([[(150, 630), (1200, 620), (780, 450), (550, 450)]])
    cv2.fillPoly(maske,noktalar,255)
    maskeli = cv2.bitwise_and(resim,maske)
    return maskeli
def cizgi(resim,cizgiler):
    resim = np.copy(resim)
    bosresim = np.zeros((resim.shape[0],resim.shape[1],3),dtype=np.uint8)
    try:
        for i in cizgiler:
            for x1,y1,x2,y2 in i:
                cv2.line(bosresim,(x1,y1),(x2,y2),(0,255,0),thickness=10)
        resim = cv2. addWeighted(resim,0.7,bosresim,1,0.0)
    except:
        print('Görüntü Yakalanamadı !')
    return resim

def toplam(resim):
    gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gri,155,255)
    kesit = maske(canny)
    cizgiler = cv2.HoughLinesP(kesit,rho=6,theta=np.pi/180,threshold=160,lines=np.array([]),minLineLength=30,maxLineGap=50)
    #cizgiler = cv2.HoughLinesP(kesit, 1, np.pi/180,30)
    son = cizgi(resim,cizgiler)
    return son
video = cv2.VideoCapture('yeni2.mp4')
while True:
    ret,goruntu = video.read()
    goruntu2 = toplam(goruntu)
    cv2.putText(goruntu2,'Alparslan Adali',(500,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('Orjinali',goruntu)
    cv2.imshow('Serit Takip',goruntu2)
    if cv2.waitKey(60) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()

















