import cv2
import numpy as np

def extract_features(image_path):
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0

    features = {}

    features["ink_density"] = np.mean(img)
    features["blur_metric"] = cv2.Laplacian(img, cv2.CV_64F).var()

    edges = cv2.Canny((img*255).astype(np.uint8), 50, 150)
    features["edge_density"] = np.sum(edges > 0) / edges.size

    features["stroke_variance"] = np.var(img)
    features["horiz_profile_std"] = np.std(np.mean(img, axis=1))
    features["vert_profile_std"] = np.std(np.mean(img, axis=0))
    features["local_contrast"] = img.max() - img.min()

    _, thresh = cv2.threshold((img*255).astype(np.uint8), 127, 255, cv2.THRESH_BINARY_INV)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(thresh)

    areas = stats[1:, cv2.CC_STAT_AREA] if num_labels > 1 else [0]

    features["num_blobs"] = len(areas)
    features["avg_blob_area"] = np.mean(areas)
    features["blob_area_std"] = np.std(areas)

    features["skewness"] = np.mean((img - np.mean(img))**3)
    features["tremor_index"] = np.std(cv2.Laplacian(img, cv2.CV_64F))

    return list(features.values())
