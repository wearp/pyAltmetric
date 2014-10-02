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
**Fetching by individual citations by identifiers**

You can fetch individual citations using DOI, PubMed ID, arxiv and ADS bibcode identifiers. A successful call will return a python dictionary::
    
    from pyaltmetric import Altmetric

    a = Altmetric()

    a.id("241939")
    a.doi("10.1038/news.2011.490")
    a.pmid("21148220")
    a.arxiv("1108.2455")
    a.ads("2012apphl.100y3104b")

    a = Altmetric("api_key_goes_here")

**Querying the Altmetric.com database**

You can query the Altmetric.com for a list of articles in a give timeframe. For more information on parameters see `Querying the Database <http://api.altmetric.com/docs/call_citations.html>`_::

    a.citations("1w", page=1, nlmid="0410462")

**Reading a citation**
    
pyAltmetric has a Citation object provides an friendly interface for accessing citation attributes. Citation's ``get_fields()`` method allows the retrieval of multiple attributes::

    >>> from pyaltmetric import Altmetric, Citation
    >>>
    >>> b = a.id("241939")
    >>> c = Citation(b)
    >>> print c.title
    u'Rebuilding Global Fisheries'

Using Citation, you can get a taste for a citation's impact across multiple platforms::

    >>> c
    Altmetrics on: "Rebuilding Global Fisheries" with doi 10.1126/science.1173146 
    published in Science.

    All Posts      14
    Tweets          6
    Facebook        1
    Google+         0
    Reddit          0
    Blogs           2

    >>>

More examples
-------------
* `Using DOIs to fetch multiple citations <https://github.com/wearp/pyAltmetric/blob/master/examples/fetch_multiple_doi.py>`_
* `Creating a CSV file of citations using get_fields() <https://github.com/wearp/blob/pyaltmetric/citations_to_csv.py>`_

Copyright
---------
Copyright (c) 2014 Will Earp

License
-------
Free software: BSD license


