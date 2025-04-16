# background subtraction and video saving with opencv

this simple python script uses opencv to apply background subtraction to a video and saves the output as a new `.mp4` file.

## showcase
- [YT video - motion filtering](https://www.youtube.com/watch?v=3ykhqCq5v_M)

## features

- reads an input video (`movement.mp4`)
- applies background subtraction using `cv2.createBackgroundSubtractorMOG2`
- displays the live processed mask
- saves the result as a grayscale `.mp4` video (`output_mask.mp4`)
- stops when you press the `x` key

## requirements

- Python >=3.13
- OpenCV
