import cv2
from os.path import dirname, join

# LECTURA DEL MODELO ----
# Modelo de arquitectura
prototxt = join(dirname(__file__),"model/MobileNetSSD_deploy.prototxt.txt")
# Pesos
model = join(dirname(__file__),"model/MobileNetSSD_deploy.caffemodel")
#Etiquetas de la clase del modelo preentrenado

classes = {0:"Fondo",1:"aeroplane",2:"bicycle",3:"bird",4:"boat",5:"bottle",6:"bus",7:"Auto"}
#Se carga el modelo de la red
net = cv2.dnn.readNetFromCaffe(prototxt, model)

#Para la lectura de imagenes
direccion = join(dirname(__file__),"Images/104.jpg")
image = cv2.imread(direccion)

#Definicion de las dimensiones de las imagenes
height, width, _ = image.shape
image_resized = cv2.resize(image,(300,300))

#Se crea la entrada
blob = cv2.dnn.blobFromImage(image_resized, 0.007843,(300,300),(127.5, 127.5,127.5))
print("blob.shape:", blob.shape)

#Detecciones y predicciones

net.setInput(blob)
detections=net.forward()

for detection in detections[0][0]:
    print(detection)

    if detection[2] > 0.45:
        label = classes[detection[1]]
        print("Label:",label)
    
        #Etiquetado
        box = detection[3:7] * [width,height,width,height]
        x_start, y_start, x_end, y_end = int(box[0]),int(box[1]),int(box[2]),int(box[3])

        cv2.rectangle(image,(x_start,y_start),(x_end,y_end),(0,255,0),2)
        cv2.putText(image,"Conf: {:.2f}".format(detection[2]*100),(x_start,y_start - 5), 1, 1.2, (255,0,0),2)
        cv2.putText(image,label,(x_start,y_start-25),1,1.2,(255,0,0),2)


cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()