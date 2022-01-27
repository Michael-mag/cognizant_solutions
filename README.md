### HOW TO RUN THE CODE:
- after unpacking the zip folder:
  - open pycharm's integrated terminal, or any terminal (unix os)
  - navigate to the root of the package
  - The command: ```ls``` should show some of these:
    - directories: src, tests, ...
    - files: Makefile, README.md, ...
  - In this path, run either one of the following 2 commands: 
    1. ```make install``` 
      - This installs all the dependencies and installs the source code as
       a python package.
      - The above command also creates a virtual environment, which needs to be activated using the command:
        - ```source .venv/bin/activate```
    2. Or if pip is available, run the following commands:
       - ```python -m venv venv```
       - ```source venv/bin/activate```
       - ```pip install -e .```
  - Next, from the same path, run: ```pytest -s tests```
  - After the command is done, the command: ```ls``` should show two new files created:
     1. results.xlsx: output file for comparing to excel files
     2. converted_xml_file.xlsx: output file after parsing the given xml file
