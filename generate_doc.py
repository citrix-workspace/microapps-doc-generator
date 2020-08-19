#!/usr/bin/env python3

from collections import defaultdict
import json
import zipfile
import os
import argparse
import tempfile


def main(mappFile):
    # Create temporary folder and unzip bundle contents there
    with zipfile.ZipFile(mappFile, 'r') as zin:
        tmp = tempfile.TemporaryDirectory(dir=os.getcwd())
        zin.extractall(tmp.name)
        folder = tmp.name

    # Process metadata from metadata.json
    with open("{}/metadata.json".format(folder), "r") as metadata:
        metadata_json = json.load(metadata)
        title = metadata_json["title"]
        vendor = metadata_json["vendor"]
        description = metadata_json["description"]

    # Process data about the integration structure from sile.sapp
    with open("{}/file.sapp".format(folder), "r") as metadata:
        file_json = json.load(metadata)
        # endpoints = {"PUSH": {"/api/endpoint": [{table details}]}}
        endpoints = defaultdict(lambda: defaultdict(list))
        service_action_list = []

        # Process endpoints used for authentication
        def check_before_append(value, requestmethod="POST"):
            if value not in endpoints[requestmethod] and value != "":
                endpoints[requestmethod][value].extend([])

        check_before_append(file_json["services"][0]["configuration"]
                            ["security"]["authorizationURL"])

        check_before_append(file_json["services"][0]["configuration"]
                            ["security"]["tokenURL"])

        check_before_append(file_json["services"][0]["configuration"]
                            ["serviceActionSecurity"]["authorizationURL"])

        check_before_append(file_json["services"][0]["configuration"]
                            ["serviceActionSecurity"]["tokenURL"])

        # Build out a data structure of table relationships
        relationships = defaultdict(dict)
        for relationship in file_json["services"][0]["relationships"]:
            for pair in relationship["fkColumnPairs"]:
                (relationships[relationship["fkTable"]["title"]]
                    [pair["fkColumn"]["attributeName"]]) = "FK({}.{})".format(
                    relationship["pkTable"]["title"],
                    pair["pkColumn"]["attributeName"]
                )

        # Process other endpoints, build out a data structure which groups by
        # request method type and URI
        eps = file_json["services"][0]["configuration"]["dataEndpoints"]
        for endpoint in eps:
            tables = []
            for table in endpoint["tables"]:
                columns = []
                for column in table["columns"]:
                    # Build out descriptive string about the column
                    column_str = "*  {}: {}".format(
                        column["name"], column["columnType"]
                    )
                    if "length" in column:
                        column_str += "({})".format(column["length"])
                    if "role" in column and column["role"] == "PRIMARY_KEY":
                        column_str += ", PK"
                    # Lookup column in foreign key relationships dict
                    if table["tableName"] in relationships:
                        if column["name"] in relationships[table["tableName"]]:
                            column_str += ", {}".format(
                                relationships[table["tableName"]]
                                [column["name"]]
                            )
                    if column["ignored"]:
                        column_str += ", IGNORED"
                    columns.append(column_str)
                tables.append({"name": table["tableName"], "fields": columns})
            (
                endpoints[endpoint["requestMethod"]][endpoint["endpoint"]]
            ).extend(tables)

        # Process service actions, add details to endpoints list and seperate
        # service action name list
        actions = file_json["services"][0]["configuration"]["serviceActions"]
        for action in actions:
            endpoints[action["requestMethod"]][action["endpoint"]].extend([])
            service_action_list.append(action["name"])

    # Build connector specification output file
    output_file = "{}-connector-specifications.md".format(
        title.replace(" ", "-")
        )
    with open(output_file, "w") as md:
        md.write("---\nlayout: doc\n---\n\n")
        md.write("# {} {} specifications\n\n".format(vendor, title))
        md.write("{}\n\n".format(description))
        md.write("# Version Details\n\n")
        md.write("INSERT VERSION SUPPORT DETAILS HERE\n\n")
        md.write("## Endpoints\n\n\n")
        for k, v in endpoints.items():
            md.write("{}\n\n".format(k))
            for endpoint in v.keys():
                md.write("    {}\n".format(endpoint))
            md.write("\n")
        md.write("## Service Actions\n\n")
        for service_action in service_action_list:
            md.write("*  **{}** - INSERT SERVICE ACTION DESCRIPTION\n".format(
                service_action
                ))
        md.write("\n")
        md.write("## Key Entities\n\n")
        md.write("The following are the main business entities that this \
            connector addresses:\n\n")
        md.write("*  INSERT LIST OF MAIN BUSINESS ENTITIES\n\n")
        md.write("## Entities with Attributes\n\n")
        md.write("The following is a full list of entities and their \
            attributes:\n\n")
        for k, v in endpoints.items():
            for tables in v.values():
                for table in tables:
                    if "fields" in table:
                        md.write("{}\n\n".format(table["name"]))
                        for field in table["fields"]:
                            md.write("{}\n".format(field))
                        md.write("\n")

    # Build out integration guide document
    with open("templates/integrate-template.md", "r") as template:
        output_doc = "integrate-{}.md".format(title.replace(" ", "-"))
        with open(output_doc, "w") as md:
            for line in template.readlines():
                md.write("{}".format(line.replace("INSERT_SOR_NAME", title)))

    tmp.cleanup()


if __name__ == "__main__":
    # python3 generate_doc.py --file ServiceNowHTTPnew.service.mapp
    parser = argparse.ArgumentParser(description='Generate documentation \
        templates for a bundle export')
    parser.add_argument('--file', dest='mappFile', help='name and location of \
        the mapp export file')

    args = parser.parse_args()
    main(args.mappFile)
