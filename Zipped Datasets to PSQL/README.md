The goal of this project was to work replicating a simplified version of staging areas for zipped data files. It aims to have two main sessions of code:
The first one deals with the zip files and organizes its contents and the second one is in charge of handling the files to a PostgreSQL database running in a Docker container.

The downloads folder is separated from the datasets and the logs, in a similar way as a S3 Bucket inside AWS. From there, the zipped files are extracted to its respective folders inside the Datasets folder, and a log file is generated or appended. 
In case of the files already existed, they are skipped.
