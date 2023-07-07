# !pip install astroquery

from astroquery.mast import Catalogs

# Query for ADD_NAME in TIC using coordinates
# Example ADD_NAME = GJ 911
result_table = Catalogs.query_region("ADD_NAME", catalog="TIC")

# Extract the TIC value
tic = result_table['ID'][0]

# Print the TIC value
print("TIC:", tic)
