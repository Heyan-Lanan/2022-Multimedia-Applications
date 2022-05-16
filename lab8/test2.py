import cv2
import SimpleITK as sitk
import matplotlib.pyplot as plt

ct_path = './volume-0.nii'
seg_path = './segmentation-0.nii'
ct_array = sitk.GetArrayFromImage(sitk.ReadImage(ct_path))
seg_array = sitk.GetArrayFromImage(sitk.ReadImage(seg_path))
seg_bg = seg_array==0
seg_liver = seg_array>=1
seg_tumor = seg_array==2

ct_bg = ct_array*seg_bg
ct_liver = ct_array*seg_liver
ct_tumor = ct_array*seg_tumor

bg_min = ct_bg.min()
bg_max = ct_bg.max()
liver_min = ct_liver.min()
liver_max = ct_liver.max()
tumor_min = ct_tumor.min()
tumor_max = ct_tumor.max()
hist_bg = cv2.calcHist([ct_bg.flatten()],[0],None,[100],[int(bg_min),int(bg_max)])# shape(100, 1)
hist_liver = cv2.calcHist([ct_liver.flatten()],[0],None,[100],[int(liver_min),int(liver_max)])# shape(100, 1)
hist_tumor = cv2.calcHist([ct_tumor.flatten()],[0],None,[100],[int(tumor_min),int(tumor_max)])# shape(100, 1)
plt.plot(hist_bg,'k')
plt.plot(hist_liver,'r')
plt.plot(hist_tumor,'g')
plt.legend(('bg', 'liver', 'tumor'),loc='upper right')
plt.title('Tissue Intensity Distribution')
plt.show()
