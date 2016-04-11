import parslepy, urllib2
rules = {"questions(//div[contains(@class,'question-summary')])": [{"title": ".//h3/a", "votes": "div.votes div.mini-counts"}]}
parslepy.Parselet(rules).parse(urllib2.urlopen('http://stackoverflow.com'))
{'questions': [{'title': u'node.js RSS memory grows over time despite fairly consistent heap sizes',
    'votes': u'0'},
    {'title': u'SQL query for count of predicate applied on rows of subquery',
    'votes': u'3'},
}

import lxml.etree
import parslepy
import pprint
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample document to test parslepy</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>
<body>
<h1 id="main">What&rsquo;s new</h1>
<ul>
    <li class="newsitem"><a href="/article-001.html">This is the first article</a></li>
    <li class="newsitem"><a href="/article-002.html">A second report on something</a></li>
    <li class="newsitem"><a href="/article-003.html">Python is great!</a> <span class="fresh">New!</span></li>
</ul>
</body>
</html>"""
rules = {
     "heading": "h1#main",
     "news(li.newsitem)": [{
         "title": ".",
         "url": "a/@href",
         "fresh": ".fresh"
     }],
}
p = parslepy.Parselet(rules)
extracted = p.parse_fromstring(html)
pprint.pprint(extracted)
{'heading': u'What\u2019s new',
 'news': [{'title': u'This is the first article', 'url': '/article-001.html'},
          {'title': u'A second report on something',
           'url': '/article-002.html'},
          {'fresh': u'New!',
           'title': u'Python is great! New!',
           'url': '/article-003.html'}]}
