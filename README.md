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

This will give you a config file `datasets.json` with json dictionary with the information from DAS that has a following structure

```
    "DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8": {
        "nevents": 79621344,
        "nfiles": 80,
        "dbs": "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/aakhmets-mc_2018UL_dy_DYJetsToLL_LHEFilterPtZ-100To250_1729599421-00000000000000000000000000000000/USER",
        "era": "2018",
        "generator_weight": 1.0,
        "sample_type": "dyjets",
        "nick": "DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
        "xsec": 96.23
    }
```

After creating the general config file `datasets.json`, we can create the config files with the filelist for every sample. By default the same type samples (like `dyjets`) are saved withing the same folder and the name of the file is the same as its nickname. For instance, `/work/olavoryk/helper_files/crab-nano-config/dyjets/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8.json` . This config file has the following structure:

```
{
    "nevents": 79621344,
    "nfiles": 80,
    "dbs": "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/aakhmets-mc_2018UL_dy_DYJetsToLL_LHEFilterPtZ-100To250_1729599421-00000000000000000000000000000000/USER",
    "era": "2018",
    "generator_weight": 1.0,
    "sample_type": "dyjets",
    "nick": "DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "xsec": 96.23,
    "filelist": [
        "root://cmsdcache-kit-disk.gridka.de//store/user/aakhmets/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/mc_2018UL_dy_DYJetsToLL_LHEFilterPtZ-100To250_1729599421/241022_205051/0000/nanosim_33.root",
        "root://cmsdcache-kit-disk.gridka.de//store/user/aakhmets/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/mc_2018UL_dy_DYJetsToLL_LHEFilterPtZ-100To250_1729599421/241022_205051/0000/nanosim_22.root",
        "root://cmsdcache-kit-disk.gridka.de//store/user/aakhmets/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/mc_2018UL_dy_DYJetsToLL_LHEFilterPtZ-100To250_1729599421/241022_205051/0000/nanosim_23.root",
    ]
}
```

To create it, make sure that `datasets.json` exists. Then simple:

```
python3 filelist.py --era 2018
```