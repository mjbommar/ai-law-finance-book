# Chapter: Knowledge Graphs & Semantic Web - Foundations

**Subtitle**: RDF, RDFS/OWL, SKOS, SPARQL, SHACL, JSON-LD

## Overview

This chapter introduces core Semantic Web technologies that support durable identifiers, typed relations, validation, and query. Examples are aligned to legal and financial data and connect to the book's Evidence Record framework.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 1 | `sections/linked_data.tex` | Linked Data Principles |
| 2 | `sections/rdf_rdfs_owl.tex` | RDF Data Model and RDFS/OWL |
| 3 | `sections/skos.tex` | SKOS for Taxonomies and Thesauri |
| 4 | `sections/sparql.tex` | SPARQL Query, Update, and Federation |
| 5 | `sections/shacl.tex` | Validation with SHACL |
| 6 | `sections/jsonld.tex` | JSON-LD for Web Interop |
| 7 | `sections/identifiers_vocab.tex` | Domain Identifiers and Vocabularies |
| 8 | `sections/publishing_best_practices.tex` | Publishing and Cataloging |

## Files

```
09-kg-foundations/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
└── sections/             # Section content
    ├── linked_data.tex
    ├── rdf_rdfs_owl.tex
    ├── skos.tex
    ├── sparql.tex
    ├── shacl.tex
    ├── jsonld.tex
    ├── identifiers_vocab.tex
    └── publishing_best_practices.tex
```

## Building

From chapter directory:
```bash
make pdf      # Build standalone chapter PDF
make clean    # Remove auxiliary files
```

From repository root:
```bash
make chapters # Build all chapter PDFs
```
