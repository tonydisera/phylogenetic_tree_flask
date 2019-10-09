from flask import Flask, render_template
app = Flask(__name__)
import pandas as pd
import os
import numpy as np

APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/getSpeciesData")
def getSpeciesData():
    speciesFileName = "static/data/species_multialign_info.csv"

    # Load the CSV file from the static folder, inside the current path
    species = pd.read_csv(os.path.join(APP_FOLDER,speciesFileName))

    species['genome_size']    = np.round((species['size'] /10**6),0) * 10**6;
    species['genome_size']    = species['genome_size'].apply(np.int64);

    species['genome_size_mb'] = np.round((species['genome_size'] /100 * 100),0) / 10**6;
    species['genome_size_mb'] = species['genome_size_mb'].apply(np.int64);

    # show the post with the given id, the id is an integer
    return species.to_json(orient='records')

@app.route("/getPhylogenyData")
def getPhyologenyData():
    phylogenyFileName = APP_FOLDER + "/static/data/hg19.100way.commonNames.nh"
    str = open(phylogenyFileName, "r").read()
    return str;
