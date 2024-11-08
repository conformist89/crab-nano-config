import json
import os
import subprocess
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--era", help="Data taking period, for now only Run 2 UL", type=str)

args = parser.parse_args()


command1 = 'dasgoclient -query="dataset dataset=/SingleMuon/aakhmets-data_2018UL_singlemuon_SingleMuon_Run2018A_1729863731-00000000000000000000000000000000/USER instance=prod/phys03" -json | grep "nfiles"'


result = subprocess.run(command1, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

output_das = result.stdout.split()[0]

json_output = json.loads(output_das)

nevents = json_output['dataset'][0]['nevents']
nfiles = json_output['dataset'][0]['nfiles']
dbs = json_output['dataset'][0]['name']
era = args.era
generator_weight = 1.0

# print(nevents)
# print(nfiles)
# print(dbs)

# Start with an empty dictionary
data = {}
data['nevents'] = nevents
data['nfiles'] = nfiles
data['dbs'] = dbs
data['era'] = era
data['generator_weight'] = generator_weight

json_config = json.dumps(data, indent=4)
print("\nUpdated JSON String:")
print(json_config)


