"""Tools to style a talk."""

from IPython.display import HTML, display, YouTubeVideo

def prefix(url):
    prefix = '' if url.startswith('http') else 'http://'
    return prefix + url


def simple_link(url, name=None):
    name = url if name is None else name
    url = prefix(url)
    return '<a href="%s" target="_blank">%s</a>' % (url, name)


def html_link(url, name=None):
    return HTML(simple_link(url, name))


# Utility functions
def website(url, name=None, width=800, height=450):
    html = []
    if name:
        html.extend(['<div class="nb_link">',
                     simple_link(url, name),
                     '</div>'] )

    html.append('<iframe src="%s"  width="%s" height="%s">' % 
                (prefix(url), width, height))
    return HTML('\n'.join(html))


def nbviewer(url, name=None, width=800, height=450):
    return website('nbviewer.ipython.org/url/' + url, name, width, height)

# Load and publish CSS
style = HTML("""<style>

.rendered_html
{
  color: #2C5494;
  font-family: Ubuntu;
  font-size: 140%;
  line-height: 1.1;
  margin: 0.5em 0;
  }

.talk_title
{
  color: #498AF3;
  font-size: 250%;
  font-weight:bold;
  line-height: 1.2; 
  margin: 10px 50px 10px;
  }

.subtitle
{
  color: #386BBC;
  font-size: 180%;
  font-weight:bold;
  line-height: 1.2; 
  margin: 20px 50px 20px;
  }

.slide-header, p.slide-header
{
  color: #498AF3;
  font-size: 200%;
  font-weight:bold;
  margin: 0px 20px 10px;
  page-break-before: always;
  text-align: center;
  }

.rendered_html h1
{
  color: #498AF3;
  line-height: 1.2; 
  margin: 0.15em 0em 0.5em;
  page-break-before: always;
  text-align: center;
  }


.rendered_html h2
{ 
  color: #386BBC;
  line-height: 1.2;
  margin: 1.1em 0em 0.5em;
  }

.rendered_html h3
{ 
  font-size: 100%;
  line-height: 1.2;
  margin: 1.1em 0em 0.5em;
  }

.rendered_html li
{
  line-height: 1.8;
  }

.input_prompt, .CodeMirror-lines, .output_area
{
  font-family: Consolas;
  font-size: 120%;
  }

.gap-above
{
  padding-top: 200px;
  }

.gap01
{
  padding-top: 10px;
  }

.gap05
{
  padding-top: 50px;
  }

.gap1
{
  padding-top: 100px;
  }

.gap2
{
  padding-top: 200px;
  }

.gap3
{
  padding-top: 300px;
  }

.emph
{
  color: #386BBC;
  }

.warn
{
  color: red;
  }

.center
{
  text-align: center;
  }

.nb_link
{
    padding-bottom: 0.5em;
}

</style>""")


display(style)
