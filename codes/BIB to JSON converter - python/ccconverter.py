from pybtex.database.input import bibtex
import json

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("6238.bib")
x=1;

#loop through the individual references
#here iterated from article to article
for bib_id in bibdata.entries:
        #print (bibdata.entries[bib_id])
        namelist= (bibdata.entries[bib_id].persons[u'author'])
        new_namelist = []
        for name in namelist :
            strnname= str(name)
            new_namelist.append (strnname)

        if (bibdata.entries[bib_id].type) == 'article' :



            dict = {"type": bibdata.entries[bib_id].type,
              "title" : bibdata.entries[bib_id].fields[u'title'],
              "abstract" : "" ,
              "year": bibdata.entries[bib_id].fields[u'year'], 
              "Authors":new_namelist
                    #list[]
            ##                    "name": ""
            ##                    "email": ""
            ##                    "E number": #optional
            ##                    "affiliation": ""
                      ,
            ##              "venue":{"journal" : bibdata.entries[bib_id].fields[u'journal'] ,
            ##                    "volume" : bibdata.entries[bib_id].fields[u'volume']} ,
              "venue":{
                    "journal" : bibdata.entries[bib_id].fields[u'journal'] ,
                    "volume" : bibdata.entries[bib_id].fields[u'volume']
                    } ,
              "DOI": "",
              "pdf": "",#as a link
              "pblication url" : bibdata.entries[bib_id].fields[u'url'],
              "presentation": "" ,#optional(in a conference)
              "code": "", # git repo ,
              "tags": "",#as a list
              }

        elif (bibdata.entries[bib_id].type) == 'inproceedings' :

            
            dict = {"type": bibdata.entries[bib_id].type,
                  "title" : bibdata.entries[bib_id].fields[u'title'],
                  "book title" : bibdata.entries[bib_id].fields[u'booktitle'],
                  "abstract" : "" ,
                  "year": bibdata.entries[bib_id].fields[u'year'], 
                  "Authors":new_namelist,
                        #list[]
            ##                    "name": ""
            ##                    "email": ""
            ##                    "E number": #optional
            ##                    "affiliation": ""
                          
##                  "publisher" : bibdata.entries[bib_id].fields[u'publisher'] ,
##                  "DOI": bibdata.entries[bib_id].fields[u'doi'],
                  "DOI" : "",  
                  "pdf": "",#as a link
                  "pblication url" : bibdata.entries[bib_id].fields[u'url'],
                  "presentation": "" ,#optional(in a conference)
                  "code": "", # git repo ,
                  "tags": "",#as a list
                  }

        elif (bibdata.entries[bib_id].type) == 'phdthesis' :

            
            dict = {"type": bibdata.entries[bib_id].type,
                  "title" : bibdata.entries[bib_id].fields[u'title'],
                  "book title" : "",
                  "abstract" : "" ,
                  "year": bibdata.entries[bib_id].fields[u'year'], 
                  "Authors":new_namelist,
                        #list[]
            ##                    "name": ""
            ##                    "email": ""
            ##                    "E number": #optional
            ##                    "affiliation": ""
                          
##                  "publisher" : bibdata.entries[bib_id].fields[u'publisher'] ,
##                  "DOI": bibdata.entries[bib_id].fields[u'doi'],
                  "DOI" : "",  
                  "pdf": "",#as a link
                  "pblication url" : bibdata.entries[bib_id].fields[u'url'],
                  "presentation": "" ,#optional(in a conference)
                  "code": "", # git repo ,
                  "tags": "",#as a list
                  }

            
        else:
            print(bibdata.entries[bib_id].type)
            print ("\n")
            print ("\n")
            
        json_object = json.dumps(dict, indent = 4)
      
        # Writing to sample.json
        filename = '%s.json'%(x)
        with open(filename, "w") as jsonfile:
          jsonfile.write(json_object)
        x+=1
        print (x)
