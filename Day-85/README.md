
# Image Watermark Application

This is a Python application that allows you to add a watermark to an image. The application provides a graphical user interface (GUI) for selecting an image, adjusting the watermark size, and displaying the resulting image with the watermark applied.

## Prerequisites

- Python 3.x
- Tkinter library
- Pillow library

## Installation

1. Clone the repository or download the source code files.

2. Install the required libraries using pip:

   ```
   pip install tkinter pillow
   ````

## Usage

1. Run the application by executing the following command:

   ```
   python image_watermark.py
   ````

2. The application window will open. Use the GUI to perform the following actions:

   - Select an image file by clicking on the "Select Image" button.
   - Adjust the watermark size using the spinbox.
   - The image with the applied watermark will be displayed in the application window.

3. Close the application window to exit.

## Code Explanation

The code consists of two main functions: `show_in_app` and `on_spinbox_change`.

- `show_in_app`: This function is invoked when the "Show in App" button is clicked. It retrieves the value from the spinbox, resizes the foreground image based on the value, pastes the foreground image onto the background image, and displays the resulting image.

- `on_spinbox_change`: This function is called when the value of the spinbox is changed. It performs similar operations to `show_in_app`, but it also resizes the image to fit within a maximum width and height, updates the label with the new image, and displays the resized image in the application window.

The code also includes an `if __name__ == "__main__"` block to instantiate the `ImageWatermarkApp` class and start the application.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

