# Details

Microapp integration developers can use this tool to create user-facing documentation 
of their microapp integration.

The tool will prepopulate a template with various elements (e.g service actions and
endpoints) extracted from the microapp bundle.

This automated approach provides:

-  Standardisation of documentation across integrations
-  Time saving by creating the boiler plate structure for you

See this [ServiceNow documentation](https://docs.citrix.com/en-us/citrix-microapps/downloads/servicenow-http-connector-specifications.html) for an example of documentation written using this script:

# How to generate document templates

1. Export your integration
1. Copy the integration export file (.mapp) to this directory
1. Run the "generate_doc.py" script by running: python3 generate_doc.py --file {export file name}.mapp
1. The templates will then be generated in the same directory: integrate-{integration name}.md and {integration name}-connector-specifications.md

# After generating the template

Once the script has run, open your markdown documentation files and fill in the
remaining pieces of information required, as indicated by the instructions in capital
letters throughout the document.