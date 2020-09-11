# Playing with Plotly's Dash

Let me start off by saying that, at least so far, I've found Dash to be a complete pain in the ass. It almost single-handedly manages to make Python code as un-Pythonic as possible. But it does look cool and some folks are making some really nice vizualizations. <br>

# Projects:
 - Bees - A cookbook intro project to get familiar with Dash's MVC (or MVC-like) layout. Goes with an [accompanying YouTube video.](https://www.youtube.com/watch?v=hSPmj7mK6ng&t=382s) <br>

# What I don't like about Dash
  1. Overly verbose but in useless ways

    Why isn't this...
        {"label": "2015", "value": 2015}
    condensed and abstracted to this?
        {"2015": 2015}
    Or, at a minimum, this?
        {label: "2015", value: 2015}
  2. Semantic use of white space like the rest of Python? Yeah, screw that.


