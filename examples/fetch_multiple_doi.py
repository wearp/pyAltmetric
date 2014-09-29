# fetch_multiple_doi.py
#
# This examples show how to use pyAltmetric to make multiple calls for 
# citations using a list of DOIs (Digital Object Identifier).
#
from pyaltmetric import Altmetric, Citation
import json

# list of target DOIs 
dois = ('10.1038/news.2011.49', '10.1038/nj7361-479a', '10.1136/bmj.c6801',
        '10.1038/nature.2014.14583', '10.1038/news.2011.498')
citations = []

# initialize an Altmetric instance
a = Altmetric()

# iterate through DOIs fetching each citation from api.altmetric.com
# Altmetric will return None if there's no details available for the doi.
for i in dois: 
    citation = a.doi(i)
    citations.append(citation)

# write citation objects as json to a file
with open('citations_as_json.txt', 'w+') as outfile:
    json.dump(citations, outfile)