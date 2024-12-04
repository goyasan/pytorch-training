import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

preprocess_1 = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

preprocess_2 = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness = 0.5, contrast=0.5, saturation=0.5, hue=0.1),
    transforms.ToTensor()
])

preprocess_3 = transforms.Compose([
    transforms.RandomRotation(degrees=1),
    transforms.RandomResizedCrop(size=(224,224)),
    transforms.ToTensor(),  
])

image_path = "./06/exercise/exercise_data/dog_img.png"
image = Image.open(image_path)
processed_image = preprocess_3(image)

plt.imshow(processed_image.permute(1, 2, 0).numpy())
plt.show()