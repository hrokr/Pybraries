## What's in this (in case you haven't read the readme from the above level)?
**Earthquakes** -- A few years ago I started a makerspace with a group of really good folks. Along the way we met an artist and instructor, Christina Weisner, who was in the early stages of doing a project and consulting with with one of our members, Kerry Kraus. Kerry was a professor of electronics technology at a local community college

The code was a bit of kludge. It got the data from USGS somehow (I'm not sure if was RSS, Atom or JSON), processed it and sent a signal to a bunch of Arduinos (by SOUND), which were coded in wiring (basically, a lightweight version of C). Each Arduino was used to ring one of set of seismometers Christina bought. You can see Christina & Kery and learn more about her project [here](https://www.youtube.com/embed/uK_es620K0w)

**The Plan**
For an MVP I'm going to get the JSON data from the USGS and display it using Folium.

Assuming all that goes off well, I have some thoughts on how I want to branch out. I'd like to see if there is any relation between depth or intensity and tsunami formation and perhaps make it also provide warnings via twillio. I'm sure a lot of this has been done before so don't think this is a great feat.
