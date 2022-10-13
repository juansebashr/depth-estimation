# Data available

## Get the data

To get the data, you have to install dvc (follow [this](https://dvc.org/doc/install) link) and configure the remote
bucket where the data is stored.

```
dvc remote add -d myremote gs://chiper-dvc/your_repo_name

dvc remote modify --local myremote \
        credentialpath 'path:\to\you\credentials\file.json' 
```

and then downloading using the following command:

`dvc pull`

## Data Dictionary

In this directory you will find the following data:

Insert the data that you're collecting, a little description and the date that you get it, remember, all the data files MUST be in the gitignore, only commit the .dvc files.
