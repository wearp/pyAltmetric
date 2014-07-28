===============================
pyAltmetric
===============================

.. image:: https://badge.fury.io/py/pyaltmetric.png
    :target: http://badge.fury.io/py/pyaltmetric

pyAltmetric is a python wrapper for `Altmetric API v1 <http://api.altmetric.com>`_. It provides an API for downloading and reading citations both individually and in bulk.

Installation
------------
::

    pip install pyaltmetric

Usage
-----
**Fetching by individual citations by identifiers**::
    
    from pyaltmetric import Altmetric

    a = Altmetric()

    a.id("241939")
    a.doi("10.1038/news.2011.490")
    a.pmid("21148220")
    a.rxiv("1108.2455")
    a.ads("2012apphl.100y3104b")

    a = Altmetric("api_key_goes_here")

**Querying the Altmetric.com database**::

    a.citations("1w", page=1, nlmid="0410462")

**Reading a citation**::
    
    from pyaltmetric import Citation

    b = a.id("241939")
    c = Citation(b)

    print c.title
    
    for field in c:
        print field

**Reading multiple citations**::
    
    form pyaltmetric import CitationCollection

    b = Citation(a.id("241939"))
    c = Citation(a.doi("10.1038/news.2011.490"))

    d = CitationCollection()
    d.add_citation(b, c)

    for citation in c:
        print citation
    
* Free software: BSD license


