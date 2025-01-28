# Run Compare and Execute with additional path suffix

**Linux Only**
(the command sh)

## Instructions

1. `cd` to this folder
2. Run `cglblens run .`

## Explainations


This example demonstrates the capability of the configuration parameter `compare.sources.additional_path_suffix`.

cglblens will 

- run `mock_test_txt.sh`  in a new `test` folder and `mock_reference_txt.sh` in a new `reference` folder which will generate 4 files `cglblens_generated_data.txt`+ log files at a file structure depth of 2.

- compare the 2 files `cglblens_generated_data.txt` and generate an html report

- 1 error will be found.
