===============================
altmetric-api
===============================

.. image:: https://badge.fury.io/py/altmetric-api-wrapper.png
    :target: http://badge.fury.io/py/altmetric-api-wrapper

altmetric-api is a python wrapper for [Altmetric API v1](http://api.altmetric.com). It provides an API for downloading and reading citations both individually and in bulk.

Installation
------------
::

    pip install altmetric-api

Usage
-----
**Fetching by individual citations by identifiers**::
    from altmetric import Altmetric

    a = Altmetric()
    a.id("241939")
    a.doi("10.1038/news.2011.490")
    a.pmid("21148220")
    a.rxiv("1108.2455")
    a.ads("2012apphl.100y3104b")

    a = Altmetric("api_key_goes_here")

**Querying the Altmetric.com database**::

    a = Altmetric()
    a.citations("1w", page=1, nlmid="0410462")

**Reading a citation**::
    from altmetric import Citation

    a = Altmetric()
    b = a.id("241939")

    c = Citation(b)
    print c
    print c.title
    for field in c:
        print field

**Reading multiple citations**::
    form altmetric import CitationCollection

    a = Altmetric()
    b = Citation(a.id("241939"))
    c = Citation(a.doi("10.1038/news.2011.490"))

    d = CitationCollection()
    d.add_citation(b, c)

    for citation in c:
        print citation
    
* Free software: BSD license


