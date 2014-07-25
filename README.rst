===============================
altmetric-api
===============================

.. image:: https://badge.fury.io/py/altmetric-api-wrapper.png
    :target: http://badge.fury.io/py/altmetric-api-wrapper/0.1
    
.. image:: https://travis-ci.org/wearp/Altmetric.png?branch=master
        :target: https://travis-ci.org/wearp/Altmetric

.. image:: https://pypip.in/d/altmetric-api-wrapper/badge.png
        :target: https://pypi.python.org/pypi/altmetric-api-wrapper/0.1

# altmetric-api

altmetric-api is a python wrapper for [Altmetric API v1](http://api.altmetric.com). It provides an API for downloading and reading citations both individually and in bulk.

### Installation 

```
pip install altmetric-api
```

### Usage

#### Fetching by individual citations by identifiers
```
a = Altmetric()
a.id("241939")
a.doi("10.1038/news.2011.490")
a.pmid("21148220")
a.arxiv("1108.2455")
a.ads("2012apphl.100y3104b")

a = Altmetric("api_key_goes_here")
```

#### Querying the Altmetric.com database
```
b = Altmetric()
b.citations("1w", page=1, nlmid="0410462")
```

#### Reading a citation
```
c = Altmetric()
d = a.id("241939")

e = Citation(d)
print e
print e.title
for field in e:
    print field
```

* Free software: BSD license
* Documentation: http://Altmetric.readthedocs.org.

Features
--------

* TODO
