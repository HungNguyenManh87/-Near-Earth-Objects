"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    #  Load NEO data from the given CSV file.
    NEOs=[]
    with open(neo_csv_path,'r') as neofile:
        reader=csv.DictReader(neofile)
        for row in reader:
            Neo=NearEarthObject(designation=row["pdes"],name=row["name"],diameter=row["diameter"],hazardous=row["pha"])
            NEOs.append(Neo)
    return (NEOs)


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    CLAPs=[]
    # Load close approach data from the given JSON file.
    with open(cad_json_path,'r') as jsofile:
        contents=json.load(jsofile)
        i=0
        while i < len(contents["data"]):
            CLAP=CloseApproach(designation=contents["data"][i][0],time=contents["data"][i][3],distance=contents["data"][i][4],velocity=contents["data"][i][7])
            CLAPs.append(CLAP)
            i = i + 1
    return (CLAPs)
