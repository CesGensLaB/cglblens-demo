# Run Compare with --collect-depth 

## Instructions

1. `cd` to this folder
2. Run with `--collect-depth`: `cglblens run --collect-depth 2 .`

## Explanations

Here the folders structure:

```
/03_collect_depth_and_compare
    /depth_1
        /01_no_difference
            /reference
                co2_emissions.csv
            /test
                co2_emissions.csv
        /02_differences
            /reference
                co2_emissions.csv
            /test
                co2_emissions.csv
        /99_override
            /reference
                co2_emissions.csv
            /test
                co2_emissions.csv
            cglblens.yml
    cglblens.yml
```

With `--collect-depth` cglblens will 
1. search and find for config file in `.` path
2. and execute with this config in the working directories at depth `2` from `.` path :
    - `depth_1/01_no_difference`
    - `depth_1/02_differences`
    - for `depth_1/99_override` there is another config file defined too: in this case, the values defined in this this config will ovveride the main one from 1 (here genereate a json report instead of an html report)