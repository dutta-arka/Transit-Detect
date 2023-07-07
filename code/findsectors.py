# !pip install lightkurve
# !pip install astroquery

import lightkurve as lk
# Set a TIC
TIC = 'TIC xxxxxxxxx'
# You could rn the following in a diffrent code box if are running a jupyter notebook and directly see from there
# lk.search_lightcurve(TIC, mission='TESS', author='SPOC')
lc_collection = lk.search_lightcurve(TIC, mission='TESS', author='SPOC').download_all()
# We are going to use only SPOC data. However SHERLOCKPIPE can make use of TESS-SPOC too.
L = list(set(lc_collection.sector))
L.sort()
print(L)
# Run before making each sector or combine make a loop to run them such that it does for all the target hosts
