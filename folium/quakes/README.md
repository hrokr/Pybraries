# Background and Project Description
A few years ago I started a makerspace with a group of really good folks. Along the way we met an artist and instructor, Christina Weisner, who was in the early stages of doing a project and consulting with with one of our members, Kerry Kraus. Kerry was a professor of electronics technology at a local community college.

According to Kerry, the code was a bit of kludge. It got the data from USGS somehow (I'm not sure if was RSS, Atom or JSON), processed it and sent a signal to a bunch of Arduino Uno boards (by SOUND!). Each Arduino was used to actuate one of the seismometers Christina bought. You can see Christina & Kerry and learn more about her project [here](https://www.youtube.com/embed/uK_es620K0w).

I really like the idea of this project because it blends art with technology. And it's even cooler because one of the hydrophones was still functional so Christina (with some help) was able to futher it by making the observers part of the installation. Another thing I found to be interesting is the artist as a sort of conductor. Christina had the inspiration and idea but a lot of the actual fabrication and technical aspects came from others. 

I want to take this in a somewhat different direction. In part this is because I'd like to take a stab at a tusnami warning system but part is simply because don't have any hydrophones on hand. Or a place to store them for that matter.
<br><br><br>

# Current Status

Jupyter notebook that pulls the JSON data from USGS of earthquakes greater than magnitude 2.5 over the last day. This is displayed using Folium because I wanted to recreate as close as I could the USGS map which is done in Leaflet.JS, which Folium is based on. It takes about 8 seconds to pull the data, process it and have it display.
<br><br><br>

# Progress and Next Steps

- [x] Contact Eric Geist at [Tsunami and Earthquake Research](https://www.usgs.gov/centers/pcmsc/science/tsunami-and-earthquake-research?qt-science_center_objects=0#qt-science_center_objects) to see if there have been more tsunami occurrences
- [ ] Get & massage data for tsunami warnings and for actual tsunamis reported
- [ ] Develop model
- [ ] Move code from notebook to a website
- [ ] Twillio integration
  - [ ] Learn Twillio API
- [ ] Deploy and seek feedback
<br><br><br>


# On to the data
If you take some time to delve into the data, you're likely to run into some of the same questions I had. Namely, what do some of the values mean? Is a Tsunami Event Validity of 1 better or worse, more or less valid, or ... what than a Tsunami Event with a validity of 4? For the purposes of completeness, here is a legend for select fields along with commentary:
<br><br>
### <u>Tsunami Event Validity (Valid values: -1 to 4)</u>
  - -1	erroneous entry
  - 0	event that only caused a seiche or disturbance in an inland river
  - 1	very doubtful tsunami
  - 2	questionable tsunami
  - 3	probable tsunami
  - 4	definite tsunami

<center><b>Scores less than 3 will be dropped </b> </center>
<br><br>

### <u>Deaths from the Tsunami and the Source Event</u>

When a description was found in the historical literature instead of an actual number of deaths, this value was coded and listed in the Deaths column. If the actual number of deaths was listed, a descriptor was also added for search purposes.
  - 0	None
  - 1	Few (~1 to 50 deaths)
  - 2	Some (~51 to 100 deaths)
  - 3	Many (~101 to 1000 deaths)
  - 4	Very many (over 1000 deaths)
<br><br>
### <u>Tsunami Cause Code:</u> <br>
Valid values: 0 to 11
 - 0	Unknown
 - 1	Earthquake
 - 2	Questionable Earthquake
 - 3	Earthquake and Landslide
 - 4	Volcano and Earthquake
 - 5	Volcano, Earthquake, and Landslide
 - 6	Volcano
 - 7	Volcano and Landslide
 - 8	Landslide
 - 9	Meteorological
 - 10	Explosion
 - 11	Astronomical Tide
<br><br>







