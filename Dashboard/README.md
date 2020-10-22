# DS-5500
## California Wildfires Dashboard
**Authors:** Gopalika Sharma and Surya Menon 

#### Summary:
This Plotly Dash dashboard explores historic California wildfires between 1992-2015. The dataset with these fire incidences is made available by the [US Forest Service](https://enterprisecontentnew-usfs.hub.arcgis.com/datasets/e4d020cb51304d5194860d4464da7ba7_0/data?geometry=61.662%2C-2.200%2C54.279%2C76.163).

This dashboard provides a spatial visualization of forest fires across the state, to better understand the distribution and severity of fires, as well as to observe interesting patterns and trends over time. We additionally included additional spatial data (including population metrics and locations of fire stations and health facilities) to assess the impact the impact of fires alongside other factors. We also created plots to explore some of the features of fire incidents (i.e. fire cause and size) that can be filtered by county and year to see more granular details. Visualizing this information could help the state of California determine where additional resources are needed to alleviate impact in the future. 

#### Run Dashboard Locally:
To run this dashboard locally the following Python packages are required:
- kepler.gl 0.2.1
- dash 1.16.3
- dash-core-components 1.12.1
- dash-html-components 1.1.1
- dash-bootstrap-components 0.10.7
- plotly 4.11.0
- pandas 1.1.2
- numpy 1.19.1

Navigate to the directory with the dashboard files included in this folder and run the following command:

```python app.py```

You should be directed to a localhost url, where the dashboard should be visible when loaded completely. 

**Note:** For this dashboard to load fully, necessary data files--including a CSV file with California fire instances and an html file with the kepler.gl map visualization must be in the directory. The kepler.gl file can be downloaded from this [link](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/q1ijfisgc0prk1f/keplergl_q3m03h.json), or can be recreated with the `kepler_map.ipynb` file in this directory and the GeoJSON files and California fires CSV file. 

#### References to Spatial Datasets:
1. US Forest Service. (2020, April 29). National Interagency Fire Occurrence 1992-2015 (Feature Layer). https://enterprisecontentnew-usfs.hub.arcgis.com/datasets/e4d020cb51304d5194860d4464da7ba7_0/data?geometry=61.662%2C-2.200%2C54.279%2C76.163  

2. CAL FIRE. (2020, September 14). California County Boundaries. California State Geoportal. https://gis.data.ca.gov/datasets/CALFIRE-Forestry::california-county-boundaries 

3. Homeland Infrastructure Foundation-Level Data (HIFLD). (2020, September 11). Fire Stations. HIFLD Open Data. https://hifld-geoplatform.opendata.arcgis.com/datasets/fire-stations?geometry=-130.326%2C33.769%2C-104.442%2C39.917

4. CA Open Data - Department of Public Health. (2020, October 18). CDPH Licensing and Certification Healthcare Facilities. California State Geoportal. https://gis.data.ca.gov/datasets/CDPHDATA::cdph-licensing-and-certification-healthcare-facilities
