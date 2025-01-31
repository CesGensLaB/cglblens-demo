# Run Download, Execute and Compare

**Linux Only**
(the command sh)

## Instructions

1. `cd` to this folder
2. Run `cglblens run .`

## Explainations
In this configuration, we specify a URL to download the executable for the reference test. The `executable_url` field uses a conditional statement to determine the appropriate file extension based on the operating system.

### Executable URL

The `executable_url` is set to:

https://raw.githubusercontent.com/CesGensLaB/cglblens-demo/refs/heads/main/assets/exe/mock_reference_txt.{% if sys.os == 'linux' %}sh{% endif %}{% if sys.os == 'windows' %}bat{% endif %}


This URL points to the location of the executable script:

- If the operating system is Linux (`sys.os == 'linux'`), the URL will end with `.sh`, indicating a shell script.
- If the operating system is Windows (`sys.os == 'windows'`), the URL will end with `.bat`, indicating a batch script.


