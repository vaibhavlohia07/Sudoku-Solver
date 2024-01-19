### Prerequisites
- Python 3.8
- OpenCV
### Procedure
1)  Image preprocessing (Thresholding).
2)  Find the largest contour (sudoku square).
3)  Get the cordinates of largest contour.
4)  Crop the image.
5)  Perform Warp perspective on image
6)  Extract each cells from the image by slicing the sudoku grid.
7)  Extract the largest component in the sudoku image (number).
8)  Remove noise in block.
9)  Send the number to pre trained Digit Recogition model.
10) Send the grid to Sudoku Solver to perform the final step.