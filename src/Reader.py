import cv2
import zbar
# import numpy as np
class Reader():

# class DetectQRcode():
#
#     def detectQR(self, image):
#         scanner = zbar.ImageScanner()
#
#         scanner.parse_config('enable')
#
#         gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY, dstCn=0)
#         pil = image.fromarray(gray)
#         width , high = pil.size
#         raw = pil.tostring()
#         image = zbar.Image(width, height, 'Y800', raw)
#
#         scanner.scan(image)
#         for symbol in image:
#             loc = symbol.location
#             x = (loc[0][0]+loc[2][0])/2
#             y = (loc[0][1]+loc[2][1])/2
#             if symbol.data == "None":
#                 pass
#             else:
#                 return symbol.data
    def capture(self,):
        exec("fswebcam capture -r 1920x1080")


    def qrRead(self, image):
        pass

    def getPosition(self, code):

    def mapPositon(self, coord):
        prevSZ =[1920, 1080]
        newSZ = [3,2]
        return [(float(coord[0]) - 0) * (newSZ[1] - 0) / (prevsz[0] - 0) + 0, (float(coord[1]) - 0) * (newSZ[1] - 0) / (prevsz[1] - 0) + 0,]
