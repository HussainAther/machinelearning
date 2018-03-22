from nilearn import datasets
from nilearn.plotting import plot_stat_map, show
from nilearn.input_data import NiftiMasker
from sklearn.feature_selection import f_regression
import numpy as np
import matplotlib.pyplot as plt

"""
This example shows how to use the Localizer dataset in a basic analysis.
A standard Anova is performed (massively univariate F-test) and the resulting
Bonferroni-corrected p-values are plotted. We use a calculation task and 20 subjects out of the 94 available.
"""

# Load Localizer contrast
n_samples = 20 # 20 samples
localizer_dataset = datasets.fetch_localizer_calculation_task(
    n_subjects=n_samples) # Fetch calculation task contrast maps from the localizer.
tested_var = np.ones((n_samples, )) # Ones used in anova test

"""
Neuroimaging data are represented in 4 dimensions: 3 spatial dimensions,
and one dimension to index time or trials. Scikit-learn algorithms, on the other hand,
only accept 2-dimensional samples × features matrices (see section 2.3).
Depending on the setting, voxels and time series can be considered as features or samples.
For example, in spatial independent component analysis (ICA), voxels are samples.

The reduction process from 4D-images to feature vectors comes with the
loss of spatial structure (see Figure 1). It however allows to discard
uninformative voxels, such as the ones outside of the brain. Such voxels
that only carry noise and scanner artifacts would reduce SNR and affect
the quality of the estimation. The selected voxels form a brain mask.
Such a mask is often given along with the datasets or can be computed
with software tools such as FSL or SPM.

Nifti_masker is used for applying a mask to extract time-series from Niimg-like objects.

NiftiMasker is useful when preprocessing (detrending, standardization, resampling, etc.)
of in-mask voxels is necessary. Use case: working with time series of resting-state or task maps.
"""

nifti_masker = NiftiMasker( # Applying a mask to extract time-series from Niimg-like objects.
    smoothing_fwhm=5,
    memory='nilearn_cache', memory_level=1)  # cache options
cmap_filenames = localizer_dataset.cmaps
fmri_masked = nifti_masker.fit_transform(cmap_filenames)

# Get Anova (parametric F-scores)
# F regression is a linear model for testing the individual effect of each of many regressors. This is a scoring function to be used in a feature seletion procedure, not a free standing feature selection procedure.

_, pvals_anova = f_regression(fmri_masked, tested_var, # Univariate linear regression tests.
                              center=False)  # do not remove intercept
pvals_anova *= fmri_masked.shape[1]
pvals_anova[np.isnan(pvals_anova)] = 1
pvals_anova[pvals_anova > 1] = 1
neg_log_pvals_anova = - np.log10(pvals_anova)
neg_log_pvals_anova_unmasked = nifti_masker.inverse_transform(
    neg_log_pvals_anova)

## Visualization
## Various plotting parameters
z_slice = 45  # plotted slice

threshold = - np.log10(0.1)  # 10% corrected

# Plot Anova p-values
fig = plt.figure(figsize=(5, 6), facecolor='w')
display = plot_stat_map(neg_log_pvals_anova_unmasked,
                        threshold=threshold,
                        display_mode='z', cut_coords=[z_slice],
                        figure=fig)

masked_pvals = np.ma.masked_less(neg_log_pvals_anova_unmasked.get_data(),
                                 threshold)

title = ('Negative $\log_{10}$ p-values'
         '\n(Parametric + Bonferroni correction)'
         '\n%d detections' % (~masked_pvals.mask).sum())

display.title(title, y=1.1, alpha=0.8)

show()

