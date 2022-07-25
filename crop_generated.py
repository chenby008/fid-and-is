from PIL import Image
import os

img_dir1 = '/workspace/data/cby_recent/generated'
save_dir1 = '/workspace/data/cby_recent/pic1'
save_dir2 = '/workspace/data/cby_recent/pic2'
save_dir3 = '/workspace/data/cby_recent/pic3'
save_dir4 = '/workspace/data/cby_recent/pic4'
save_dir5 = '/workspace/data/cby_recent/pic5'
save_dir6 = '/workspace/data/cby_recent/pic6'
save_dir7 = '/workspace/data/cby_recent/pic7'

#if not os.path.exists(save_dir):
#	os.mkdir(save_dir)

cnt = 0
w, h = 192, 256

for item in os.listdir(img_dir1):
	cnt = cnt + 1
	print('%d/56 ...' %(cnt))
	img1 = Image.open(os.path.join(img_dir1, item))
	imgcrop1 = img1.crop((0, 0, w, h))
	imgcrop2 = img1.crop((w, 0, 2 * w, h))
	imgcrop3 = img1.crop((2 * w, 0, 3 * w, h))
	imgcrop4 = img1.crop((3 * w, 0, 4 * w, h))
	imgcrop5 = img1.crop((4 * w, 0, 5 * w, h))
	imgcrop6 = img1.crop((5 * w, 0, 6 * w, h))
	imgcrop7 = img1.crop((6 * w, 0, 7 * w, h))
	imgcrop1.save(os.path.join(save_dir1, item))
	imgcrop2.save(os.path.join(save_dir2, item))
	imgcrop3.save(os.path.join(save_dir3, item))
	imgcrop4.save(os.path.join(save_dir4, item))
	imgcrop5.save(os.path.join(save_dir5, item))
	imgcrop6.save(os.path.join(save_dir6, item))
	imgcrop7.save(os.path.join(save_dir7, item))
