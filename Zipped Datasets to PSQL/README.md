The goal of this project was to work replicating a simplified version of staging areas for zipped data files. It aims to have two main sessions of code:
The first one deals with the zip files and organizes its contents and the second one is in charge of handling the files to a PostgreSQL database running in a Docker container.

The downloads folder is separated from the datasets and the logs, in a similar way as a S3 Bucket inside AWS. From there, the zipped files are extracted to its respective folders inside the Datasets folder, and a log file is generated or appended. 
In case of the files already existed, they are skipped.

The gif below shows the code running inside a notebook:
![export](https://user-images.githubusercontent.com/103280317/221058517-5a2268e1-9b97-4663-8654-18e66bc80be3.gif)
