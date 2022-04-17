"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at
the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data
    about near-Earth objects.
    :neo: a list of near earth objects
    :return: A collection of `NearEarthObject`s.
    """
    neo = []
    with open(neo_csv_path) as file:
        readerr = csv.DictReader(file)
        for row in readerr:
            row["name"] = row["name"] or None
            row["diameter"] = float(row["diameter"]) if row["diameter"] else None
            neo.append(NearEarthObject(
                    designation=row["pdes"],
                    name=row["name"],
                    diameter=row["diameter"],
                    hazardous=row["pha"])
                )
    return neo


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about
    close approaches.
    :param approach: a list of close approach
    :return: A collection of `CloseApproach`es.
    """
    approach = []

    with open(cad_json_path) as file:
        data = json.load(file)

        for x in data["data"]:
            y = CloseApproach(**dict(zip(data["fields"], x)))
            approach.append(y)
    return approach
