import cv2

system=cv2.imread("solar-system.jpg")

cv2.putText(system,"Sol",(100,108),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(system,"Mercurio",(110,180),cv2.FONT_ITALIC,0.6,(0,225,0))
cv2.putText(system,"Venus",(180,270),cv2.FAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION,2,(225,0,0))
cv2.putText(system,"Tierra",(255,170),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.2,(185,0,155))
cv2.putText(system,"Marte",(370,265),cv2.FONT_HERSHEY_PLAIN,2,(225,187,0))
cv2.putText(system,"Jupiter",(465,90),cv2.FONT_HERSHEY_DUPLEX,1.4,(0,169,195))
cv2.putText(system,"Saturno",(720,305),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.2,(225,17,70))
cv2.putText(system,"Urano",(940,135),cv2.FONT_HERSHEY_TRIPLEX,1.1,(145,220,0))
cv2.putText(system,"Neptuno",(1100,290),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(25,187,219))

cv2.imshow("solar",system)
cv2.waitKey(0)
print(system)