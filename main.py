import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

def show_InputImage(content_image, style_image):
    plt.imshow(np.squeeze(content_image))
    plt.show()
    plt.imshow(np.squeeze(style_image))
    plt.show()

def stylize_image(content_image, style_image):
    return model(tf.constant(content_image), tf.constant(style_image))[0]

def show_OutputImage(content_image, stylized_image):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(np.squeeze(content_image))
    axes[0].set_title('Content Image')
    axes[0].axis('off')
    
    axes[1].imshow(np.squeeze(stylized_image))
    axes[1].set_title('Stylized Image')
    axes[1].axis('off')
    
    plt.show()
    fig.savefig('comparison_output.jpg')
    cv2.imwrite('output.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))

def main():
    content_image = load_image('WatArun.jpg')       
    style_image = load_image('StarryNight.jpg')
    show_InputImage(content_image, style_image)
    stylized_image = stylize_image(content_image, style_image)
    show_OutputImage(content_image, stylized_image)

if __name__ == "__main__":
    main()