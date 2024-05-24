import cv2
import numpy as np
import matplotlib.pyplot as plt

def visualize_image_with_polygon(image_path, polygon_coords_file, output_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Read and parse polygon coordinates from file
    points = []
    with open(polygon_coords_file, 'r') as file:
        coords = file.readline().split()[1:]  # Ignore the first value (class index)
        for i in range(0, len(coords), 2):
            x = int(float(coords[i]) * image.shape[1])
            y = int(float(coords[i+1]) * image.shape[0])
            points.append((x, y))
    
    # Create an empty mask to start with
    mask = np.zeros_like(image)

    # Fill the polygon area in the mask with white
    pts = np.array(points, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], (255, 255, 255))

    # Bitwise-and the mask with the original image
    isolated_image = cv2.bitwise_and(image, mask)
    
    # Save the isolated image
    cv2.imwrite(output_path, cv2.cvtColor(isolated_image, cv2.COLOR_RGB2BGR))

image_path = '/Users/sarahhaddad/Desktop/Segmentation/images/train/0AHWO6HSC4FE_jpg.rf.2f3eee02f3ef6ed6fe879952b675c8a9.jpg'
polygon_coords = '/Users/sarahhaddad/Desktop/Segmentation/labels/train/0AHWO6HSC4FE_jpg.rf.2f3eee02f3ef6ed6fe879952b675c8a9.txt'
output_path = 'isolated_image.jpg'
# Visualize the image with the polygon annotation and save the isolated image
visualize_image_with_polygon(image_path, polygon_coords, output_path)
