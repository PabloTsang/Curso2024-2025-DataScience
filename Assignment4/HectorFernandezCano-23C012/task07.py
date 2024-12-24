# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YL7evHIoZwEhk7f9zNBrSaKJWl1mz13k

**Task 07: Querying RDF(s)**
"""

# !pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

for s,p,o in g:
  print(s,p,o)

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace('http://somewhere/#')
q1 = prepareQuery('''
    SELECT ?living WHERE{
      ?living rdfs:subClassOf ns:LivingThing.
    }
    ''',
    initNs= {"ns" : ns, "rdfs": RDFS}
    )

for r in g.query(q1):
    print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace('http://somewhere/#')
q2 = prepareQuery('''
  SELECT ?person WHERE{
    {
    ?person rdf:type ns:Person.
    } UNION {
    ?subclase rdfs:subClassOf ns:Person.
    ?person2 rdf:type ?subclase.
    }
    }
    ''',
    initNs= {"ns": ns, "rdf":RDF, "rdfs": RDFS}
)
for r in g.query(q2):
  print(r.person1, r.person2)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

from rdflib.plugins.sparql import prepareQuery
ns =  Namespace('http://somewhere/#')
q3 = prepareQuery('''
  SELECT ?person ?animal WHERE{
    {?person rdf:type ns:Person.}
    UNION {
      ?animal rdf:type ns:Animal
    }
      }
  ''',
      initNs = {"ns": ns, "rdf": RDF}
)
for r in g.query(q3):
  print(r.person, r.animal)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace('http://somewhere/#')
foaf= Namespace('http://xmlns.com/foaf/spec/#')
q4 = prepareQuery('''
  SELECT ?person WHERE{
    ?person foaf:knows ns:RockySmith.
  }
''',
initNs = {'ns': ns, 'foaf': foaf}
)
for r in g.query(q4):
  print(r.person)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace('http://somewhere/#')
foaf = Namespace('http://xmlns.com/foaf/spec/#')
q5 = prepareQuery('''
  SELECT ?animal1 WHERE{
    ?animal1 rdf:type ns:Animal.
    ?animal2 rdf:type ns:Animal.
    ?animal1 foaf:knows ?animal2.
  }
''',
    initNs = {"foaf":foaf, "ns": ns})
for r in g.query(q5):
  print(r.animal1)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace('http://somewhere/#')
foaf =  Namespace('http://xmlns.com/foaf/spec/#')
q6 = prepareQuery('''
  SELECT ?age WHERE{
    ?lvinig_thing rdf:type ns:LivingThing.
    ?living_thing foaf:age ?age.
  }
  ORDER BY DESC(?age)
''',
    initNs = {"ns":ns,"foaf": foaf}
)
for r in g.query(q6):
  print(r.age)