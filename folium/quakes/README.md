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

