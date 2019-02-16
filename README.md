# Computer_Vision_Motion_Detection_2
Motion Detection In A Video Source -  Advance


1. The video is segmented into frames, (conider each frame as an image)
2. Consider 2 images / frames (A & B) that were taken back-to-back.
3. Convert the image A & B into gray scale. 
4. Compute a difference between these two gray scale images, and assign it to image C.
5. If, significant differece is detected between these two frames, we can conclude that some motion has occoured. 
6. An loop function will thus produce an new C image every time there is a frame change in the video.
7. Making is applied where the difference is larger than 1% of ther frame
8. Text is display if the mask is applied. 


----- TO RUN THE PROJECT ----- 
1. Using a terminal: python motion_detection_advance.py 
2. Using pycharm : Right click, and select Run motion_detection_advance.py
