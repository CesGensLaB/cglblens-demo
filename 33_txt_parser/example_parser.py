def get_curves(lines):
    curves = []
    charts = []
    current_section = None
    current_series = []

    for line in lines:
        # Skip comments
        if line.startswith('#') or not line.strip():
            continue

        # Detect section headers
        if line.startswith('Section'):
            if current_section:
                curves.append({
                    "title": current_section,
                    "short_title": current_section,
                    "series": current_series
                })
                charts.append({
                    "title": current_section,
                    "xaxis": xaxis_label,
                    "yaxis": yaxis_label,
                    "curves": [len(curves) - 1]
                })
            current_section = line.strip()
            current_series = []
            continue

        # Skip headers
        if line.startswith('x,y'):
            xaxis_label, yaxis_label = line.strip().split(',')
            continue

        # Split the line into x and y values
        values = line.strip().split(',')
        current_series.append([float(values[0]), float(values[1])])

    # Add the last section
    if current_section:
        curves.append({
            "title": current_section,
            "short_title": current_section,
            "series": current_series
        })
        charts.append({
            "title": current_section,
            "xaxis": "X Axis Label",
            "yaxis": "Y Axis Label",
            "curves": [len(curves) - 1]
        })

    return {"curves": curves, "charts": charts}
