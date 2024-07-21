import cv2
import numpy as np


def compute_differenc(background,  image):
    dif = cv2.absdiff(background, image)
    dif_mono = np.sum(dif, axis=2) / 3.0
    dif_mono = dif_mono.astype('uint8')
    return dif_mono


def compute_binary_mask(dif_mono):
    _, mask = cv2.threshold(dif_mono, 15, 255, cv2.THRESH_BINARY)
    mask = np.stack((mask, mask, mask), axis=-1)
    return mask


def replace_background(mask, background_sub, image):
    image_sub = np.where(mask == 0, background_sub, image)
    return image_sub


def background_subtraction(background_dir, background_sub_dir, image_dir):
    IMAGE_SIZE = (678, 381)
    background = cv2.imread(background_dir)
    background = cv2.resize(background, IMAGE_SIZE)

    background_sub = cv2.imread(background_sub_dir)
    background_sub = cv2.resize(background_sub, IMAGE_SIZE)

    image = cv2.imread(image_dir)
    image = cv2.resize(image, IMAGE_SIZE)
    dif_mono = compute_differenc(background,  image)
    mask = compute_binary_mask(dif_mono)
    image_sub = replace_background(mask, background_sub, image)

    while True:
        cv2.imshow('Khung hình', image_sub)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

    # Giải phóng bộ nhớ
    cv2.destroyAllWindows()


if __name__ == "__main__":
    background_dir = r"D:\Hoc\AIO2024\AIO2024_Excercise\Module_2\Week_02\Image_data\GreenBackground.png"
    background_sub_dir = r"D:\Hoc\AIO2024\AIO2024_Excercise\Module_2\Week_02\Image_data\NewBackground.jpg"
    image_dir = r"D:\Hoc\AIO2024\AIO2024_Excercise\Module_2\Week_02\Image_data\Object.png"
    background_subtraction(background_dir, background_sub_dir, image_dir)
