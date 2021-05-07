def vegalite_piechart(n_pass, n_fail):
    pie = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
        "description": "A simple pie chart showing the ratio of passed and failed tests.",
        "data": {
            "values": [
                {"category": "pass", "value": n_pass},
                {"category": "fail", "value": n_fail},
            ]
        },
        "mark": "arc",
        "encoding": {
            "theta": {"field": "value", "type": "quantitative"},
            "color": {"field": "category", "type": "nominal"}
        }
    }
    return pie