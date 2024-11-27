### Prerequisites
To run the program, you will need:
* Python 3.8 or later
* OpenCV library (opencv-python-headless)
* NumPy library
### Procedure
1)  Image preprocessing by using thresholding
2)  Finding the largest contour, to identify the main sudoku grid
3)  Get the coordinates of the largest contour
4)  Crop the image accordingly
5)  Perform a warp perspective on the image
6)  Extract individual cells from the image by slicing the sudoku grid.
7)  Extract the largest component in the sudoku image, viz. the numbers
8)  Remove noise in the blocks
9)  Send the number to a pre-trained digit recogition model, the dataset for the pre-trained model is MNIST
10) Send the grid to sudoku-solver to perform the final step, where backtracking is applied to efficiently solve the sudoku
