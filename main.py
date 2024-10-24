import cv2
import easyocr
import matplotlib.pyplot as plt


def main():
    image_path = 'data/img.png'
    img = cv2.imread(image_path)

    threshold = 0.25

    reader = easyocr.Reader(['en'], gpu=True)
    text_ = reader.readtext(img)

    for t in text_:
        bbox, text, score = t

        if score > threshold:
            cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 2)
            cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


if __name__ == '__main__':
    main()
