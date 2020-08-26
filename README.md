# Details

generate_doc.py is a script that takes an exported microapp integration file
as input and produces a markdown (.md) file that documents the functionality of
the integration. This automated approach provides:

-  standardisation of documentation
-  writes the boiler plate structure for you, saving time

Once the script has run, simply open your markdown documentation file and
fill in the remaining pieces of information required, as indicated by the
instructions in capital letters throughout the document.

# How to generate document templates

1. Export your integration
1. Copy the integration export file (*.mapp) to this directory
1. Run the "generate_doc.py" script by running: python3 generate_doc.py --file {export file name}.mapp
1. The templates will then be generated in the directory with the name scheme: integrate-{integration name}.md and {integration name}-connector-specifications.md
1. Fill in all extra details required by the template, this is indicated with CAPITALIZED LETTERS