# Design Points

## Summary 

This is a model for a pluggable API that allows provisioning of search as plug-in modules. 

A plug in provides a straight-forward way of building free or guided searches against a search index. The search will translate user 
specificiation of a search in a simple form that works in a text box or search builder into a query that can be run against a back
end search index. An example would be a text box on a form with free text or field:search value. The API implementation is responsible 
for turning search definitions into an appropriate back-end DSL or formal query, using reasonable defaulting. Query results are to be returned
in a standard row format that can be used in a 'virtual collection' style listening or a more generic search result listing. The listing
can include add'l metadata beyond the collection/file name/size/create date/modify date in an additional info addendum to the row.


## Links and Dev Notes

* JWT example for Flask - https://github.com/zalando/connexion/tree/master/examples/openapi3/jwt

## Operations

A search plugin is a REST API that conforms to 
this Swagger API definition. The REST API performs the following function:

### Describe the search 'option'

GET /info

array of title, description

A search API will advertise a title and description for the search. This can be used in an interface to provide a search category for things like
drop-down selectors, it also can provide a mouse-over or user prompt for the type of search.

A client to these search API could initialize by pinging the provided search endpoints to gather a comprehensive search options menu.

### Describe the search fields/types/description/example for a searchabe field in the target schema.

GET /schema/SEARCHID

Returns a JSON structure with the search options

### Execute a search

returns a JSON description of the searchable fields with info

POST /search/SEARCHID

Posts a simple JSON structure containing a free text string that is a search term. The search can contain TERMNAME:SEARCHTERM strings
that are understood by the search schema.

This returns a row/column search result as described above. The search could include paging offets and limits.

### Execute an advanced search

POST /advancedsearch/SEARCHID

POSTS a JSON structure with an array of field name and search term, along with AND/OR connectors. The API is not currently planned to support nesting parens.

This returns a row/colunn search as described above. The search could include paging offets and limits.
