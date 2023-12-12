# Transit-Detect
A repository to focus only on finding transit of RV confirmed and candidate planets. Constraints: Orbital Period: [0.5, 33.0] days

## Downloading Data
Required targets can be found in NASA Exoplanet Archive or The Extrasolar Planets Encyclopaedia. Select RV confirmed/candidate planets and download the .csv files. Include the TIC list for confirmed planets if you download it from NASA Exoplanet Archive. In case you use The Extrasolar Planets Encyclopaedia, you can use TICconverter.py.

## Processing Data
Once You have downloaded the data, Select the host star names with an orbital period of less than 33 days (default of SHERLOCKPIPE). Make a .txt file (Or directly read from a .csv file in the terminal. Three such .txt files are added here.
Using these .txt files, run finaldataset.ipynb.

## Analysing the data
We use [SHERLOCKPIPE](https://github.com/franpoz/SHERLOCK.git) for this step. Please see the [documentation](https://sherlockpipe.readthedocs.io/en/latest/index.html#) for a detailed overview. The steps are the following.
+ For each run, findsectors.py to find the sectors for which the targets have been observed.
+ Update the prop1.yaml or prop2.yaml, depending upon your preference.
+ run the command ``` python3 -m sherlockpipe --properties c13.yaml ``` on terminal after installing SHERLOCKPIPE or use ``` !python3 -m sherlockpipe --properties c13.yaml ``` in ipython or jupyter notebook.
+ Zip the final file and download that.

## Tabulating Data
A tabulation format of all the data is given in data.csv. [Final Data Sheet](https://docs.google.com/spreadsheets/d/1i95u_nRxyQGhKAlw-9guYQfdSYQ4seXdPk9JbY0Tunw/edit?usp=sharing) This leads to a google spreadsheet that contains all the relevant information regarding any planet detection and corresponding vetting information. The candidates that came out relevant after the vetting have been documented in this spreadsheet. [Release Data](https://docs.google.com/spreadsheets/d/1sjhrfy6IH1ciZ82lqMhPsQIwn5zKqHrpNN8fCc6v7X8/edit?usp=sharing).

## Vetting
A small description of the vetting process is described below.
### Manually
The first step toward vetting the objects of interest was done manually. All the output from SHERLOCKPIPE was thoroughly vetted, and a set of possible transit events were noted. This process was similar to the planethunters project, except on a much smaller scale and all by me.
### Using TRICERATOPS
All the manually vetted candidates are then processed using a statistical vetting package called "TRICERATOPS". The notebooks for all such candidates are added to the vetting and candidate folders for confirmed and candidate RV planets after manual vetting.

## Final Output
All the possible/likely planets are listed here [Report Data](https://docs.google.com/spreadsheets/d/1eRbgPTvS1gr9Y8xxylBoHJVLFCWtdh_d3sfJu33GQPU/edit?usp=sharing)

## Future Works
A possible work could be using machine learning integrated with JWST data for many long-period planets.

## References

