# Playing with Plotly's Dash & Express Libraries


Let me start off by saying that, at least so far, I've found Dash to be a complete pain in the ass. It almost single-handedly manages to make Python code as un-Pythonic as possible. But it does look cool and some folks are making some really nice vizualizations. To make things worse, there isn't all that much out there to help you learn it. And this is compounded by a set of breaking changes. I'm not truly upset that they didn't manage to perfectly architect a path with no breaking changes; it's just that materials you would think could help don't. You'd think this just means go with the newest tutorials. Only they're highly variable in quality and you never know how far back you can go to get information. 

You might wonder what's there to learn in the first place aside from making a mess of the way things look. 

Well, one of the big things is the MVC. Which is fairly common for web development but since web development isn't Python strong suit, most Python programmers aren't really familiar with it. I'm certainly not. Fortunately, the Plotly folks give it almost no attention so you get to wander around not knowing what questions to even ask.
<br> <br>

Plotly Express, on the other hand, is incredible. It's both easy to use and pretty powerful. In just a few lines of code you can make some really nice graphs and charts. 

Supposedly, Plotly Express is - or will be - a complete replacement for (yet another Plotly thing) Graph Objects. Considering the speed and ease compared with Matplotlib, I think its worth the tiem. It's not as flexible as Matplotlib but it looks much better out of the box and, again, it's faster to get something done.
<br> <br>
# Projects in this repo:
 - Dash <br>
   - **Bees** - A cookbook intro project to get familiar with Dash's MVC (or MVC-like) layout. Goes with an [accompanying YouTube video.](https://www.youtube.com/watch?v=hSPmj7mK6ng&t=382s)
   - **{in progress} Europe_internet** - Another cookbook focusing on the DataTable. Goes with an [accompanying YouTube video.](https://www.youtube.com/watch?v=USTqY4gH_VM)
 
  - Express <br>
    - **Plotly Express using Gapminder Data** - A notebook that follows the first part of the [Plotly Express and Dash](https://www.youtube.com/watch?v=DIk-y41djCQ) webinar by Nicolas Kruchten of Plotly. So far, this has been the absolute best thing I've seen, by anyone, on any Plotly library. Personally, I'd start here.<br><br>


# Notes

A couple of years back I attended a talk by, I think, a Node core developer. And he said there is a saying that you only get beginner's eyes once, meaning that once you really understand something, you typically don't remember the useless part of how and why you were confused about something.

So, I'm writing this down for that reason. But I would also add that saying can be true in more than one way. You can make something that is confusing and tough to use and beginners will just pass on it. 

The rate of adoption is a function of the ease of use and usefulness so it only makes sense to make something low friction.<br><br>

## What I don't like about Dash
  1. Overly verbose but in useless ways

    Why isn't this...
        {"label": "2015", "value": 2015}
    condensed and abstracted to this?
        {"2015": 2015}
    Or, at a minimum, this?
        {label: "2015", value: 2015}
  2. Semantic use of white space like the rest of Python? Yeah, screw that.

<br>

## What I don't like about Plotly Express
Not much, frankly. It's easy to use, quick to get started, pretty powerful, and looks good. About the only thing I'd point out is that for something like this:

    px.scatter(df, y='lifeExp', log_x=True, x='gdpPercap', size='pop', size_max=65, color='continent', hover_data= df.columns,range_y = [20,90], labels=dict(gdpPercap="GDP per Cap", lifeExp="Life Expectency"))

that last part *labels=dict(...)*  MUST be in that form; you can't use something more pythonic like:
    
    labels= {gdpPercap = "GDP per Cap", lifeExp = "Life Expectency"}

That's a pretty minor complaint.
   