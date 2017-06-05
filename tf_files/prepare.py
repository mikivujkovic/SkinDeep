"""
Script that augments images in benign and malignant folders
"""
import augment
import os       

augment.augment_dir("benign", "augmented/benign")
augment.augment_dir("malignant", "augmented/malignant")

