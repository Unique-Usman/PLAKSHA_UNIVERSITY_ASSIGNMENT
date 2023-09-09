import numpy as np

def binarize(im, thresh):
    """function to binarize an image

    Args:
        im: image to be binarize
        thresh: the threshhold value
    Returns:
        the result of binarize
    """
    h, w, c = im.shape
    ans = np.zeros([h, w], dtype="int32")
    for i in range(h):
        for j in range(w):
            ans[i, j] = 0 if thresh > np.sum(im[i, j]) / c else 1
    return ans
