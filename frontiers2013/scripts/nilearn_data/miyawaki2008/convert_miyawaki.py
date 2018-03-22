""" Convert Miyawaki 2008 dataset to NIfTI format.

This script takes the matlab version of Miyawaki dataset files and
convert them to NIfTI, a common format used in neuro-imaging.

This script require you to download some file and put them in the
current directory:
    * all .mat files of the dataset
    * file supple.mat used to reconstruct the original mask

All can be downloaded from this website :
    http://brainliner.jp/data/brainliner-admin/Reconstruct
"""

import os
import numpy as np
from scipy import io
import h5py

from nibabel import nifti1, Nifti1Image

supple = io.loadmat('supple.mat')

# Transposed shape (because matlab arrays are in Fortran order)
shapeT = (30, 64, 64)
stimShape = (10, 10)
affine = np.eye(4)


def _create_mask(name, indices):
    """ Create a mask, save it into a NIfTI file and return it

    Parameters
    ----------

    name: string
        Name of the file

    indices: 1D numpy array
        Indices of activated voxels
    """

    mask = np.zeros(shapeT, dtype=np.bool)
    mask_ravel = mask.ravel()
    for ind in indices:
        mask_ravel[ind] = True
    img = Nifti1Image(mask.astype(np.int).T, affine)
    nifti1.save(img, os.path.join('miyawaki2008', 'mask', name + '.nii.gz'))


def _convert_file(name, indices):
    # Load file
    print 'Converting %s' % name
    mat = h5py.File(name + '.mat')

    # Save fMRI scans
    fMRI_masked = []
    for i in range(1, 18065):
        fMRI_masked.append(mat['chData/ch%d/value' % i].value)
    fMRI_masked = np.asarray(fMRI_masked).T[0]
    fMRI = []
    for fm in fMRI_masked:
        f = np.zeros(shapeT)
        fr = f.ravel()
        for i, e in enumerate(fm):
            fr[indices[i]] = e
        fMRI.append(f[np.newaxis, ...])
    fMRI = np.concatenate(np.array(fMRI), axis=0).T
    img = Nifti1Image(fMRI, affine)
    nifti1.save(img, os.path.join('miyawaki2008', 'func', name + '.nii.gz'))

    # Save stimuli
    stimravel = []
    for i in range(18065, 18165):
        stimravel.append(mat['chData/ch%d/value' % i].value)
    stimravel = np.asarray(stimravel).T[0]
    np.savetxt(os.path.join('miyawaki2008', 'label', name + '_label.csv'),
               stimravel, fmt='%d', delimiter=',')
    print('... done.')


if os.path.exists('miyawaki2008'):
    import shutil
    shutil.rmtree('miyawaki2008')

os.mkdir('miyawaki2008')

# Create directories
os.mkdir(os.path.join('miyawaki2008', 'func'))
os.mkdir(os.path.join('miyawaki2008', 'mask'))
os.mkdir(os.path.join('miyawaki2008', 'label'))

# Create the general mask
_create_mask('mask', supple['volInd'][:, 0])

# Create ROI masks
for i in range(11):
    for j in range(4):
        if len(supple['roi_name'][i][j]) != 0:
            _create_mask(supple['roi_name'][i][j][0],
                         supple['roi_volInd'][i][j])

# Extract all data, keeping original file structure
# Figures
for i in range(1, 13):
    _convert_file('data_figure_run%02d' % i, supple['volInd'][:, 0])
# Random
for i in range(1, 21):
    _convert_file('data_random_run%02d' % i, supple['volInd'][:, 0])
