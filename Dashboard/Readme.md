# DS-5500
## California Wildfires Dashboard
**Authors:** Gopalika Sharma and Surya Menon 

#### Summary:
This plotly dashboard is exploring historic California Wildfires from 1992-2015.This data is available at https://enterprisecontentnew-usfs.hub.arcgis.com/datasets/e4d020cb51304d5194860d4464da7ba7_0/data?geometry=61.662%2C-2.200%2C54.279%2C76.163.</br>
This dashboard provides a spatial visualization of forest fires across the state, which allows for observing patterns and trends over time. We also added additional spatial data sources (including population metrics and locations of fire stations and health facilities) to assess other possible patterns with regards to the impact.We also created plots to explore some of the features of fire incidents (i.e. fire cause and size) that can be filtered to explore by county and year.

#### Instructions to Run:
To run this dashboard locally the following python packages are required:
1. kepler.gl 0.2.1</br>
2. dash 1.16.3</br>
3. dash-core-components 1.12.1</br>
4. dash-html-components 1.1.1</br>
5. dash-bootstrap-components 0.10.7</br>
6. plotly 4.11.0</br>
7. pandas 1.1.2</br>
8. numpy 1.19.1</br>

For the dashboard to run, navigate to the directory with the dashboard files included in this folder and run the following command:
python app.py</br>
You should be directed to the localhost url, where the dashboard should be visible when loaded completely.</br>
Note: For this dashboard to load correctly, necessary data files including the csv file with california fire instances and the kepler.gl html file with the map visualisation must be in the same folder.</br>
The kepler.gl file can be downloaded from the following link: https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/q1ijfisgc0prk1f/keplergl_q3m03h.json </br>
#### References:
1. Global Climate Change: Vital Signs of the Planet. https://climate.nasa.gov/news/2912/satellite-data-record-shows-climate-changes-impact-on-fires/  

2. California Department of Fish and Wildlife. (n.d.). Science: Wildfire Impacts. CA.gov. Retrieved 2020, from https://wildlife.ca.gov/Science-Institute/Wildfire-Impacts  

3. US Forest Service. (2020, April 29). National Interagency Fire Occurrence 1992-2015 (Feature Layer). https://enterprisecontentnew-usfs.hub.arcgis.com/datasets/e4d020cb51304d5194860d4464da7ba7_0/data?geometry=61.662%2C-2.200%2C54.279%2C76.163  

4. UCI. (n.d.). UCI Machine Learning Repository: Forest Fires Data Set. UCI Machine Learning Repository. Retrieved 2020, from https://archive.ics.uci.edu/ml/datasets/Forest+Fires  
