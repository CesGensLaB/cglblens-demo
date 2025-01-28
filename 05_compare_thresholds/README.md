# Run Compare by using float thresholds

## Instructions

1. `cd` to this folder
2. Run `cglblens run .`

## Explanations

Here are four test cases to demonstrate how `float_thresholds` work:

### Case 1: Value of test is greater than `relative_vs_absolute_min` (using relative error) and there is an error

- Reference value: `1.0`
- Test value: `1.02`
- Absolute difference: `|1.02 - 1.0| = 0.02`
- Relative difference: `0.02 / 1.0 = 0.02`

The relative difference `0.02` is greater than `relative_error_max` (0.01), so there is an error.

### Case 2: Value of test is greater than `relative_vs_absolute_min` (using relative error) and there is no error

- Reference value: `1.0`
- Test value: `1.005`
- Absolute difference: `|1.005 - 1.0| = 0.005`
- Relative difference: `0.005 / 1.0 = 0.005`

The relative difference `0.005` is less than `relative_error_max` (0.01), so there is no error but a warning.

### Case 3: Value of test is less than `relative_vs_absolute_min` (using absolute error) and there is an error

- Reference value: `0.001`
- Test value: `0.002`
- Absolute difference: `|0.002 - 0.001| = 0.001`

The absolute difference `0.001` is greater than `absolute_error_max` (0.001), so there is an error.

### Case 4: Value of test is less than `relative_vs_absolute_min` (using absolute error) and there is no error

- Reference value: `0.001`
- Test value: `0.0015`
- Absolute difference: `|0.0015 - 0.001| = 0.0005`

The absolute difference `0.0005` is less than `absolute_error_max` (0.001), so there is no error but a warning.

