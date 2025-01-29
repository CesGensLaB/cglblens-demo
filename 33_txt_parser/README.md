# Run Compare with a custom parser

**Linux Only**
(the command sh)

## Instructions

1. `cd` to this folder
2. Run `cglblens run .`

## Explanations

In this use case of cglblens, we use a custom parser (written in Python) that takes `lines` as input and outputs in the following format:

### Returned by the parser

A dictionary with keys:
- `curves`: list[CurveObject]
- `charts`: list[ChartObject]

### CurveObject
A dictionary with keys:
- `title`: str
- `short_title`: str
- `series`: list[list[float, float]] # list of x,y pairs

### ChartObject
A dictionary with keys:
- `title`: str
- `xaxis`: str
- `yaxis`: str
- `curves`: list[int] # indices referencing the `curves` list in the root

### Complete Example

This example is based on the parser used in our case with the `data.txt` file from our scenario.

```json
{
    "curves": [
        {
            "title": "Section 1",
            "short_title": "Section 1",
            "series": [
                [1.0, 2.0],
                [2.0, 4.0],
                [3.0, 6.0]
            ]
        },
        {
            "title": "Section 2",
            "short_title": "Section 2",
            "series": [
                [4.0, 8.0],
                [5.0, 10.0],
                [6.0, 12.0]
            ]
        },
        {
            "title": "Section 3",
            "short_title": "Section 3",
            "series": [
                [7.0, 14.0],
                [8.0, 16.0],
                [9.0, 18.0]
            ]
        }
    ],
    "charts": [
        {
            "title": "Section 1",
            "xaxis": "x",
            "yaxis": "y",
            "curves": [0]
        },
        {
            "title": "Section 2",
            "xaxis": "x",
            "yaxis": "y",
            "curves": [1]
        },
        {
            "title": "Section 3",
            "xaxis": "x",
            "yaxis": "y",
            "curves": [2]
        }
    ]
}