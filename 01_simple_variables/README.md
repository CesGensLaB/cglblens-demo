# Run Simple Compare

## Instructions

1. `cd` to this folder
2. Run `cglblens --log-level=DEBUG run .`

## Explainations

cglblens will compare :

- the 2 files `co2_emissions.csv`, and find 3 comparison errors
- the 2 files `data.txt`, and find 1 comparison errors
- generate an html report

You can see the template strings applied:

```log
2024-12-16 08:29:10 93cc657e72cb root[262] DEBUG with config {
    "processor": "Compare",
    "variables": {
        "parameter_1": "parameter_1_value",
        "parameter_2": "parameter_2_value parameter_1_value",
        "env_home": "/root",
        "python_version": "3.11.2",
        "os_arch": "linux_x86_64"
    },
    "tags": [
        "csv",
        "txt",
        "simple"
    ],
```
from the configuration file
```yaml
variables:
  parameter_1: parameter_1_value
  parameter_2: "parameter_2_value {{ vars.parameter_1}}"
  env_home: "{{ env.HOME }}"
  python_version: "{{ sys.python }}"
  os_arch: "{{ sys.os }}_{{ sys.arch }}"
```
In this configuration file, several variables are defined to make the configuration more flexible and maintainable. Here is an explanation of each variable:

### `parameter_1`
- **Description**: A simple variable with a static value.
- **Value**: `parameter_1_value`

### `parameter_2`
- **Description**: A variable that combines a static value with the value of `parameter_1`.
- **Value**: `parameter_2_value parameter_1_value`
- **Usage**: This demonstrates how to create a variable that includes another variable's value.

### `env_home`
- **Description**: A variable that retrieves the value of the `HOME` environment variable.
- **Value**: The home directory of the current user.
- **Usage**: Useful for referencing user-specific paths.

### `python_version`
- **Description**: A variable that retrieves the current Python version.
- **Value**: The version of Python being used to run the script.
- **Usage**: Useful for ensuring compatibility or logging the Python version.

### `os_arch`
- **Description**: A variable that combines the operating system name and architecture.
- **Value**: A string in the format `os_architecture`.
- **Usage**: Useful for logging or conditional configurations based on the operating system and architecture.

These variables can be referenced throughout the configuration file to dynamically insert their values, making the configuration more adaptable to different environments and use cases.