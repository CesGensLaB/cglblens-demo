# Run Compare with --discover and --tag

## Instructions

1. `cd` to this folder
2. Test A - Run with discover `cglblens run --discover .`
3. Test B - Run with discover and tags `cglblens run --discover --tag differences .`
4. Test C - Run with discover and tags `cglblens run --discover --tag differences --tag no_difference .`

## Explainations

For reminder, the tags defined in `cglblens.yml` i

`01_no_difference/cglblens.yml`

```yaml
processor: Compare
tags: [csv, no_difference]
report:
  ...
```

`02_differences/cglblens.yml`

```yaml
processor: Compare
tags: [csv, differences]
report:
  ...
```

### Test A

Running `cglblens run --discover .` will find 2 configuration files `cglblens.yml` in `01_no_difference` and `02_differences` subfolders and execute them.

### Test B

Running `cglblens run --discover --tag differences .` will find 2 configuration files `cglblens.yml` in `01_no_difference` and `02_differences` subfolders, but only `02_differences/cglblens.yml` has a tag `differences` defined in it, then execute only this one.

### Test C

Running `cglblens run --discover --tag differences --tag no_difference .` will find 2 configuration files `cglblens.yml` in `01_no_difference` and `02_differences` subfolders, and execute them both, as `02_differences/cglblens.yml` has a tag `differences` and `01_no_difference/cglblens.yml` has a tag `no_difference` 
