# Text Detection with OpenCV and EasyOCR

This project demonstrates the use of OpenCV, Matplotlib, and EasyOCR for performing Optical Character Recognition (OCR) on images.

## Introduction

This project is designed to perform OCR on images using the EasyOCR library. It leverages OpenCV for image processing and Matplotlib for visualization. The goal is to provide a simple and effective way to extract text from images.

## Features

- Image preprocessing using OpenCV
- Text extraction using EasyOCR
- Visualization of results using Matplotlib

## Requirements

- Python 3.9 or higher
- `opencv-python-headless`
- `matplotlib`
- `easyocr`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Azur4ok/text_detection.git
    cd text_detection
    ```

2. Create a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your image files in the `data` directory.

2. Run the main script:

    ```sh
    python main.py
    ```

3. The script will process the images, perform OCR, and display the results using Matplotlib.

