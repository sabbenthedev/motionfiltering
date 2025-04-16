# Background Subtraction and Video Saving with OpenCV

This simple Python script uses OpenCV to apply background subtraction to a video and saves the output as a new `.mp4` file.

## Showcase
- [YT video - motion filtering](https://www.youtube.com/watch?v=3ykhqCq5v_M)

## Features

- Reads an input video (`movement.mp4`)
- Applies background subtraction using `cv2.createBackgroundSubtractorMOG2`
- Displays the live processed mask
- Saves the result as a grayscale `.mp4` video (`output_mask.mp4`)
- Stops when you press the `x` key

## Requirements

- Python 3.x
- OpenCV (`cv2`)

Install dependencies using:

```bash
uv add opencv-python