import json
import os
import subprocess
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--era", help="Data taking period, for now only Run 2 UL", type=str)

args = parser.parse_args()

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
    elif 'WZTo2Q2L' in sample or 'WZTo3LNu' in sample or 'ZZTo2L2Nu' in sample or 'ZZTo2L2Q' in sample or 'ZZTo4L' in sample:
        return 'diboson'
    elif 'ST' in sample:
        return 'singletop'
    else:
        return 'other'

def get_sample_info(sample):
    pass
    sample = '/SingleMuon/aakhmets-data_2018UL_singlemuon_SingleMuon_Run2018A_1729863731-00000000000000000000000000000000/USER'
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
    data['type'] = get_sample_type(sample)

    json_config = json.dumps(data, indent=4)

    return json_config
    # print("\nUpdated JSON String:")
    # print(json_config)



with open('nanofiles.json', 'r') as file:
    data = json.load(file)

# we need to parse the filelist
filelist = data['filelist']

for file in filelist:
    print(get_sample_info(file))
    print("\n")