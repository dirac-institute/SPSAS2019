"""
Fetch all data files needed for examples chosen for SaoPaulo2019 bylectures by ZI, see
Sao Paulo School of Advanced Science on Learning from Data, July 31 - Aug 2, 2019
https://sites.usp.br/datascience/spsas-learning-from-data/
License: BSD; Zeljko Ivezic <ivezic@uw.edu>
"""

# *** SaoPaulo2019 participants: ***
# please copy this code somewhere and execute it; unless you 
# changed astroML defaults, you should see these 7 files in 
# your ~/astroML_data directory (a total of 400 MB):
# RRLyrae.fit			SDSSssppDR9_rerun122.fit
# SDSSspecgalsDR8.fit		sgSDSSimagingSample.fit
# dr7_quasar.npy		sdss_S82standards.npy
# spec4000.npz
# **************************
# the verbose output is also shown in
# http://www.astro.washington.edu/users/ivezic/astroML/AstroHackWeek2014/fetchAllData.out
# alternatively, you can simply copy this directory (and its contents) 
# http://www.astro.washington.edu/users/ivezic/astroML/AstroHackWeek2014/astroML_data
# as directory astroML_data in your home directory. 

#------------------------------------------------------------
# Get SDSS SSPP data
from astroML.datasets import fetch_sdss_sspp
data = fetch_sdss_sspp()

# Fetch the great wall data
from astroML.datasets import fetch_great_wall
from astroML.density_estimation import KNeighborsDensity
X = fetch_great_wall()

# Fetch and process the noisy imaging data
from astroML.datasets import fetch_imaging_sample
data_noisy = fetch_imaging_sample()

# Fetch and process the stacked imaging data
from astroML.datasets import fetch_sdss_S82standards
data_stacked = fetch_sdss_S82standards()

# get data and split into training & testing sets
from astroML.datasets import fetch_rrlyrae_combined
X, y = fetch_rrlyrae_combined()

# Fetch quasar data
from astroML.datasets import fetch_dr7_quasar
quasars = fetch_dr7_quasar()

# Download SDSS spectra 
from astroML.datasets import sdss_corrected_spectra
data = sdss_corrected_spectra.fetch_sdss_corrected_spectra()



