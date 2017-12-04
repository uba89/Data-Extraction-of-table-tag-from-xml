from lxml import etree
#from StringIO import StringIO

f = open('level2.xml')
doc = etree.parse(f)
f.close()


for id in doc.xpath('//tables'):
    print ("TABL ")
    #print "TABL "
    print ("TABL    ", id.xpath('./@id')[0])
    for th in id.xpath('./table/tgroup/thead/row/entry//text()'):
        print ("TABL    ", th)
        #for ent in id.xpath('./table/tgroup/tbody/row/entry/descendant-or-self::text()'):
        #   print "TABL    ", ent
        for row in id.xpath('./table/tgroup/tbody/row'):
            entry_text=""
            for ent in row.xpath('entry/text()'):
                entry_text+=" "+ent
            print ("TABL    "+entry_text)




        #line = ' '.join(entry.text.strip() for entry in findall('entry'))
        #print "TABL    ", line




