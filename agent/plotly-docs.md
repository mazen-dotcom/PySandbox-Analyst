 Plotly.js JSON Chart Schema — Complete Reference

> This document describes every Plotly chart purely as a **JSON object**. Every chart is a plain JSON structure with `data`, `layout`, and optionally `config` and `frames`.

---

## 1. Top-Level Figure Structure

```json
{
  "data": [ ... ],
  "layout": { ... },
  "config": { ... },
  "frames": [ ... ]
}
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `data` | `array` of trace objects | Yes | One or more trace objects describing each series |
| `layout` | `object` | Yes | Non-data visual attributes: title, axes, legend, annotations, shapes, etc. |
| `config` | `object` | No | High-level configuration: modebar, scroll/zoom, locale, static output |
| `frames` | `array` of frame objects | No | Animation frames, each can contain `data` and `layout` changes |

---

## 2. Trace Types (the `data` array)

Each element in `data` is a **trace object**. The `"type"` field selects the chart kind. Below is every trace type available in plotly.js v3.x.

### 2.1 Cartesian Traces (2D x/y axes)

#### `"scatter"` — Line, scatter, text, and bubble charts

```json
{
  "type": "scatter",
  "x": [1, 2, 3, 4],
  "y": [10, 15, 13, 17],
  "mode": "lines+markers+text",
  "name": "Series A",
  "text": ["a", "b", "c", "d"],
  "textposition": "top",
  "hovertext": ["A", "B", "C", "D"],
  "hovertemplate": "%{x} -> %{y}<extra>%{text}</extra>",
  "line": {
    "color": "rgb(31, 119, 180)",
    "width": 2,
    "dash": "solid",
    "shape": "linear",
    "smoothing": 1.3,
    "simplify": true
  },
  "marker": {
    "color": "rgb(31, 119, 180)",
    "size": 8,
    "symbol": "circle",
    "opacity": 0.8,
    "line": { "color": "#444", "width": 1 },
    "colorscale": "Viridis",
    "showscale": false,
    "cmin": 0,
    "cmax": 20
  },
  "fill": "none",
  "fillcolor": "rgba(31, 119, 180, 0.2)",
  "stackgroup": "",
  "orientation": "v",
  "xaxis": "x",
  "yaxis": "y",
  "showlegend": true,
  "legendgroup": "",
  "opacity": 1,
  "visible": true,
  "connectgaps": false,
  "cliponaxis": true
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mode` | `"lines"` / `"markers"` / `"text"` / combos with `+` / `"none"` | `"lines"` if >20 pts else `"lines+markers"` | Drawing mode |
| `line.shape` | `"linear"` / `"spline"` / `"hv"` / `"vh"` / `"hvh"` / `"vhv"` | `"linear"` | Line interpolation |
| `line.dash` | `"solid"` / `"dot"` / `"dash"` / `"longdash"` / `"dashdot"` / `"longdashdot"` | `"solid"` | Line dash style |
| `marker.symbol` | `"circle"` / `"square"` / `"diamond"` / `"cross"` / `"x"` / `"triangle-up"` / 100+ more | `"circle"` | Point symbol |
| `marker.colorscale` | named scale or `[[0,color], [1,color]]` | `"Viridis"` | Colorscale for marker coloring |
| `fill` | `"none"` / `"tozeroy"` / `"tozerox"` / `"tonexty"` / `"tonextx"` / `"toself"` / `"tonext"` | `"none"` | Fill area |
| `stackgroup` | string | `""` | Group name for stacking; enables stacking |

#### `"bar"` — Vertical and horizontal bar charts

```json
{
  "type": "bar",
  "x": ["A", "B", "C"],
  "y": [20, 14, 23],
  "orientation": "v",
  "base": 0,
  "width": 0.8,
  "offset": 0,
  "marker": {
    "color": "rgb(158, 202, 225)",
    "opacity": 0.6,
    "line": { "color": "rgb(8, 48, 107)", "width": 1.5 },
    "cornerradius": 0,
    "pattern": {
      "shape": "",
      "size": 8,
      "solidity": 0.3,
      "fgcolor": "#000",
      "bgcolor": "rgba(0,0,0,0)",
      "fillmode": "replace"
    }
  },
  "text": ["20", "14", "23"],
  "textposition": "auto",
  "textfont": { "family": "Arial", "size": 12, "color": "#444" },
  "insidetextfont": { "family": "Arial", "size": 12, "color": "#fff" },
  "error_x": { "type": "data", "array": [1, 2, 1], "visible": true },
  "error_y": { "type": "percent", "value": 5, "visible": true },
  "xaxis": "x",
  "yaxis": "y",
  "cliponaxis": true
}
```

Layout-level bar attributes (`layout` object):

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `barmode` | `"group"` / `"stack"` / `"overlay"` / `"relative"` | `"group"` | How multiple bar traces combine |
| `barnorm` | `""` / `"fraction"` / `"percent"` | `""` | Normalize bar heights |
| `bargap` | number (0-1) | `0.02` | Gap between bars of adjacent x coords |
| `bargroupgap` | number (0-1) | `0` | Gap between bars within the same x coord |
| `barcornerradius` | number or string (e.g. `"25%"`) | `0` | Rounded corners on all bars |

#### `"histogram"` — Histograms

```json
{
  "type": "histogram",
  "x": [1, 2, 2, 3, 3, 3, 4, 4, 5],
  "nbinsx": 10,
  "xbins": { "start": 0, "end": 6, "size": 0.5 },
  "histnorm": "",
  "histfunc": "count",
  "cumulative": { "enabled": false, "direction": "increasing" },
  "marker": { "color": "rgb(49,130,189)", "line": { "color": "white", "width": 1 } },
  "orientation": "v",
  "bingroup": ""
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `histnorm` | `""` / `"percent"` / `"probability"` / `"density"` / `"probability density"` | `""` | Normalization |
| `histfunc` | `"count"` / `"sum"` / `"avg"` / `"min"` / `"max"` | `"count"` | Aggregation function |
| `cumulative.enabled` | boolean | `false` | Cumulative histogram |
| `bingroup` | string | `""` | Group histograms together for shared bins |

#### `"box"` — Box plots

```json
{
  "type": "box",
  "y": [2, 3, 4, 5, 6, 7, 8, 9, 10, 15],
  "name": "Series 1",
  "boxmean": "sd",
  "boxpoints": "outliers",
  "notched": false,
  "notchwidth": 0.25,
  "whiskerwidth": 0.5,
  "q1": [],
  "median": [],
  "q3": [],
  "lowerfence": [],
  "upperfence": [],
  "mean": [],
  "sd": [],
  "marker": { "color": "rgb(8,81,156)", "outliercolor": "red", "symbol": "circle" },
  "line": { "color": "rgb(8,81,156)", "width": 2 },
  "fillcolor": "rgba(8,81,156,0.2)",
  "orientation": "v",
  "alignmentgroup": "",
  "offsetgroup": ""
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `boxmean` | `true` / `"sd"` / `false` | `false` | Show mean as line (sd = ±1 std dev) |
| `boxpoints` | `"all"` / `"outliers"` / `"suspectedoutliers"` / `false` | `"outliers"` | Which points to show |
| `notched` | boolean | `false` | Show notches around median |

#### `"violin"` — Violin plots

```json
{
  "type": "violin",
  "y": [2, 3, 4, 5, 6, 7, 8, 9, 10, 15],
  "name": "Series 1",
  "side": "both",
  "spanmode": "soft",
  "bandwidth": 1.5,
  "scalegroup": "",
  "scalemode": "width",
  "points": "outliers",
  "jitter": 0,
  "pointpos": 0,
  "meanline": { "visible": false, "color": "black", "width": 2 },
  "box": { "visible": false, "width": 0.25, "fillcolor": "rgba(0,0,0,0.2)" },
  "line": { "color": "rgb(8,81,156)", "width": 2 },
  "fillcolor": "rgba(8,81,156,0.2)",
  "orientation": "v",
  "alignmentgroup": "",
  "offsetgroup": ""
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `side` | `"both"` / `"positive"` / `"negative"` | `"both"` | Side of violin |
| `spanmode` | `"soft"` / `"hard"` | `"soft"` | How to span the violin |
| `scalemode` | `"width"` / `"count"` | `"width"` | Scale violins by width or count |
| `points` | `"all"` / `"outliers"` / `"suspectedoutliers"` / `false` | `"outliers"` | Show data points |

#### `"heatmap"` — 2D heatmaps

```json
{
  "type": "heatmap",
  "z": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  "x": [1, 2, 3],
  "y": [1, 2, 3],
  "zmin": 0,
  "zmax": 10,
  "zmid": null,
  "zsmooth": "best",
  "colorscale": "Viridis",
  "showscale": true,
  "reversescale": false,
  "connectgaps": false,
  "hoverongaps": true,
  "text": [["a","b","c"],["d","e","f"],["g","h","i"]],
  "hovertemplate": "x: %{x}<br>y: %{y}<br>z: %{z}<extra></extra>",
  "xgap": 0,
  "ygap": 0,
  "transpose": false
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `zsmooth` | `"fast"` / `"best"` / `false` | `false` | Smoothing algorithm |
| `connectgaps` | boolean | `false` | Connect NaN gaps in z |
| `hoverongaps` | boolean | `true` | Show hover on gaps |
| `transpose` | boolean | `false` | Transpose z data |

#### `"contour"` — Contour plots

```json
{
  "type": "contour",
  "z": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  "x": [1, 2, 3],
  "y": [1, 2, 3],
  "ncontours": 15,
  "contours": {
    "coloring": "fill",
    "showlines": true,
    "start": 0,
    "end": 10,
    "size": 1,
    "labelfont": { "family": "Arial", "size": 10, "color": "#444" },
    "labelformat": ".1f",
    "operation": "=",
    "value": 0
  },
  "line": { "color": "white", "width": 1, "smoothing": 0.85 },
  "colorscale": "Viridis",
  "showscale": true,
  "reversescale": false,
  "connectgaps": false,
  "hoverongaps": true,
  "transpose": false
}
```

#### `"histogram2d"` / `"histogram2dcontour"` — 2D histograms

```json
{
  "type": "histogram2d",
  "x": [1, 2, 2, 3, 3, 3, 4, 4, 5],
  "y": [2, 3, 3, 4, 4, 4, 5, 5, 6],
  "nbinsx": 10,
  "nbinsy": 10,
  "xbins": { "start": 0, "end": 6, "size": 0.5 },
  "ybins": { "start": 0, "end": 8, "size": 0.5 },
  "histnorm": "",
  "colorscale": "Viridis",
  "showscale": true,
  "zsmooth": "best",
  "zmin": null,
  "zmax": null
}
```

#### `"image"` — Image trace (render images on a plot)

```json
{
  "type": "image",
  "z": [
    [[0,0,0,1], [128,128,128,1], [255,255,255,1]],
    [[255,0,0,1], [0,255,0,1], [0,0,255,1]]
  ],
  "zsmooth": "fast",
  "hovertemplate": "",
  "xaxis": "x",
  "yaxis": "y"
}
```

#### `"scatterternary"` / `"scattercarpet"` — Specialized cartesian

```json
{
  "type": "scatterternary",
  "a": [1, 2, 3],
  "b": [4, 5, 6],
  "c": [7, 8, 9],
  "sum": 20,
  "mode": "markers",
  "marker": { "color": "red", "size": 8 },
  "subplot": "ternary"
}
```

---

### 2.2 Polar/Radial Traces

#### `"scatterpolar"` / `"scatterpolargl"` — Polar scatter

```json
{
  "type": "scatterpolar",
  "r": [1, 2, 3, 4],
  "theta": [0, 45, 90, 135],
  "thetaunit": "degrees",
  "mode": "lines+markers",
  "line": { "color": "purple" },
  "marker": { "color": "purple", "size": 6 },
  "fill": "none",
  "subplot": "polar"
}
```

#### `"barpolar"` — Polar bar charts

```json
{
  "type": "barpolar",
  "r": [1, 2, 3, 4],
  "theta": [0, 45, 90, 135],
  "thetaunit": "degrees",
  "width": [10, 10, 10, 10],
  "marker": {
    "color": ["red", "blue", "green", "orange"],
    "line": { "color": "white", "width": 1 }
  },
  "subplot": "polar"
}
```

---

### 2.3 Pie-Like Traces (Non-Cartesian)

#### `"pie"` — Pie and donut charts

```json
{
  "type": "pie",
  "values": [19, 26, 55],
  "labels": ["Residential", "Non-Residential", "Utility"],
  "name": "Energy",
  "marker": {
    "colors": ["rgb(56,75,126)", "rgb(18,36,37)", "rgb(34,53,101)"],
    "line": { "color": "#444", "width": 1 },
    "pattern": { "shape": "", "size": 8, "solidity": 0.3 }
  },
  "text": ["19%", "26%", "55%"],
  "textposition": "inside",
  "textinfo": "label+percent",
  "texttemplate": "%{label}<br>%{percent}",
  "hoverinfo": "label+percent+value+name",
  "hovertemplate": "%{label}: %{value} (%{percent})<extra></extra>",
  "hole": 0,
  "pull": 0,
  "direction": "clockwise",
  "rotation": 0,
  "sort": true,
  "automargin": false,
  "insidetextorientation": "horizontal",
  "insidetextfont": { "family": "Arial", "size": 14, "color": "#fff" },
  "outsidetextfont": { "family": "Arial", "size": 12, "color": "#000" },
  "showlegend": true,
  "legend": "legend",
  "domain": { "row": 0, "column": 0, "x": [0, 1], "y": [0, 1] },
  "scalegroup": ""
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `hole` | number 0–1 | `0` | Makes a donut chart (0 = full pie) |
| `pull` | number or array 0–1 | `0` | Pull slices out for explosion |
| `direction` | `"clockwise"` / `"counterclockwise"` | `"counterclockwise"` | Sector direction |
| `textinfo` | `"label"`/`"text"`/`"value"`/`"percent"` combos or `"none"` | `"label+percent"` | What text shows on slices |
| `insidetextorientation` | `"horizontal"` / `"radial"` / `"tangential"` / `"auto"` | `"auto"` | Text orientation inside |
| `sort` | boolean | `true` | Sort slices by value |
| `domain` | `{row, column, x[2], y[2]}` | — | Position in grid layout (for subplots) |

#### `"funnelarea"` — Funnel area chart (like pie but funnel-shaped)

```json
{
  "type": "funnelarea",
  "values": [100, 60, 40, 20],
  "labels": ["Leads", "Proposals", "Negotiations", "Closed"],
  "textinfo": "label+percent",
  "marker": {
    "colors": ["rgb(55,128,191)", "rgb(219,64,82)", "rgb(50,171,96)", "rgb(128,0,128)"]
  },
  "scalegroup": "",
  "aspectratio": 0.5,
  "baseratio": 0.4
}
```

---

### 2.4 Hierarchical / Tree Traces

#### `"sunburst"` — Sunburst charts

```json
{
  "type": "sunburst",
  "labels": ["Earth", "Land", "Water", "Forest", "Desert", "Ocean", "Ice"],
  "parents": ["", "Earth", "Earth", "Land", "Land", "Water", "Water"],
  "values": [100, 30, 70, 15, 15, 60, 10],
  "branchvalues": "total",
  "count": "",
  "maxdepth": 3,
  "marker": {
    "colors": ["#636efa", "#ef553b", "#00cc96", "#ab63fa", "#ffa15a", "#19d3f3", "#ff6692"]
  },
  "textinfo": "label+percent entry",
  "insidetextorientation": "radial",
  "leaf": { "opacity": 1 }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `branchvalues` | `"total"` / `"remainder"` | `"total"` | How values propagate |
| `maxdepth` | integer | `-1` (all) | Max depth levels to show |
| `count` | string | `""` | Determines default value when not set |
| `textinfo` | `"label"`/`"text"`/`"value"`/`"percent"`/`"percent root"`/`"percent entry"`/`"percent parent"` combos | `"label+percent entry"` | Text content |

#### `"treemap"` — Treemap charts

```json
{
  "type": "treemap",
  "labels": ["Root", "A", "B", "A1", "A2", "B1", "B2"],
  "parents": ["", "Root", "Root", "A", "A", "B", "B"],
  "values": [100, 40, 60, 15, 25, 35, 25],
  "branchvalues": "total",
  "maxdepth": 3,
  "textinfo": "label+value",
  "tiling": {
    "packing": "squarify",
    "squarifyratio": 1,
    "flip": 0,
    "pad": 3
  },
  "pathbar": { "visible": true, "thickness": 20, "side": "top" },
  "marker": {
    "colors": ["#636efa", "#ef553b", "#00cc96", "#ab63fa", "#ffa15a", "#19d3f3", "#ff6692"]
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `tiling.packing` | `"squarify"` / `"binary"` / `"dice"` / `"slice"` / `"slice-dice"` | `"squarify"` | Tiling algorithm |
| `pathbar.visible` | boolean | `true` | Show navigation path bar |

#### `"icicle"` — Icicle charts (rectangular hierarchy)

```json
{
  "type": "icicle",
  "labels": ["Root", "A", "B", "A1", "A2"],
  "parents": ["", "Root", "Root", "A", "A"],
  "values": [100, 40, 60, 15, 25],
  "branchvalues": "total",
  "textinfo": "label+value",
  "tiling": { "orientation": "v" }
}
```

---

### 2.5 Statistical / Distribution Traces

#### `"histogram"`, `"box"`, `"violin"` — Already covered above

#### `"splom"` — Scatter plot matrix (SPLOM)

```json
{
  "type": "splom",
  "dimensions": [
    { "label": "Sepal length", "values": [5.1, 4.9, 4.7, 4.6, 5.0] },
    { "label": "Sepal width", "values": [3.5, 3.0, 3.2, 3.1, 3.6] },
    { "label": "Petal length", "values": [1.4, 1.4, 1.3, 1.5, 1.4] }
  ],
  "marker": {
    "color": "rgb(31,119,180)",
    "size": 3,
    "opacity": 0.7,
    "line": { "color": "white", "width": 0.5 }
  },
  "text": ["setosa", "setosa", "setosa", "setosa", "setosa"],
  "diagonal": { "visible": true }
}
```

#### `"parcoords"` — Parallel coordinates

```json
{
  "type": "parcoords",
  "dimensions": [
    {
      "label": "Height",
      "values": [150, 160, 170, 180, 190],
      "range": [140, 200],
      "constraintrange": [160, 180]
    },
    {
      "label": "Weight",
      "values": [50, 60, 70, 80, 90],
      "range": [40, 100]
    }
  ],
  "line": {
    "color": [1, 2, 3, 4, 5],
    "colorscale": "Viridis",
    "showscale": true
  }
}
```

#### `"parcats"` — Parallel categories diagram

```json
{
  "type": "parcats",
  "dimensions": [
    {
      "label": "Gender",
      "values": ["M", "F", "M", "F", "M"],
      "categoryorder": "trace"
    },
    {
      "label": "Class",
      "values": ["1st", "2nd", "3rd", "1st", "3rd"],
      "categoryorder": "trace"
    }
  ],
  "line": {
    "color": [1, 2, 3, 4, 5],
    "colorscale": "Viridis",
    "showscale": true,
    "shape": "spline"
  },
  "bundlecolors": true,
  "sortpaths": "forward"
}
```

---

### 2.6 Financial Traces

#### `"candlestick"` — Candlestick charts

```json
{
  "type": "candlestick",
  "x": ["2024-01-01", "2024-01-02", "2024-01-03"],
  "open": [100, 102, 105],
  "high": [105, 107, 108],
  "low": [98, 101, 103],
  "close": [103, 106, 104],
  "increasing": {
    "line": { "color": "#17BECF", "width": 1 },
    "fillcolor": "#17BECF"
  },
  "decreasing": {
    "line": { "color": "#7F7F7F", "width": 1 },
    "fillcolor": "#7F7F7F"
  },
  "line": { "color": "rgba(31,119,180,1)", "width": 1 },
  "name": "AAPL",
  "xaxis": "x",
  "yaxis": "y",
  "whiskerwidth": 0.5
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `increasing.line.color` | color | `"#17BECF"` | Bullish candle line color |
| `decreasing.line.color` | color | `"#7F7F7F"` | Bearish candle line color |
| `whiskerwidth` | number 0–1 | `0.5` | Width of the whiskers |

#### `"ohlc"` — OHLC (Open-High-Low-Close) charts

```json
{
  "type": "ohlc",
  "x": ["2024-01-01", "2024-01-02", "2024-01-03"],
  "open": [100, 102, 105],
  "high": [105, 107, 108],
  "low": [98, 101, 103],
  "close": [103, 106, 104],
  "increasing": { "line": { "color": "#17BECF" } },
  "decreasing": { "line": { "color": "#7F7F7F" } },
  "line": { "width": 1, "dash": "solid" },
  "xaxis": "x",
  "yaxis": "y"
}
```

#### `"waterfall"` — Waterfall charts

```json
{
  "type": "waterfall",
  "x": ["Start", "Revenue", "Costs", "Tax", "Profit"],
  "y": [100, 30, -20, -10, 100],
  "measure": ["relative", "relative", "relative", "relative", "total"],
  "base": 0,
  "text": ["100", "+30", "-20", "-10", "100"],
  "textposition": "outside",
  "connector": {
    "line": { "color": "rgb(63, 63, 63)", "dash": "solid", "width": 1 },
    "visible": true
  },
  "increasing": { "marker": { "color": "#00cc96" } },
  "decreasing": { "marker": { "color": "#ef553b" } },
  "totals": { "marker": { "color": "#636efa" } }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `measure` | array of `"relative"` / `"total"` / `"absolute"` | — | How each bar contributes |
| `connector.visible` | boolean | `true` | Show connector lines between bars |

#### `"funnel"` — Funnel charts

```json
{
  "type": "funnel",
  "x": [100, 60, 40, 20],
  "y": ["Leads", "Proposals", "Negotiations", "Closed"],
  "orientation": "h",
  "marker": {
    "color": ["rgb(55,128,191)", "rgb(219,64,82)", "rgb(50,171,96)", "rgb(128,0,128)"]
  },
  "connector": { "line": { "color": "grey", "width": 1 }, "visible": true },
  "textinfo": "value+percent initial",
  "textposition": "inside",
  "cliponaxis": true
}
```

---

### 2.7 Flow / Relationship Traces

#### `"sankey"` — Sankey diagrams

```json
{
  "type": "sankey",
  "orientation": "h",
  "arrangement": "fixed",
  "node": {
    "label": ["Source A", "Source B", "Target C", "Target D"],
    "color": ["blue", "red", "green", "purple"],
    "groups": [],
    "x": [0, 0, 0.5, 0.5],
    "y": [0, 1, 0, 1],
    "pad": 20,
    "thickness": 20,
    "line": { "color": "black", "width": 0.5 },
    "customdata": [],
    "hovertemplate": "%{label} total: %{value}<extra></extra>"
  },
  "link": {
    "source": [0, 0, 1, 1],
    "target": [2, 3, 2, 3],
    "value": [8, 3, 2, 5],
    "color": ["rgba(0,0,255,0.3)", "rgba(0,0,255,0.3)", "rgba(255,0,0,0.3)", "rgba(255,0,0,0.3)"],
    "line": { "color": "black", "width": 0.2 },
    "customdata": [],
    "hovertemplate": "%{source.label} -> %{target.label}: %{value}<extra></extra>"
  },
  "textfont": { "family": "Arial", "size": 12, "color": "black" }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `orientation` | `"h"` / `"v"` | `"h"` | Flow direction |
| `arrangement` | `"fixed"` / `"snap"` / `"perpendicular"` / `"freeform"` / `"d3"` | `"d3"` | Node arrangement algorithm |
| `node.pad` | number | `20` | Padding between nodes |
| `node.thickness` | number | `20` | Node thickness |

---

### 2.8 Map Traces

#### `"scattergeo"` — Geographic scatter plots

```json
{
  "type": "scattergeo",
  "lat": [40.7128, 34.0522, 41.8781],
  "lon": [-74.0060, -118.2437, -87.6298],
  "locations": ["USA", "CAN", "MEX"],
  "locationmode": "USA-states",
  "mode": "markers+text",
  "marker": { "color": "red", "size": 10, "symbol": "circle" },
  "text": ["NYC", "LA", "Chicago"],
  "geo": "geo",
  "line": { "color": "black", "width": 1 },
  "fill": "none",
  "fillcolor": "rgba(0,0,0,0)"
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `locationmode` | `"ISO-3"` / `"USA-states"` / `"country names"` / `"geojson-id"` | `"ISO-3"` | How `locations` is interpreted |
| `locations` | array of strings | — | Country/state codes (requires `locationmode`) |
| `geo` | subplot id | `"geo"` | Reference to `layout.geo` |

#### `"choropleth"` — Choropleth maps

```json
{
  "type": "choropleth",
  "locations": ["USA", "CAN", "MEX"],
  "locationmode": "country names",
  "z": [100, 200, 150],
  "text": ["United States", "Canada", "Mexico"],
  "colorscale": "Blues",
  "autocolorscale": false,
  "reversescale": false,
  "showscale": true,
  "colorbar": { "title": { "text": "Value" } },
  "marker": { "line": { "color": "white", "width": 0.5 }, "opacity": 0.8 },
  "geo": "geo",
  "zmin": null,
  "zmax": null
}
```

#### `"scattermapbox"` / `"scattermap"` — Mapbox tile-based scatter

```json
{
  "type": "scattermapbox",
  "lat": [40.7128, 34.0522],
  "lon": [-74.0060, -118.2437],
  "mode": "markers+text",
  "marker": { "color": "red", "size": 10, "opacity": 0.8 },
  "text": ["NYC", "LA"],
  "textposition": "top right",
  "subplot": "map",
  "fill": "none",
  "below": ""
}
```

#### `"choroplethmapbox"` / `"choroplethmap"` / `"densitymapbox"` / `"densitymap"` — Mapbox tile-based maps

```json
{
  "type": "choroplethmapbox",
  "geojson": {
    "type": "FeatureCollection",
    "features": []
  },
  "featureidkey": "properties.id",
  "locations": ["id1", "id2"],
  "z": [100, 200],
  "colorscale": "Viridis",
  "subplot": "map"
}
```

```json
{
  "type": "densitymapbox",
  "lat": [40.7128, 34.0522],
  "lon": [-74.0060, -118.2437],
  "z": [5, 10],
  "radius": 10,
  "colorscale": "Hot",
  "subplot": "map",
  "below": ""
}
```

---

### 2.9 3D Traces (WebGL/gl3d)

#### `"scatter3d"` — 3D scatter plot

```json
{
  "type": "scatter3d",
  "x": [1, 2, 3, 4],
  "y": [5, 6, 7, 8],
  "z": [9, 10, 11, 12],
  "mode": "markers+lines+text",
  "marker": {
    "color": "rgb(31,119,180)",
    "size": 6,
    "symbol": "circle",
    "line": { "color": "#444", "width": 0.5 },
    "opacity": 0.8,
    "colorscale": "Viridis",
    "showscale": false
  },
  "line": { "color": "#444", "width": 2, "dash": "solid" },
  "text": ["pt1", "pt2", "pt3", "pt4"],
  "surfaceaxis": -1,
  "projection": {
    "x": { "show": false, "opacity": 0.5 },
    "y": { "show": false, "opacity": 0.5 },
    "z": { "show": false, "opacity": 0.5 }
  },
  "scene": "scene",
  "connectgaps": false
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `surfaceaxis` | `-1` / `0` / `1` / `2` | `-1` | Project points onto axis surface |
| `projection` | object | — | Show projections on each axis plane |
| `scene` | subplot id | `"scene"` | Reference to `layout.scene` |

#### `"surface"` — 3D surface plot

```json
{
  "type": "surface",
  "x": [1, 2, 3, 4],
  "y": [1, 2, 3, 4],
  "z": [[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21], [22, 23, 24, 25]],
  "colorscale": "Viridis",
  "showscale": true,
  "reversescale": false,
  "opacity": 1,
  "surfacecolor": [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
  "cmin": null,
  "cmax": null,
  "contours": {
    "x": { "show": false, "highlight": true, "color": "black", "width": 1, "project": { "x": false, "y": false, "z": false } },
    "y": { "show": false, "highlight": true, "color": "black", "width": 1 },
    "z": { "show": true, "highlight": true, "color": "black", "width": 1 }
  },
  "hidesurface": false,
  "scene": "scene",
  "connectgaps": false
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `hidesurface` | boolean | `false` | Hide surface, show only contour lines |
| `surfacecolor` | 2D array | — | Override z for coloring |
| `contours.x/y/z.show` | boolean | `false` | Show contour lines on each axis |

#### `"mesh3d"` — 3D mesh (triangle mesh)

```json
{
  "type": "mesh3d",
  "x": [0, 1, 1, 0],
  "y": [0, 0, 1, 1],
  "z": [0, 0, 0, 1],
  "i": [0, 0, 0],
  "j": [1, 2, 3],
  "k": [2, 3, 1],
  "intensity": [0, 0.33, 0.66, 1],
  "intensitymode": "vertex",
  "vertexcolor": [],
  "facecolor": [],
  "colorscale": "Viridis",
  "showscale": true,
  "opacity": 0.8,
  "scene": "scene",
  "flatshading": false,
  "contour": { "show": false, "color": "black", "width": 1 },
  "hoverinfo": "x+y+z"
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `i`, `j`, `k` | arrays | — | Indices of triangle vertices |
| `intensity` | array | — | Per-vertex values for colorscale |
| `intensitymode` | `"vertex"` / `"cell"` | `"vertex"` | How intensity maps |
| `vertexcolor` | array of colors | — | Per-vertex colors (overrides colorscale) |
| `facecolor` | array of colors | — | Per-face colors |
| `flatshading` | boolean | `false` | Disable smooth shading |

#### `"isosurface"` — 3D isosurface (volume iso-level)

```json
{
  "type": "isosurface",
  "x": [0, 0, 0, 0, 1, 1, 1, 1],
  "y": [0, 0, 1, 1, 0, 0, 1, 1],
  "z": [0, 1, 0, 1, 0, 1, 0, 1],
  "value": [0, 0, 0, 0, 1, 1, 1, 1],
  "isomin": 0.5,
  "isomax": 0.5,
  "caps": { "x": { "show": true }, "y": { "show": true }, "z": { "show": true } },
  "slices": {
    "x": { "show": false, "locations": [] },
    "y": { "show": false, "locations": [] },
    "z": { "show": false, "locations": [] }
  },
  "surface": { "count": 1, "fill": 1, "pattern": "all", "show": true },
  "colorscale": "Viridis",
  "showscale": true,
  "scene": "scene"
}
```

#### `"volume"` — 3D volume rendering

```json
{
  "type": "volume",
  "x": [0, 0, 0, 0, 1, 1, 1, 1],
  "y": [0, 0, 1, 1, 0, 0, 1, 1],
  "z": [0, 1, 0, 1, 0, 1, 0, 1],
  "value": [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4],
  "isomin": 0.2,
  "isomax": 1.2,
  "caps": { "x": { "show": true }, "y": { "show": true }, "z": { "show": true } },
  "slices": {
    "x": { "show": true, "locations": [0.5] },
    "y": { "show": true, "locations": [0.5] },
    "z": { "show": true, "locations": [0.5] }
  },
  "surface": { "count": 3, "fill": 0.7, "pattern": "all", "show": true },
  "colorscale": "Viridis",
  "showscale": true,
  "opacity": 0.5,
  "scene": "scene"
}
```

#### `"streamtube"` — 3D streamtubes (flow visualization)

```json
{
  "type": "streamtube",
  "x": [0, 0, 0],
  "y": [0, 0, 0],
  "z": [0, 0, 0],
  "u": [1, 0, 0],
  "v": [0, 1, 0],
  "w": [0, 0, 1],
  "starts": {
    "x": [0, 0.5, 1],
    "y": [0, 0.5, 1],
    "z": [0, 0.5, 1]
  },
  "colorscale": "Viridis",
  "showscale": true,
  "showlegend": true,
  "maxdisplayed": 1000,
  "sizeref": 1,
  "scene": "scene"
}
```

#### `"cone"` — 3D cone plot (vector field)

```json
{
  "type": "cone",
  "x": [0, 1, 2],
  "y": [0, 0, 0],
  "z": [0, 0, 0],
  "u": [1, 1, 1],
  "v": [0, 0, 0],
  "w": [0, 0, 0],
  "colorscale": "Viridis",
  "showscale": true,
  "sizemode": "scaled",
  "sizeref": 0.5,
  "anchor": "tip",
  "scene": "scene"
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `sizemode` | `"scaled"` / `"absolute"` | `"scaled"` | Size scaling mode |
| `anchor` | `"tip"` / `"tail"` / `"cm"` / `"center"` | `"tip"` | Anchor point for the cone |

---

### 2.10 Table / Special Traces

#### `"table"` — Table trace (not a chart — renders a data table)

```json
{
  "type": "table",
  "header": {
    "values": [["Name"], ["Age"], ["City"]],
    "align": "center",
    "line": { "color": "#506784", "width": 1 },
    "fill": { "color": "#506784" },
    "font": { "family": "Arial", "size": 12, "color": "white" },
    "height": 28,
    "format": [],
    "prefix": "",
    "suffix": "",
    "valuessrc": null
  },
  "cells": {
    "values": [
      ["Alice", "Bob", "Charlie"],
      ["30", "25", "35"],
      ["NYC", "LA", "Chicago"]
    ],
    "align": "left",
    "line": { "color": "#c8d4e3", "width": 1 },
    "fill": { "color": ["#ebf0f8", "#ffffff"] },
    "font": { "family": "Arial", "size": 11, "color": "#506784" },
    "height": 20,
    "format": [],
    "prefix": "",
    "suffix": "",
    "valuessrc": null
  },
  "columnorder": [],
  "columnwidth": [],
  "domain": { "x": [0, 1], "y": [0, 1] },
  "hoverinfo": "all"
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `header.values` | array of arrays | — | Each inner array is a column |
| `cells.values` | array of arrays | — | Row data, same column count as header |
| `fill.color` | color or array | — | Alternating `["even", "odd"]` works |

#### `"indicator"` — Single value indicators (gauges, KPI cards)

```json
{
  "type": "indicator",
  "mode": "number+delta+gauge",
  "value": 420.69,
  "title": { "text": "Revenue", "align": "center", "font": { "size": 24 } },
  "delta": {
    "reference": 400,
    "position": "bottom",
    "relative": false,
    "valueformat": ".2f",
    "increasing": { "color": "#00cc96" },
    "decreasing": { "color": "#ef553b" }
  },
  "gauge": {
    "shape": "angular",
    "bar": { "color": "#636efa", "line": { "color": "#444", "width": 0 } },
    "bgcolor": "rgba(0,0,0,0)",
    "bordercolor": "#444",
    "borderwidth": 0,
    "axis": { "range": [null, 500], "visible": true, "tickwidth": 1 },
    "steps": [
      { "range": [0, 200], "color": "#ff4136" },
      { "range": [200, 400], "color": "#ff851b" },
      { "range": [400, 500], "color": "#2ecc40" }
    ],
    "threshold": { "line": { "color": "#ff4136", "width": 4 }, "thickness": 0.75, "value": 450 }
  },
  "domain": { "row": 0, "column": 0, "x": [0, 1], "y": [0, 1] },
  "align": "center",
  "number": { "font": { "size": 60 }, "prefix": "$", "suffix": "M", "valueformat": ".2f" }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mode` | `"number"` / `"delta"` / `"gauge"` combos with `+` | — | Which elements to show |
| `gauge.shape` | `"angular"` / `"bullet"` | `"angular"` | Gauge style |

---

### 2.11 ScatterGL (WebGL-Accelerated Scatter)

#### `"scattergl"` — Like scatter but uses WebGL for performance

```json
{
  "type": "scattergl",
  "x": [1, 2, 3, 4],
  "y": [10, 15, 13, 17],
  "mode": "markers",
  "marker": {
    "color": "rgba(31,119,180,0.7)",
    "size": 6,
    "symbol": "circle",
    "line": { "color": "#444", "width": 0.5 }
  },
  "line": { "color": "rgb(31,119,180)", "width": 2 },
  "text": ["a", "b", "c", "d"],
  "connectgaps": false,
  "xaxis": "x",
  "yaxis": "y"
}
```

Supports the same attributes as `"scatter"` but with better performance for large datasets.

#### `"scatterpolar"` (GL version: `"scatterpolargl"`)

Same attributes as `"scatterpolar"`.

#### `"scattersmith"` — Smith chart (impedance matching)

```json
{
  "type": "scattersmith",
  "real": [0.1, 0.2, 0.5, 1.0],
  "imag": [0.05, 0.1, -0.2, -0.5],
  "mode": "lines+markers",
  "line": { "color": "blue" },
  "marker": { "color": "blue", "size": 6 },
  "subplot": "smith"
}
```

---

## 3. Layout Object

The `layout` object controls everything outside the data traces.

### 3.1 Global Layout

```json
{
  "layout": {
    "title": { "text": "Chart Title", "font": { "family": "Arial", "size": 18, "color": "#333" }, "x": 0.5, "y": 0.95, "xanchor": "center", "yanchor": "top", "xref": "container", "yref": "container", "automargin": true },
    "font": { "family": "Arial, sans-serif", "size": 12, "color": "#333" },
    "width": 800,
    "height": 600,
    "autosize": true,
    "margin": { "l": 80, "r": 50, "t": 100, "b": 80, "pad": 4, "autoexpand": true },
    "paper_bgcolor": "#fff",
    "plot_bgcolor": "#fff",
    "showlegend": true,
    "legend": { ... },
    "hovermode": "closest",
    "hoverlabel": { "bgcolor": "#fff", "bordercolor": "#444", "font": { "family": "Arial", "size": 12 }, "align": "auto", "namelength": 15 },
    "dragmode": "zoom",
    "clickmode": "event",
    "separators": ".,",
    "barmode": "group",
    "bargap": 0.02,
    "bargroupgap": 0,
    "boxmode": "overlay",
    "hiddenlabels": [],
    "selectdirection": "any",
    "template": { ... }
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `hovermode` | `"x"` / `"y"` / `"closest"` / `"x unified"` / `"y unified"` / `false` | `"closest"` | Hover interaction mode |
| `dragmode` | `"zoom"` / `"pan"` / `"select"` / `"lasso"` / `"drawclosedpath"` / `"drawopenpath"` / `"drawline"` / `"drawrect"` / `"drawcircle"` / `"orbit"` / `"turntable"` / `false` | `"zoom"` | Drag interaction |
| `separators` | string | `".,"` | Decimal and thousands separator for numbers |

### 3.2 Title Object

```json
{
  "title": {
    "text": "My Chart",
    "font": { "family": "Arial", "size": 18, "color": "#333", "style": "normal", "weight": 400, "variant": "normal", "lineposition": "none", "shadow": "none", "textcase": "normal" },
    "x": 0.5,
    "y": 0.95,
    "xanchor": "center",
    "yanchor": "top",
    "xref": "container",
    "yref": "container",
    "pad": { "t": 10, "b": 10, "l": 10, "r": 10 },
    "automargin": true
  }
}
```

### 3.3 Axis Objects (`xaxis`, `yaxis`, `xaxis2`, `yaxis2`, ...)

Cartesian axes. You can have multiple: `xaxis`, `xaxis2`, ... `xaxis9`, same for `yaxis`.

```json
{
  "xaxis": {
    "title": { "text": "X Axis", "font": { "family": "Arial", "size": 14, "color": "#333" }, "standoff": 0 },
    "range": [0, 10],
    "autorange": true,
    "rangemode": "normal",
    "type": "linear",
    "side": "bottom",
    "domain": [0, 1],
    "anchor": "y",
    "overlaying": "free",
    "position": 0,
    "showline": true,
    "linecolor": "#444",
    "linewidth": 1,
    "showgrid": true,
    "gridcolor": "#eee",
    "gridwidth": 1,
    "griddash": "solid",
    "zeroline": true,
    "zerolinecolor": "#444",
    "zerolinewidth": 1,
    "showticklabels": true,
    "tickfont": { "family": "Arial", "size": 11, "color": "#666" },
    "tickangle": 0,
    "tickprefix": "",
    "ticksuffix": "",
    "showtickprefix": "all",
    "showticksuffix": "all",
    "tickformat": "",
    "tickformatstops": [ { "dtickrange": [null, 1000], "value": ".0f" } ],
    "tickmode": "auto",
    "nticks": 0,
    "tick0": null,
    "dtick": null,
    "tickvals": [],
    "ticktext": [],
    "ticks": "",
    "ticklen": 5,
    "tickwidth": 1,
    "tickcolor": "#444",
    "exponentformat": "B",
    "minexponent": 3,
    "showexponent": "all",
    "separatethousands": false,
    "categoryorder": "trace",
    "categoryarray": [],
    "fixedrange": false,
    "spikemode": "toaxis+across",
    "spikedash": "dash",
    "spikethickness": 2,
    "spikecolor": "#444",
    "spikesnap": "data",
    "hoverformat": ""  
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `type` | `"-"` / `"linear"` / `"log"` / `"date"` / `"category"` / `"multicategory"` | `"-"` (auto) | Axis scale type |
| `autorange` | boolean / `"reversed"` | `true` | Auto-compute range |
| `rangemode` | `"normal"` / `"tozero"` / `"nonnegative"` | `"normal"` | Constrain auto range |
| `side` | `"top"` / `"bottom"` / `"left"` / `"right"` | depends | Which side the axis appears |
| `domain` | `[start, end]` | `[0, 1]` | Position in the plotting area (0–1) |
| `anchor` | axis id | — | Which axis this one is anchored to |
| `overlaying` | `"free"` / axis id | — | Overlay on another axis |
| `fixedrange` | boolean | `false` | Prevent zoom/pan on this axis |
| `categoryorder` | `"trace"` / `"category ascending"` / `"category descending"` / `"array"` / `"total ascending"` / `"total descending"` / `"min ascending"` / `"min descending"` / `"max ascending"` / `"max descending"` / `"sum ascending"` / `"sum descending"` / `"mean ascending"` / `"mean descending"` / `"median ascending"` / `"median descending"` | `"trace"` | Category ordering |

#### Rangeslider (for x-axis)

```json
{
  "xaxis": {
    "rangeslider": {
      "visible": true,
      "thickness": 0.15,
      "range": ["2024-01-01", "2024-12-31"],
      "borderwidth": 0,
      "bordercolor": "#444",
      "bgcolor": "#eee",
      "autorange": false
    }
  }
}
```

#### Rangeselector (for x-axis)

```json
{
  "xaxis": {
    "rangeselector": {
      "visible": true,
      "buttons": [
        { "count": 1, "label": "1m", "step": "month", "stepmode": "backward" },
        { "count": 6, "label": "6m", "step": "month", "stepmode": "backward" },
        { "count": 1, "label": "YTD", "step": "year", "stepmode": "todate" },
        { "count": 1, "label": "1y", "step": "year", "stepmode": "backward" },
        { "step": "all", "label": "All" }
      ],
      "x": 0,
      "y": 1.2,
      "xanchor": "left",
      "yanchor": "bottom",
      "font": { "size": 11 },
      "bgcolor": "#d3d3d3",
      "activecolor": "#636efa",
      "bordercolor": "#444",
      "borderwidth": 1
    }
  }
}
```

#### Minor Grid / Ticks

```json
{
  "xaxis": {
    "minor": {
      "showgrid": false,
      "gridcolor": "#f5f5f5",
      "gridwidth": 0.5,
      "griddash": "solid",
      "tickmode": "auto",
      "nticks": 0,
      "tick0": null,
      "dtick": null,
      "tickvals": [],
      "ticks": "",
      "ticklen": 2,
      "tickwidth": 0.5,
      "tickcolor": "#999"
    }
  }
}
```

### 3.4 Scene Objects (for 3D: `scene`, `scene2`, ...)

```json
{
  "scene": {
    "bgcolor": "rgba(0,0,0,0)",
    "camera": {
      "up": { "x": 0, "y": 0, "z": 1 },
      "center": { "x": 0, "y": 0, "z": 0 },
      "eye": { "x": 1.25, "y": 1.25, "z": 1.25 },
      "projection": { "type": "perspective" }
    },
    "domain": { "x": [0, 1], "y": [0, 1] },
    "aspectmode": "auto",
    "aspectratio": { "x": 1, "y": 1, "z": 1 },
    "xaxis": { "title": { "text": "X" }, "type": "linear", "range": [null, null], "showgrid": true, "gridcolor": "#eee", "showspikes": true },
    "yaxis": { "title": { "text": "Y" }, "type": "linear" },
    "zaxis": { "title": { "text": "Z" }, "type": "linear" },
    "annotations": [],
    "dragmode": "turntable",
    "hovermode": "closest"
  }
}
```

### 3.5 Geo Object (for `layout.geo`)

```json
{
  "geo": {
    "scope": "world",
    "showcountries": true,
    "countrycolor": "#444",
    "countrywidth": 0.5,
    "showsubunits": true,
    "subunitcolor": "#444",
    "subunitwidth": 0.5,
    "showframe": true,
    "framecolor": "#444",
    "framewidth": 1,
    "bgcolor": "rgba(0,0,0,0)",
    "lakecolor": "#d3d3d3",
    "landcolor": "#f5f5f5",
    "oceancolor": "#e0f0ff",
    "showocean": true,
    "showland": true,
    "showlakes": false,
    "showrivers": false,
    "rivercolor": "#a0c8e0",
    "riverwidth": 0.5,
    "coastlinecolor": "#444",
    "coastlinewidth": 0.5,
    "projection": { "type": "equirectangular", "rotation": { "lon": 0, "lat": 0, "roll": 0 }, "parallels": [0, 0], "scale": 1 },
    "resolution": 50,
    "lonaxis": { "range": [null, null], "showgrid": true, "gridcolor": "#eee", "gridwidth": 1 },
    "lataxis": { "range": [null, null], "showgrid": true, "gridcolor": "#eee", "gridwidth": 1 },
    "fitbounds": false,
    "visible": true,
    "domain": { "x": [0, 1], "y": [0, 1] }
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `scope` | `"world"` / `"usa"` / `"europe"` / `"asia"` / `"africa"` / `"north america"` / `"south america"` | `"world"` | Geographic scope |
| `projection.type` | `"equirectangular"` / `"mercator"` / `"orthographic"` / `"natural earth"` / `"kavrayskiy7"` / `"miller"` / `"robinson"` / `"eckert4"` / `"azimuthal equal area"` / `"azimuthal equidistant"` / `"conic equal area"` / `"conic conformal"` / `"conic equidistant"` / `"gnomonic"` / `"stereographic"` / `"mollweide"` / `"hammer"` / `"transverse mercator"` / `"albers usa"` / `"winkel tripel"` / `"aitoff"` / `"sinusoidal"` | `"equirectangular"` | Map projection |
| `fitbounds` | boolean / `"locations"` / `"geojson"` | `false` | Auto-zoom to data bounds |

### 3.6 Map Object (for `layout.map` — Mapbox-style)

```json
{
  "map": {
    "style": "basic",
    "center": { "lat": 40, "lon": -100 },
    "zoom": 3,
    "bearing": 0,
    "pitch": 0,
    "uirevision": null,
    "domain": { "x": [0, 1], "y": [0, 1] }
  }
}
```

### 3.7 Polar Object (for `layout.polar`)

```json
{
  "polar": {
    "bgcolor": "rgba(0,0,0,0)",
    "radialaxis": {
      "title": { "text": "Radius" },
      "range": [0, null],
      "type": "linear",
      "angle": 0,
      "showline": true,
      "showgrid": true,
      "gridcolor": "#eee",
      "gridwidth": 1,
      "side": "counterclockwise",
      "tickfont": { "size": 11 }
    },
    "angularaxis": {
      "title": { "text": "Angle" },
      "type": "linear",
      "rotation": 0,
      "direction": "counterclockwise",
      "thetaunit": "degrees",
      "showline": true,
      "showgrid": true,
      "gridcolor": "#eee",
      "gridwidth": 1,
      "tickfont": { "size": 11 },
      "period": 360
    },
    "sector": [0, 360],
    "hole": 0,
    "gridshape": "circular",
    "domain": { "x": [0, 1], "y": [0, 1] },
    "uirevision": null
  }
}
```

### 3.8 Legend

```json
{
  "legend": {
    "title": { "text": "Legend", "font": { "family": "Arial", "size": 12, "color": "#333" }, "side": "top" },
    "traceorder": "normal",
    "tracegroupgap": 10,
    "font": { "family": "Arial", "size": 12, "color": "#333" },
    "bgcolor": "#fff",
    "bordercolor": "#444",
    "borderwidth": 0,
    "x": 1.02,
    "y": 1,
    "xanchor": "left",
    "yanchor": "auto",
    "xref": "paper",
    "yref": "paper",
    "orientation": "v",
    "valign": "middle",
    "itemclick": "toggle",
    "itemdoubleclick": "toggleothers",
    "itemsizing": "trace",
    "itemwidth": 30,
    "groupclick": "toggleitem",
    "grouptitlefont": { "family": "Arial", "size": 12, "color": "#333" },
    "uirevision": null,
    "visible": true
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `x`/`y` | number | `1.02`/`1` | Position (in paper coordinates 0–1) |
| `xanchor` | `"auto"` / `"left"` / `"center"` / `"right"` | `"left"` | Horizontal anchor |
| `yanchor` | `"auto"` / `"top"` / `"middle"` / `"bottom"` | `"auto"` | Vertical anchor |
| `orientation` | `"v"` / `"h"` | `"v"` | Vertical or horizontal layout |
| `itemclick` | `"toggle"` / `"toggleothers"` / `false` | `"toggle"` | Behavior on legend click |
| `itemdoubleclick` | `"toggle"` / `"toggleothers"` / `false` | `"toggleothers"` | Behavior on double-click |

### 3.9 Grid (for subplots)

```json
{
  "grid": {
    "rows": 2,
    "roworder": "top to bottom",
    "columns": 2,
    "subplots": [["xy", "x2y"], ["x3y2", "x4y2"]],
    "xaxes": ["x", "x2"],
    "yaxes": ["y", "y2"],
    "pattern": "independent",
    "xgap": 0.1,
    "ygap": 0.1,
    "xside": "bottom plot",
    "yside": "left plot"
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `pattern` | `"independent"` / `"coupled"` | `"coupled"` | Independent axes or shared |
| `subplots` | 2D array of subplot ids | — | Freeform grid layout |
| `xaxes`/`yaxes` | array of axis ids | — | Axis IDs for each column/row |

### 3.10 Annotations

```json
{
  "annotations": [
    {
      "text": "Annotation label",
      "x": 0.5,
      "y": 0.5,
      "xref": "paper",
      "yref": "paper",
      "xanchor": "auto",
      "yanchor": "auto",
      "align": "center",
      "font": { "family": "Arial", "size": 12, "color": "#333" },
      "showarrow": true,
      "arrowhead": 1,
      "arrowsize": 1,
      "arrowwidth": 1,
      "arrowcolor": "#444",
      "ax": -40,
      "ay": -30,
      "axref": "pixel",
      "ayref": "pixel",
      "standoff": 0,
      "startarrowsize": 0.3,
      "startstandoff": 0,
      "bgcolor": "rgba(0,0,0,0)",
      "bordercolor": "#444",
      "borderwidth": 0,
      "borderpad": 3,
      "opacity": 1,
      "textangle": 0,
      "valign": "middle",
      "visible": true,
      "width": null,
      "height": null,
      "clicktoshow": "false",
      "captureevents": false,
      "hovertext": "",
      "hoverlabel": { "bgcolor": "#fff", "bordercolor": "#444", "font": { "size": 12 } },
      "name": "",
      "templateitemname": ""
    }
  ]
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `xref`/`yref` | `"paper"` / `"x"` / `"x2"` / `"x domain"` etc. | `"paper"` | Coordinate reference |
| `showarrow` | boolean | `true` | Draw arrow from annotation |
| `ax`/`ay` | number | `-40`/`-30` | Arrow tail offset (pixels) |
| `clicktoshow` | `false` / `"onclick"` / `"onout"` | `"false"` | Show on click |

### 3.11 Shapes

```json
{
  "shapes": [
    {
      "type": "rect",
      "xref": "x",
      "yref": "paper",
      "x0": "2024-01-15",
      "y0": 0,
      "x1": "2024-02-15",
      "y1": 1,
      "fillcolor": "#d3d3d3",
      "opacity": 0.2,
      "line": { "color": "#444", "width": 0, "dash": "solid" },
      "layer": "above",
      "xsizemode": "scaled",
      "ysizemode": "scaled",
      "xanchor": 0,
      "yanchor": 0,
      "name": "",
      "showlegend": false,
      "legendgroup": "",
      "legend": "legend",
      "legendrank": 1000,
      "legendwidth": null,
      "editable": false,
      "visible": true,
      "templateitemname": ""
    }
  ]
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `type` | `"rect"` / `"circle"` / `"line"` / `"path"` | — | Shape geometry |
| `layer` | `"below"` / `"above"` / `"between"` | `"above"` | Drawing layer relative to traces |
| `xsizemode`/`ysizemode` | `"scaled"` / `"pixel"` | `"scaled"` | Sizing mode |

### 3.12 Images (layout-level image overlays)

```json
{
  "images": [
    {
      "source": "https://example.com/logo.png",
      "xref": "paper",
      "yref": "paper",
      "x": 0.05,
      "y": 0.95,
      "sizex": 0.1,
      "sizey": 0.1,
      "xanchor": "left",
      "yanchor": "top",
      "opacity": 1,
      "layer": "above",
      "name": "",
      "templateitemname": "",
      "visible": true
    }
  ]
}
```

### 3.13 Color Axis (shared color axes)

```json
{
  "coloraxis": {
    "colorscale": "Viridis",
    "showscale": true,
    "reversescale": false,
    "autocolorscale": false,
    "cmin": null,
    "cmax": null,
    "cmid": null,
    "colorbar": {
      "title": { "text": "Value", "font": { "size": 12 }, "side": "right" },
      "thickness": 20,
      "thicknessmode": "pixels",
      "len": 0.5,
      "lenmode": "fraction",
      "x": 1.02,
      "y": 0.5,
      "xanchor": "left",
      "yanchor": "middle",
      "xref": "paper",
      "yref": "paper",
      "outlinewidth": 0,
      "outlinecolor": "#444",
      "bgcolor": "rgba(0,0,0,0)",
      "bordercolor": "#444",
      "borderwidth": 0,
      "tickfont": { "size": 10 },
      "tickmode": "auto",
      "tickformat": "",
      "exponentformat": "B",
      "separatethousands": false,
      "nticks": 0,
      "ticks": "",
      "ticklen": 5,
      "tickwidth": 1,
      "tickcolor": "#444",
      "showticklabels": true
    }
  }
}
```

### 3.14 Updatemenus

```json
{
  "updatemenus": [
    {
      "type": "buttons",
      "direction": "right",
      "showactive": true,
      "active": 0,
      "x": 0.5,
      "y": 1.1,
      "xanchor": "center",
      "yanchor": "bottom",
      "xref": "paper",
      "yref": "paper",
      "bgcolor": "#f5f5f5",
      "bordercolor": "#444",
      "borderwidth": 1,
      "font": { "family": "Arial", "size": 12, "color": "#333" },
      "pad": { "r": 3, "t": 3, "b": 3, "l": 3 },
      "buttons": [
        {
          "method": "restyle",
          "args": [{ "mode": "markers" }],
          "label": "Markers",
          "args2": [{ "mode": "lines" }]
        },
        {
          "method": "relayout",
          "args": [{ "yaxis.type": "log" }],
          "label": "Log Scale"
        }
      ],
      "visible": true,
      "name": "",
      "templateitemname": ""
    }
  ]
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `type` | `"buttons"` / `"dropdown"` | `"dropdown"` | Menu style |
| `direction` | `"left"` / `"right"` / `"up"` / `"down"` | `"down"` | Button layout direction |
| `button.method` | `"restyle"` / `"relayout"` / `"update"` / `"animate"` / `"skip"` | `"restyle"` | Action type |
| `args` | array | — | Arguments passed to the method |
| `args2` | array | — | Arguments on second click/deselect |

### 3.15 Sliders

```json
{
  "sliders": [
    {
      "active": 0,
      "currentvalue": { "prefix": "Frame: ", "font": { "size": 12 }, "visible": true, "xanchor": "left", "offset": 0 },
      "steps": [
        { "method": "animate", "args": [["frame1"], { "mode": "immediate" }], "label": "1", "value": "frame1", "visible": true },
        { "method": "animate", "args": [["frame2"], { "mode": "immediate" }], "label": "2", "value": "frame2", "visible": true }
      ],
      "x": 0.5,
      "y": -0.05,
      "xanchor": "center",
      "yanchor": "top",
      "xref": "paper",
      "yref": "paper",
      "len": 0.9,
      "lenmode": "fraction",
      "pad": { "r": 20, "t": 20, "b": 20, "l": 20 },
      "bgcolor": "#f5f5f5",
      "bordercolor": "#444",
      "borderwidth": 1,
      "font": { "family": "Arial", "size": 11, "color": "#333" },
      "tickcolor": "#444",
      "ticklen": 5,
      "tickwidth": 1,
      "minorticklen": 0,
      "name": "",
      "templateitemname": "",
      "visible": true
    }
  ]
}
```

### 3.16 Ternary (for `layout.ternary`)

```json
{
  "ternary": {
    "aaxis": { "title": { "text": "A" }, "min": 0.01, "linecolor": "#444", "showgrid": true, "gridcolor": "#eee", "gridwidth": 1 },
    "baxis": { "title": { "text": "B" }, "min": 0.01, "linecolor": "#444", "showgrid": true, "gridcolor": "#eee" },
    "caxis": { "title": { "text": "C" }, "min": 0.01, "linecolor": "#444", "showgrid": true, "gridcolor": "#eee" },
    "bgcolor": "rgba(0,0,0,0)",
    "sum": 1,
    "domain": { "x": [0, 1], "y": [0, 1] }
  }
}
```

### 3.17 Smith (for `layout.smith`)

```json
{
  "smith": {
    "imaginaryaxis": { "linecolor": "#444", "showgrid": true, "gridcolor": "#eee", "tickfont": { "size": 11 } },
    "realaxis": { "linecolor": "#444", "showgrid": true, "gridcolor": "#eee", "tickfont": { "size": 11 }, "side": "bottom" },
    "bgcolor": "rgba(0,0,0,0)",
    "domain": { "x": [0, 1], "y": [0, 1] }
  }
}
```

### 3.18 Transition & Animation

```json
{
  "transition": {
    "duration": 500,
    "easing": "cubic-in-out",
    "ordering": "layout first"
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `duration` | number ms | `500` | Animation duration |
| `easing` | `"linear"` / `"quad-in"` / `"quad-out"` / `"quad-in-out"` / `"cubic-in"` / `"cubic-out"` / `"cubic-in-out"` / many more | `"cubic-in-out"` | Easing function |
| `ordering` | `"layout first"` / `"traces first"` | `"layout first"` | Animation ordering |

---

## 4. Config Object

The `config` object controls chart behavior (interactivity, modebar, display). This is NOT part of layout — it is a separate top-level parameter.

```json
{
  "config": {
    "staticPlot": false,
    "responsive": false,
    "displayModeBar": "hover",
    "displaylogo": true,
    "showTips": true,
    "showAxisDragHandles": true,
    "showAxisRangeEntryBoxes": true,
    "showLink": false,
    "linkText": "Edit chart",
    "plotlyServerURL": "https://chart-studio.plotly.com",
    "showEditInChartStudio": false,
    "sendData": true,
    "modeBarButtonsToRemove": [],
    "modeBarButtonsToAdd": [],
    "modeBarButtons": false,
    "toImageButtonOptions": {
      "format": "png",
      "filename": "newplot",
      "height": null,
      "width": null,
      "scale": 1
    },
    "editable": false,
    "edits": {
      "annotationPosition": false,
      "annotationTail": false,
      "annotationText": false,
      "axisTitleText": false,
      "colorbarPosition": false,
      "colorbarTitleText": false,
      "legendPosition": false,
      "legendText": false,
      "shapePosition": false,
      "titleText": false,
      "traceName": false
    },
    "doubleClick": "reset+autosize",
    "doubleClickDelay": 300,
    "scrollZoom": false,
    "dragmode": "zoom",
    "hovermode": "closest",
    "hoverdistance": 20,
    "spikedistance": 20,
    "mapboxAccessToken": "",
    "logging": 0,
    "notifyOnLogging": true,
    "queueLength": 0,
    "globalTransforms": [],
    "locale": "en-US",
    "setBackground": "opaque",
    "topojsonURL": "https://cdn.jsdelivr.net/npm/topojson@3.0.2/world-110m.json",
    "fillFrame": false,
    "frameMargins": 0,
    "typesetMath": false,
    "msaa": false,
    "plotGlPixelRatio": 2
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `staticPlot` | boolean | `false` | Disable all interactivity |
| `responsive` | boolean | `false` | Auto-resize with container |
| `displayModeBar` | `true` / `false` / `"hover"` | `"hover"` | Mode bar visibility |
| `scrollZoom` | boolean | `false` | Enable scroll-to-zoom |
| `doubleClick` | `"reset+autosize"` / `"reset"` / `"autosize"` / `false` | `"reset+autosize"` | Double-click behavior |
| `editable` | boolean | `false` | Make chart elements editable |
| `locale` | string | `"en-US"` | Locale for numbers/dates |
| `modeBarButtonsToRemove` | array of strings | `[]` | Remove specific modebar buttons |

---

## 5. Frames (Animation)

```json
{
  "frames": [
    {
      "name": "frame1",
      "group": "group1",
      "data": [
        {
          "y": [1, 2, 3]
        }
      ],
      "layout": {
        "title": { "text": "Frame 1" }
      },
      "traces": [0],
      "baseframe": "base1"
    },
    {
      "name": "frame2",
      "group": "group1",
      "data": [
        {
          "y": [4, 5, 6]
        }
      ],
      "layout": {
        "title": { "text": "Frame 2" }
      },
      "traces": [0],
      "baseframe": "base1"
    }
  ]
}
```

| Key | Type | Description |
|-----|------|-------------|
| `name` | string | Frame identifier |
| `group` | string | Group for animation sequencing |
| `data` | array of trace partials | Changes to apply to traces |
| `layout` | object | Changes to apply to layout |
| `traces` | array of ints | Which trace indices to update |
| `baseframe` | string | Inherit from another frame |

---

## 6. Complete Minimal Examples

### Scatter Plot

```json
{
  "data": [
    {
      "type": "scatter",
      "x": [1, 2, 3, 4],
      "y": [10, 15, 13, 17],
      "mode": "markers",
      "marker": { "color": "red", "size": 8 }
    }
  ],
  "layout": {
    "title": { "text": "Simple Scatter" },
    "xaxis": { "title": { "text": "X" } },
    "yaxis": { "title": { "text": "Y" } }
  }
}
```

### Bar Chart

```json
{
  "data": [
    {
      "type": "bar",
      "x": ["A", "B", "C"],
      "y": [20, 14, 23]
    }
  ],
  "layout": {
    "title": { "text": "Simple Bar" },
    "barmode": "group"
  }
}
```

### Pie Chart

```json
{
  "data": [
    {
      "type": "pie",
      "values": [19, 26, 55],
      "labels": ["Residential", "Non-Residential", "Utility"],
      "textinfo": "label+percent"
    }
  ]
}
```

### Multiple Subplots (Dual Y-Axis)

```json
{
  "data": [
    {
      "type": "bar",
      "x": [1, 2, 3],
      "y": [100, 200, 300],
      "yaxis": "y",
      "name": "Revenue"
    },
    {
      "type": "scatter",
      "x": [1, 2, 3],
      "y": [10, 15, 8],
      "yaxis": "y2",
      "mode": "lines+markers",
      "name": "Growth %"
    }
  ],
  "layout": {
    "title": { "text": "Dual Axis" },
    "yaxis": { "title": { "text": "Revenue" } },
    "yaxis2": { "title": { "text": "Growth %" }, "overlaying": "y", "side": "right" }
  }
}
```

### Grid of 4 Subplots

```json
{
  "data": [
    { "type": "scatter", "x": [1,2,3], "y": [1,2,3], "xaxis": "x", "yaxis": "y" },
    { "type": "scatter", "x": [1,2,3], "y": [4,5,6], "xaxis": "x2", "yaxis": "y" },
    { "type": "scatter", "x": [1,2,3], "y": [7,8,9], "xaxis": "x", "yaxis": "y2" },
    { "type": "scatter", "x": [1,2,3], "y": [10,11,12], "xaxis": "x2", "yaxis": "y2" }
  ],
  "layout": {
    "grid": { "rows": 2, "columns": 2, "pattern": "independent" },
    "xaxis": { "domain": [0, 0.45] },
    "xaxis2": { "domain": [0.55, 1] },
    "yaxis": { "domain": [0, 0.45] },
    "yaxis2": { "domain": [0.55, 1] }
  }
}
```

---

## 7. Schema & Reference URLs

| Resource | URL |
|----------|-----|
| Full JSON schema (raw) | `https://api.plot.ly/v2/plot-schema?format=json&sha1=%27%27` |
| Formatted schema (all types) | `https://api.plot.ly/v2/plot-schema?sha1=%27%27` |
| JavaScript full reference | `https://plotly.com/javascript/reference/` |
| Layout reference | `https://plotly.com/javascript/reference/layout/` |
| Scatter reference | `https://plotly.com/javascript/reference/scatter/` |
| Bar reference | `https://plotly.com/javascript/reference/bar/` |
| Pie reference | `https://plotly.com/javascript/reference/pie/` |
| Config options | `https://plotly.com/javascript/configuration-options/` |
| Schema viewer | `https://plot.github.io/schema-viewer/` |
| Plotly.js source | `https://github.com/plotly/plotly.js` |

> **Note:** All trace types listed here are available in plotly.js v3.x (2025+). Deprecated traces like `heatmapgl` and `pointcloud` have been removed. The `title` attribute is now always an object (`title.text`), not a string. Transforms (`filter`, `groupby`, `sort`) have been removed.