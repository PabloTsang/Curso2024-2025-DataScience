# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qdAlubcR--ZimEnZnqexk-TzbhGQeXAn

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal, FOAF
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smithers"**"""

g.add((ns.JaneSmithers, RDF.type, ns.Researcher))
g.add((ns.JaneSmithers, FOAF.name, Literal("Jane Smithers") ))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmithers the email address, fullName, given and family names. Use the https://schema.org vocabulary**"""

g.namespace_manager.bind('sc', Namespace("https://schema.org/"), override=False)
sc = Namespace("https://schema.org/")
g.add((ns.JaneSmithers, sc.email, Literal("js@gmail.com")))
g.add((ns.JaneSmithers, VCARD.fullName, Literal("Jane Smithers")))
g.add((ns.JaneSmithers, sc.givenName, Literal("Jane")))
g.add((ns.JaneSmithers, sc.familyName, Literal("Smithers")))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works. Use the "https://example.org/ namespace**"""

g.add((ns.JaneSmithers, sc.affiliation, Literal("UPM")))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**Task 6.6: Add that John knows Jane using the FOAF vocabulary. Make sure the relationship exists.**"""

FOAF = Namespace("http://xmlns.com/foaf/0.1/")
g.add((ns.JohnSmith, FOAF.knows, ns.JaneSmithers))
# Visualize the results
for s, p, o in g:
  print(s,p,o)