# Near Earth Objects

This use python to implement a command line tool that can inspect and query a dataset of Near Earth Objects and their close approaches to Earth.

### Overview

At a high-level, we'll break down this project into a few manageable tasks.

- Task 0: Inspect the data. (`data/neos.csv` and `data/cad.json`)
- Task 1: Build models to represent the data. (`models.py`)
- Task 2: Extract the data into a custom database (`extract.py` and `database.py`)
- Task 3: Create filters to query the database to generate a stream of matching `CloseApproach` objects, and limit the result size. (`filters.py` and `database.py`)
- Task 4: Save the data to a file. (`write.py`)
