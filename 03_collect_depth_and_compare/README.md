# Run Compare with --discover and --tag

## Instructions

1. `cd` to this folder
2. Run with `--collect-depth`: `cglblens run --collect-depth 2 .`

## Explainations

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
    cglblens.yml
```
With `--collect-depth` cglblens will search for config file in . and execute with this config in the working directories at depth 2 from . path, i.e `depth_1/01_no_difference` and `depth_1/02_differences`.