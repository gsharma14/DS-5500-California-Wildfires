# DS-5500
## Exploring Wildfires: Can Only *We* Prevent Forest Fires?
**Authors:** Gopalika Sharma and Surya Menon 

#### Summary:
The increasing number of forest fires throughout the world is one the biggest threats to our lives and the environment. Climate change has produced higher temperatures and drier conditions, which have resulted in longer and harsher fire seasons, particularly in the western United States (1). While forest fires are natural processes that can benefit the environment—by clearing heavy brush, releasing nutrients into the soil, and facilitating seed germination for tree and plant species—these fires are becoming larger and harder to manage. As a result, we have observed increasingly catastrophic and devastating consequences, including the destruction of property, wildlife, and human lives (2).

In fact, during this year’s wildfire season, which can be seen in Figure 1, California has experienced over 8,000 fire incidents across the state, with over 4 million acres burned, thousands of structures damaged or destroyed, and 31 fatalities as of October 26, 2020 (3). The costly interactions between humans and wildfires underline the importance in understanding the relationship between them, especially in the face of changing climate conditions and expanding human communities. The uncertainty about the size, location, and number of future wildfires establishes an intriguing analytical and predictive modeling challenge. 

<br />
<p align="center">
  <img width="320" height="342" src="https://upload.wikimedia.org/wikipedia/commons/8/85/2020_California_wildfires.png">
</p>
<p align="center">
<b>Figure 1: Forest Fire Spread in California, 2020 </b>
</p>
<br />

This capstone project aimed to research various aspects of forest fires in order to discover relevant spatial patterns and predictive elements of fire incidents that governments—such as the state of California—can use to develop strategies to manage the impact of future fires. Multiple datasets were used to achieve these goals, including a geospatial dataset for historic wildfires in the United States (US) between 1992- 2015 and a dataset recording the forest fire and weather conditions (e.g., temperature, wind, humidity, etc.) for a set of fires located in northeast Portugal (4,5).

The spatial distribution of wildfires, specifically in California, was explored to find interesting patterns and trends over time with regards to the causes and severity of fire incidents. To better assess the overall impact of wildfires across the state, these fire occurrences were also evaluated alongside other spatial factors. We then created a dashboard to explore the spatial and historical patterns of California fires,including how the size and cause of fires vary across the state and over time; effectively visualizing this information can help the state in better analyzing wildfires and determining where additional intervention may be necessary in the future to minimize damage.

Additionally, we developed machine learning models to predict fire size (regression) and cause (classification) and identified the most significant features in the data for these modeling tasks. Better anticipating the fire severity or the possible cause can be instrumental in reducing future destruction in a community by ensuring resources are in place for safety, management, and faster containment. Both the Portugal and US fires (subset on California) datasets were used to conduct the regression task; these datasets have different features related to fire incidents (weather versus spatial factors), and we used the Portugal model results to inform which factors were most relevant in predicting size and augmented the California dataset (with climate data) accordingly. The California dataset was then also trained with both multi-class and binary classification to predict fire cause.

From our spatial analysis we observed that the severity of fire incidents has increased over time between 1992 and 2015, and particularly lightning-caused wildfires. Pockets of northern California and have faced persistent high frequencies of wildfires (exacerbated by climate change) that require closer monitoring and more aid to prevent considerable damage. Through predictive modeling, we found that weather- related factors were particularly relevant when looking to anticipate both fire size and cause; climate data that is specific to the actual fire incidents are likely needed to refine these predictions going forward.
<br />


#### References:
1. Gray, E. (2019, September 19). Satellite Data Record Shows Climate Change’s Impact on Fires. NASA - Global Climate Change: Vital Signs of the Planet. https://climate.nasa.gov/news/2912/satellite-data-record-shows-climate-changes-impact-on-fires/

2. California Department of Fish and Wildlife. (n.d.). Science: Wildfire Impacts. CA.gov. Retrieved 2020, from https://wildlife.ca.gov/Science-Institute/Wildfire-Impacts

3. Center for Disaster Philanthropy (CPP). (2020, October 23). 2020 North American Wildfire Season. Center for Disaster Philanthropy. https://disasterphilanthropy.org/disaster/2020-california-wildfires/

4. US Forest Service. (2020, April 29). National Interagency Fire Occurrence 1992-2015 (Feature Layer). 
https://enterprisecontentnew-usfs.hub.arcgis.com/datasets/e4d020cb51304d5194860d4464da7ba7_0/data?geometry=61.662%2C-2.200%2C54.279%2C76.163

5. UCI. (n.d.). UCI Machine Learning Repository: Forest Fires Data Set. UCI Machine Learning Repository. Retrieved 2020, from https://archive.ics.uci.edu/ml/datasets/Forest+Fires
