import cv2
import numpy as np
from matplotlib import pyplot as plt

fnames = ['crayfish.jpg', 'office.jpg', 'map.jpg', 'train.jpg', 'terrain.jpg']

for fname in fnames:
    I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    f, axes = plt.subplots(2, 3)

    axes[0, 0].imshow(I, 'gray', vmin=0, vmax=255)
    axes[0, 0].axis('off')

    axes[1, 0].hist(I.ravel(), 256, [0, 256])

    # second column
    pixels = I.ravel()
    hist, bins = np.histogram(pixels, 256, [0, 256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    # print(cdf_m)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    print(cdf_m.min(), cdf.max())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    # print(cdf)

    J = cdf[I]
    # a = np.where(cdf == 0)[0][-1]
    # b = np.where(cdf == 255)[0][0]
    # # a = pixels.mean() - 2 * pixels.std()
    # # b = pixels.mean() + 2 * pixels.std()
    # print(a, b)

    # J = (I-a) * 255.0 / (b-a)
    # J[J < 0] = 0
    # J[J > 255] = 255
    # J = J.astype(np.uint8)

    axes[0, 1].imshow(J, 'gray', vmin=0, vmax=255)
    axes[0, 1].axis('off')

    axes[1, 1].hist(J.ravel(), 256, [0, 256])

    # third column
    K = cv2.equalizeHist(I)

    axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
    axes[0, 2].axis('off')

    axes[1, 2].hist(K.ravel(), 256, [0, 256])

    plt.show()
