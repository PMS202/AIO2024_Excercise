import cv2
import numpy as np
import streamlit as st
from PIL import Image

PROTOTXT = r"D:\Hoc\AIO2024\AIO2024_Excercise\Module_1\week_04\Object_Detection\MobileNetSSD_deploy.prototxt"
MODEL = r"D:\Hoc\AIO2024\AIO2024_Excercise\Module_1\week_04\Object_Detection\MobileNetSSD_deploy.caffemodel"


def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    # Lặp qua các phát hiện
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startx, starty, endx, endy) = box.astype("int")
            cv2.rectangle(image, (startx, starty),
                          (endx, endy), (0, 255, 0), 2)
    return image


def main():
    """Main function for the image object detection app."""

    st.title("Object Detection for Images")

    uploaded_file = st.file_uploader(
        "Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image")

        image = Image.open(uploaded_file)
        image = np.array(image)

        # Assuming process_image and annotate_image functions exist
        detections = process_image(image)
        processed_image = annotate_image(image, detections)

        st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
