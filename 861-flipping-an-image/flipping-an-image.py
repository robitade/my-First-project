class Solution(object):
  def flipAndInvertImage(self, image):
    n = len(image)
    
    # Flip each row horizontally
    for row in range(n):
        image[row] = image[row][::-1]
    
    # Invert the image
    for row in range(n):
        for col in range(n):
            image[row][col] = 1 - image[row][col]
    
    return image