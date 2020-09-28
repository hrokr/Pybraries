# Playing with Plotly's Dash & Express Libraries

Let me start off by saying that, at least so far, I've found Dash to be a complete pain in the ass. It almost single-handedly manages to make Python code as un-Pythonic as possible. But, it can produce some very nice visualizations without JS and that whole bag (or truckload) of technologies. So, I'm at it again.

To make things worse, there isn't really all that much out there to help you learn Dash. This was compounded by a set of breaking changes. I'm not truly upset that they didn't manage to perfectly architect a path with no breaking changes. It's just that materials you would think could help often don't. So you go with the newest tutorials and find they're highly variable in quality and you never know how far back you can go to get information.

You might wonder what's there to learn in the first place aside from making a mess of the way things look.

Well, one of the big things is the MVC. Which is fairly common for web development but since web development isn't Python strong suit, most Python programmers aren't really familiar with it. I'm certainly not. Fortunately, the Plotly folks give it almost no attention so you get to wander around not knowing what questions to even ask.
<br> <br>

**Plotly Express (PX), on the other hand, is incredible.** It's both easy to use and pretty powerful. In just a few lines of code you can make some really nice graphs and charts.

Supposedly, PX is - or will be - a complete replacement for (yet another Plotly thing) Graph Objects(GO). But that doesn't come from Plotly, but a dev on YouTube so I find it somewhat hard to believe. I think it's more like PX is going to be the 95% solution with GO for when you need something really custom.Considering the speed, ease and end results compared with Matplotlib, I think it's worth the time. It may not be as flexible as Matplotlib (e.g., you're not going to be able to make an XKCD-like graph) but it looks much better out of the box and, again, it's faster to get something done.
<br> <br>
# Projects in this repo:
 - Dash <br>
   - **Bees** - A cookbook intro project to get familiar with Dash's MVC (or MVC-like) layout. Goes with an [accompanying YouTube video.](https://www.youtube.com/watch?v=hSPmj7mK6ng&t=382s)
   - **{in progress} Europe_internet** - Another cookbook focusing on the DataTable. Goes with an [accompanying YouTube video.](https://www.youtube.com/watch?v=USTqY4gH_VM)
   - **Gapminder** - A Jupyter Lab (don't try to run this as a notebook, it does't work well) that follows the second part of the [Plotly Express and Dash](https://www.youtube.com/watch?v=DIk-y41djCQ) tutorial.
 
  - Express <br>
    - **Plotly Express using Gapminder Data** - A notebook that follows the first part of the [Plotly Express and Dash](https://www.youtube.com/watch?v=DIk-y41djCQ) webinar by Nicolas Kruchten of Plotly. So far, this has been the absolute best thing I've seen, by anyone, on any Plotly library. *Personally, I'd start here.*<br>
    - **Plotly Express on Sunspots data**
    This is recreating the display using PX instead of seaborn.
    - **Plotly Express on Iranian census data** Plotly includes a certain set of maps for others you need to use something like MapBox. This is mostly the MapBox API to get a choropleth for country that isn't on their list.

# Notes

A couple of years back I attended a talk by, I think, a Node core developer. He said there is a saying that you only get beginner's eyes once, meaning that once you really understand something, you typically don't remember the useless part of how and why you were confused about something. And that's why you should contribute to Open Source libraries.

I'm writing this down for that reason. But I would also add that saying can be true in more than one way. You can make something that is confusing and tough to use and beginners will just pass on it. That beginner might not be a new developer either, they might just decide a potentially interesting and useful new technology doesn't stack up well against what they already know and so they pass on it.

The rate of adoption is a function of the ease of use and usefulness so it only makes sense to make something low friction.<br><br>

## What I don't like about Dash
  1. Verbose but in useless ways

    Why isn't this...
        {"label": "2015", "value": 2015}
    condensed and abstracted to this?
        {"2015": 2015}
    Or, at a minimum, this?
        {label: "2015", value: 2015}
  2. Semantic use of white space like the rest of Python? Yeah, screw that.
  3. This isn't so much about Dash as Jupyter Dash or maybe Node. Shortly after I installed Jupyter Dash (and the requisite node) Every went to hell. Basically this seems fragile somehow. Notebooks, even straight up PX only code, will just freeze. Complete, hope-you-saved-recently-'cause-you-gonna-lose-all-that freeze.

<br>

## What I don't like about Plotly Express
Not much, frankly. It's easy to use, quick to get started, pretty powerful, and looks good. About the only thing I'd point out is that for something like this:

    px.scatter(df, y='lifeExp', log_x=True, x='gdpPercap', size='pop', size_max=65, color='continent', hover_data= df.columns,range_y = [20,90], labels=dict(gdpPercap="GDP per Cap", lifeExp="Life Expectency"))

that last part *labels=dict(...)*  MUST be in that form; you can't use something more pythonic like:
    
    labels= {gdpPercap = "GDP per Cap", lifeExp = "Life Expectency"}

That's a pretty minor complaint.
   