from pyaltmetric import Altmetric, Citation, HTTPException
import csv

# initialize Altmetric
a = Altmetric()

with open('doi.list', 'r') as infile:
    with open('results.csv', 'w') as outfile:
        writer = csv.writer(outfile)

        for x in infile:
            x = x.rstrip() 
            # search for article using doi
            c = a.doi(x)
            if c:
                # initialize Citation and fetch fields
                citation = Citation(c)
                result = citation.get_fields('title', 'doi', 'journal',
                            'cited_by_posts_count', 'cited_by_tweeters_count',
                            'cited_by_fbwalls_count', 'cited_by_gplus_count',
                            'cited_by_rdts_count', 'cited_by_feeds_count')
            else:
                result = [x, 'no data']
            # write row to file 
            writer.writerow(result)

