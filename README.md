# Details

*  generate_doc.py - code for automatically generating doc templates

# How to generate document templates

1. Export your integration
1. Copy the integration export file (*.mapp) to this directory
1. Run the "generate_doc.py" script by running: python3 generate_doc.py --file {export file name}.mapp
1. The templates will then be generate in the directory with the name scheme: integrate-{integration name}.md and {integration name}-connector-specifications.md
1. Fill in all extra details required by the template, this is indicated with CAPITALIZED LETTERS