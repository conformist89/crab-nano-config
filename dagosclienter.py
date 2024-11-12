import json
import os
import subprocess
import argparse
import re
import time

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--era", help="Data taking period, for now only Run 2 UL", type=str)

args = parser.parse_args()

# Record the start time
start_time = time.time()

def get_sample_type(sample):
    if 'SingleMuon' in sample:
        return 'data'
    elif 'TTTo' in sample:
        return 'ttbar'
    elif 'DYJets' in sample:
        return 'dyjets'
    elif 'WJets' in sample:
        return 'wjets'
    elif 'QCD' in sample:
        return 'qcd'
    elif 'WZTo2Q2L' in sample or 'WZTo3LNu' in sample or 'ZZTo2L2Nu' in sample or 'ZZTo2Q2L' in sample or 'ZZTo4L' in sample:
        return 'diboson'
    elif 'ST' in sample:
        return 'singletop'
    else:
        return 'other'
    
def get_nickname(sample):
    outstring = 'other'
    if 'SingleMuon' in sample:
        match = re.search(r"_(SingleMuon_Run2018[A-Z])_", sample)
        if match:
            outstring = match.group(1)
    else:
        match = re.search(r"/([^/]+)/", sample)
        outstring = match.group(1)
    return outstring

def get_xsec(sample):
    xsec = 1.0

    with open("xsec_proc_18UL.json", "r") as file:
        xsec_config = json.load(file)
        cross_sections = xsec_config.get("xsec2018UL", {})

        for dataset, xsec1 in cross_sections.items():
            if dataset == sample:
                xsec = xsec1

    return xsec

def get_sample_info(sample):
    command1 = 'dasgoclient -query="dataset dataset={} instance=prod/phys03" -json | grep "nfiles"'.format(sample)


    result = subprocess.run(command1, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output_das = result.stdout.split()[0]

    json_output = json.loads(output_das)

    nevents = json_output['dataset'][0]['nevents']
    nfiles = json_output['dataset'][0]['nfiles']
    dbs = json_output['dataset'][0]['name']
    era = args.era
    generator_weight = 1.0

    data = {}
    data['nevents'] = nevents
    data['nfiles'] = nfiles
    data['dbs'] = dbs
    data['era'] = era
    data['generator_weight'] = generator_weight
    data['sample_type'] = get_sample_type(sample)
    data['nick'] = get_nickname(sample)
    data['xsec'] = get_xsec(sample)

    return data



with open('nanofiles.json', 'r') as file:
    data = json.load(file)

# we need to parse the filelist
filelist = data['filelist'+args.era+'UL']


config_dict = {}
for file in filelist:
    short_nickname = get_nickname(file)
    config_dict[short_nickname] = get_sample_info(file)


# Write the dictionary to a JSON file
with open("datasets.json", "w") as file:
    json.dump(config_dict, file, indent=4)  # `indent=4` makes the file more readable
    
# Record the end time
end_time = time.time()

# Calculate the elapsed time
execution_time = (end_time - start_time) / 60
print(f"Execution time: {execution_time:.4f} minutes")