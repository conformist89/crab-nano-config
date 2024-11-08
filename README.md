# crab-nano-config
Makes a configuration files for the nano AOD 

Execution

One needs to source `dagosclient` beforehand

```
source /cvmfs/cms.cern.ch/cmsset_default.sh
```

```
python3 dagosclienter.py --era 2018UL
```

This will give you a json dictionary with the information from DAS

```
{
    "nevents": 241605557,
    "nfiles": 594,
    "dbs": "/SingleMuon/aakhmets-data_2018UL_singlemuon_SingleMuon_Run2018A_1729863731-00000000000000000000000000000000/USER",
    "era": "2018",
    "generator_weight": 1.0
}
```