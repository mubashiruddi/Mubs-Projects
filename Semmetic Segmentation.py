import torch
from torchvision import transforms
from torchvision.models.segmentation import deeplabv3_resnet101, DeepLabV3_ResNet101_Weights
from PIL import Image
import matplotlib.pyplot as plt
import numpy

# Load model with pretrained weights
model = deeplabv3_resnet101(weights=DeepLabV3_ResNet101_Weights.COCO_WITH_VOC_LABELS_V1).eval()

def preprocess(image_path):
    image = Image.open(image_path).convert("RGB")
    to_tensor = transforms.ToTensor()  # Convert image to tensor
    return to_tensor(image).unsqueeze(0), image

def segment(image_path):
    image_tensor, image = preprocess(image_path)
    return image, model(image_tensor)['out'][0].argmax(0).cpu().numpy()

# Display results
def visualize(image_path):
    image, segmentation = segment(image_path)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(image)
    axs[0].axis("off"), axs[0].set_title("Original Image")
    axs[1].imshow(segmentation, cmap="jet", alpha=0.7)
    axs[1].axis("off"), axs[1].set_title("Segmentation Map")
    plt.show()

# Run
image_path = r"G:\web\test.jpg" 
visualize(image_path)