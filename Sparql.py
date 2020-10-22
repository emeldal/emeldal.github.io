from datetime import datetime as dt

from SPARQLWrapper import SPARQLWrapper, JSON

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?person ?personLabel ?dateBirth ?dateDeath WHERE {
        ?person wdt:P27 wd:Q31 .
        ?person wdt:P106 wd:Q36180 .
        ?person wdt:P569 ?dateBirth .
        OPTIONAL {?person wdt:P570 ?dateDeath .}
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    }
    ORDER BY ?personLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Belgian writers found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n writers (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    if name_filter:
        rows = [row for row in rows if name_filter in row['personLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            birth_date = dt.strptime(row['dateBirth']['value'], date_format)
            birth_year = birth_date.year
        except ValueError:
            birth_year = "????"
        try:
            death_date = dt.strptime(row['dateDeath']['value'], date_format)
            death_year = death_date.year
        except ValueError: # unknown death date
            death_year = "????"
        except KeyError: # still alive
            death_year = ""
        print(f"{row['personLabel']['value']} ({birth_year}-{death_year})")

rows = get_rows()

show(rows, n=30)