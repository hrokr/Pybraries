# Background and Project Description
 A few years ago I started a makerspace with a group of really good folks. Along the way we met an artist and instructor, Christina Weisner, who was in the early stages of doing a project and consulting with with one of our members, Kerry Kraus. Kerry was a professor of electronics technology at a local community college

According to Kerry, the code was a bit of kludge. It got the data from USGS somehow (I'm not sure if was RSS, Atom or JSON), processed it and sent a signal to a bunch of Arduino Uno boards (by SOUND). Each Arduino was used to ring one of set of seismometers Christina bought. You can see Christina & Kerry and learn more about her project [here](https://www.youtube.com/embed/uK_es620K0w).
<br><br><br>

# Current Status

Jupyter notebook with JSON data from the USGS and display it using Folium. It take about 8 seconds to pull the data, process it and have it display.
<br><br><br>

# Progress and Next Steps

- [x] Contact Eric Geist at [Tsunami and Earthquake Research](https://www.usgs.gov/centers/pcmsc/science/tsunami-and-earthquake-research?qt-science_center_objects=0#qt-science_center_objects) to see if there have been more tsunami occurrences
- [ ] Get & massage next tranche of data
- [ ] Develop model
- [ ] Move code from notebook to a website
- [ ] Twillio integration
  - [ ] Learn Twillio API
- [ ] Deploy and seek feedback

