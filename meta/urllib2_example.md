out = urllib2.urlopen('http://pds-imaging.jpl.nasa.gov/data/mer/opportunity/mer1po_0xxx/data/sol0001/rdr/')

code = out.read()

code.find('.img')

code[1500:1526]
