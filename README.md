# Transit-Detect
A repository to focus only on finding transit of RV confirmed and candidate planets. Constraints: Orbital Period: [0.5, 33.0] days

## Downloading Data
Required targets can be found in either NASA Exoplanet Archive or The Extrasolar Planets Encyclopaedia. Select RV confirmed/candidate planets and download the .csv files. Include the TIC list for confirmed planets if you are downloading it from NASA Exoplanet Archive. In case you use The Extrasolar Planets Encyclopaedia, you can use TICconverter.py.

## Processing Data
Once You have downloaded the data, Select the host star names that have an orbital period of less than 33 days (default of SHERLOCKPIPE). Make a .txt file (Or directly read from a .csv file in the terminal. Three such .txt files are added here.
Using these .txt files, run finaldataset.ipynb.

## Analysing the data
We use [SHERLOCKPIPE](https://github.com/franpoz/SHERLOCK.git) for this step. Please see the [documentation](https://sherlockpipe.readthedocs.io/en/latest/index.html#) for a detailed overview. The steps are the following.
+ For each run, findsectors.py to find the sectors for which the targets have been observed.
+ Update the prop1.yaml or prop2.yaml depending upon your preference.
+ run the command ``` python3 -m sherlockpipe --properties c13.yaml ``` on terminal after installing SHERLOCKPIPE or use ``` !python3 -m sherlockpipe --properties c13.yaml ``` in ipython or jupyter notebook.
+ Zip the final file and download that.

## Tabulating Data
A tabulation format of all the data is given in data.csv. [Final Data Sheet 1; Of confirmed RV planets](https://docs.google.com/spreadsheets/d/1i95u_nRxyQGhKAlw-9guYQfdSYQ4seXdPk9JbY0Tunw/edit?usp=sharing)

## Vetting

### Manually

### Using TRICERATOPS


## Final Output


## Future Works


## References

