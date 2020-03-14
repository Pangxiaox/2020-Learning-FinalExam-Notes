import matplotlib.pyplot as plt
from mxnet import nd
from mxnet import image
import cv2
from mxnet.gluon.data.vision import transforms

im_fname = './timg.jpg'
img_mx = image.imread(im_fname)

print(type(img_mx))
plt.imshow(img_mx.asnumpy())
plt.show()
print(img_mx.shape)
print(img_mx[:3,:5,:])

img_plt = plt.imread(im_fname)
print(img_plt.shape)
print(img_plt[:3,:5,:])
print(type(img_plt))
plt.imshow(img_plt)

img_cv2 = cv2.imread(im_fname)
print(img_cv2.shape)
print(img_cv2[:3,:5,:])
plt.imshow(img_cv2)
plt.show()

transforms_fn = transforms.Compose([
    transforms.Resize(32),
    transforms.CenterCrop(32),
    transforms.ToTensor(),
    transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])
])
img = transforms_fn(img_mx)
img_tran = nd.transpose(img, (1, 2, 0)).asnumpy()
print(img_tran[:3, :3, :])
plt.imshow(img_tran)
plt.show()