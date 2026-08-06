# ApexCharts.js JSON Chart Schema — Complete Reference

> This document describes every ApexCharts chart purely as a **JSON object**. Every chart is a single `options` object combining `chart`, `series`, `xaxis`, `yaxis`, and other styling keys — there is no separate `data`/`layout` split like other libraries.

---

## 1. Top-Level Options Structure

```json
{
  "chart": { ... },
  "series": [ ... ],
  "xaxis": { ... },
  "yaxis": { ... },
  "title": { ... },
  "subtitle": { ... },
  "labels": [ ... ],
  "colors": [ ... ],
  "dataLabels": { ... },
  "stroke": { ... },
  "fill": { ... },
  "legend": { ... },
  "tooltip": { ... },
  "grid": { ... },
  "plotOptions": { ... },
  "annotations": { ... },
  "responsive": [ ... ],
  "markers": { ... },
  "states": { ... }
}
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `chart` | `object` | Yes | Chart-level config: type, size, animations, toolbar |
| `series` | `array` | Yes | The actual data being plotted (shape varies by chart type — see Section 2) |
| `xaxis` | `object` | Usually | Category labels / x-axis config |
| `yaxis` | `object` | No | Y-axis range/formatting config |
| `title` / `subtitle` | `object` | No | Chart title/subtitle text and styling |
| `labels` | `array` | Chart-type dependent | Category names for pie/donut/polarArea/radialBar |
| `colors` | `array` | No | Color palette override |
| `plotOptions` | `object` | Chart-type dependent | Per-chart-type specific settings (e.g. `plotOptions.bar`, `plotOptions.pie`) |

Unlike Plotly's `data` (array of traces) + `layout` (visual config) split, ApexCharts merges everything into one flat `options` object, and `series` alone carries the plotted values.

---

## 2. Series Data Formats (the `series` key)

The shape of `series` is the single most important thing to get right — it **changes depending on `chart.type`**.

### 2.1 Axis charts (line, area, bar, column, scatter, heatmap, candlestick, boxPlot, radar)

```json
"series": [
  { "name": "Series 1", "data": [30, 40, 35, 50, 49, 60, 70] },
  { "name": "Series 2", "data": [23, 12, 54, 61, 32, 56, 81] }
]
```
<cite index="23-1">series is an array of objects. Each series object can have: name (shown in legend and tooltips), data (array of data points, which can be numbers, [x, y] pairs, or objects { x, y }), type (override chart type for this series in combo charts), color, and group (for grouped bar charts)</cite>

### 2.2 Pie / Donut / RadialBar / PolarArea (non-axis charts)

```json
"series": [44, 55, 13, 43, 22],
"labels": ["Apple", "Mango", "Orange", "Watermelon", "Grape"]
```
<cite index="24-1">The data format for the pie/donut series is a single-dimensional array of numeric values. The names of the values have to be provided in the labels array separately</cite> — this same flat-array + separate `labels` pattern applies to `radialBar` and `polarArea` too.

### 2.3 Scatter / Bubble

```json
"series": [
  { "name": "Series 1", "data": [[16.4, 5.4], [21.7, 2], [25.4, 3]] }
]
```
<cite index="23-1">Paired data format for scatter/bubble: series: [{ name: 'Series 1', data: [ [16.4, 5.4], [21.7, 2], [25.4, 3] ] }]</cite> — each pair is `[x, y]` (bubble charts add a third value for radius: `[x, y, z]`).

### 2.4 Candlestick (OHLC)

```json
"series": [
  {
    "data": [
      { "x": "2024-01-01", "y": [6629, 6650, 6570, 6600] },
      { "x": "2024-01-02", "y": [6600, 6680, 6590, 6650] }
    ]
  }
]
```
<cite index="32-1">Candlestick chart is just like other cartesian charts, only the y value is an array of 4 members called OHLC (Open-High-Low-Close)</cite>.

### 2.5 BoxPlot

```json
"series": [
  {
    "data": [
      { "x": "2024-01-01", "y": [54, 66, 69, 75, 88] }
    ]
  }
]
```
<cite index="32-1">Box plot chart is similar to candlestick chart, only the y value is an array of 5 members (Minimum-First Quartile-Median-Third Quartile-Maximum)</cite>.

### 2.6 Heatmap

```json
"series": [
  { "name": "Series 1", "data": [{ "x": "W1", "y": 22 }, { "x": "W2", "y": 29 }, { "x": "W3", "y": 13 }] },
  { "name": "Series 2", "data": [{ "x": "W1", "y": 43 }, { "x": "W2", "y": 10 }, { "x": "W3", "y": 65 }] }
]
```
<cite index="40-1">The data format for a heatmap chart is the same as used on other axis based charts (line/bar)</cite> — each `series` row becomes one row of the heatmap, and each `{x,y}` pair becomes one cell, colored by its `y` (heat) value.

### 2.7 Radar

```json
"series": [
  { "name": "Series 1", "data": [80, 50, 30, 40, 100, 20] }
],
"xaxis": { "categories": ["Speed", "Strength", "Agility", "Stamina", "Skill", "Luck"] }
```
Same flat-array format as line/bar, but plotted on radial axes instead of cartesian ones — <cite index="37-1">the data format for radar chart per-series is also similar but instead of x values they are variables and instead of y values they are the only values for the variables with type of Numeric</cite>.

### 2.8 Timeline / RangeBar

```json
"series": [
  { "data": [{ "x": "Design", "y": [1551398400000, 1551657600000] }] }
]
```
<cite index="23-1">Timeline / RangeBar data format: series: [{ data: [{ x: 'Design', y: [ new Date('2019-03-05').getTime(), new Date('2019-03-08').getTime() ] }] }]</cite> — `y` is a `[start, end]` timestamp pair.

---

## 3. Chart Object (`chart` key)

```json
{
  "chart": {
    "type": "line",
    "height": 350,
    "width": "100%",
    "id": "chart1",
    "group": "sync-group",
    "toolbar": { "show": true, "tools": { "download": true, "zoom": true, "pan": true } },
    "zoom": { "enabled": true, "type": "x" },
    "animations": { "enabled": true, "speed": 800 },
    "sparkline": { "enabled": false },
    "background": "transparent",
    "foreColor": "#333",
    "stacked": false,
    "events": {}
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `type` | `"line"` / `"area"` / `"bar"` / `"pie"` / `"donut"` / `"radialBar"` / `"scatter"` / `"bubble"` / `"heatmap"` / `"candlestick"` / `"boxPlot"` / `"radar"` / `"polarArea"` / `"rangeBar"` / `"rangeArea"` / `"treemap"` / `"funnel"` / `"pyramid"` | — | <cite index="21-1">Set the ApexCharts chart type</cite> — this is the single most important config key |
| `height` / `width` | number or string | `"auto"` | Chart dimensions in px or `%` |
| `id` / `group` | string | — | Used to sync multiple charts' tooltip/zoom/pan together |
| `stacked` | boolean | `false` | Stack series on top of each other (bar/area) |
| `toolbar.show` | boolean | `true` | Show/hide the export/zoom toolbar |
| `zoom.enabled` | boolean | `true` | Allow zooming via drag |
| `animations.enabled` | boolean | `true` | Enable/disable chart animations |
| `sparkline.enabled` | boolean | `false` | Strip all axes/labels for a minimal sparkline look |

---

## 4. X-Axis / Y-Axis (`xaxis`, `yaxis`)

```json
{
  "xaxis": {
    "type": "category",
    "categories": ["Jan", "Feb", "Mar", "Apr"],
    "title": { "text": "Month" },
    "labels": { "rotate": -45, "show": true },
    "tickAmount": 6,
    "min": null,
    "max": null
  },
  "yaxis": {
    "title": { "text": "Revenue ($)" },
    "min": 0,
    "max": 5000,
    "labels": { "formatter": null },
    "opposite": false,
    "logarithmic": false
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `xaxis.type` | `"category"` / `"datetime"` / `"numeric"` | `"category"` | How to interpret `categories` values |
| `xaxis.categories` | array of strings/numbers | — | The x-axis point labels (required for most axis charts, not needed for `datetime` type if x is embedded in `series[].data`) |
| `yaxis.min` / `max` | number | auto | Force axis bounds |
| `yaxis.opposite` | boolean | `false` | Move this y-axis to the right side (for dual-axis charts) |
| `yaxis.logarithmic` | boolean | `false` | Use log scale |

For multiple y-axes (dual-axis charts), `yaxis` can be an **array** of axis objects instead of a single object, each tied to a series via `seriesName`.

---

## 5. Title & Subtitle

```json
{
  "title": { "text": "Daily Revenue Trend", "align": "left", "style": { "fontSize": "18px", "color": "#333" } },
  "subtitle": { "text": "Last 30 days", "align": "left", "style": { "fontSize": "12px", "color": "#999" } }
}
```

---

## 6. Data Labels

```json
{
  "dataLabels": {
    "enabled": true,
    "formatter": null,
    "textAnchor": "middle",
    "style": { "fontSize": "12px", "colors": ["#fff"] },
    "background": { "enabled": true, "borderRadius": 2 }
  }
}
```

---

## 7. Stroke (line/border styling)

```json
{
  "stroke": {
    "curve": "smooth",
    "width": 2,
    "dashArray": 0,
    "colors": undefined
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `curve` | `"smooth"` / `"straight"` / `"stepline"` | `"smooth"` | Line interpolation style |
| `width` | number or array | `2` | Line thickness |
| `dashArray` | number or array | `0` | Dashed line pattern |

---

## 8. Fill

```json
{
  "fill": {
    "type": "solid",
    "opacity": 0.85,
    "gradient": {
      "shade": "light",
      "type": "vertical",
      "shadeIntensity": 0.25,
      "opacityFrom": 0.85,
      "opacityTo": 0.25,
      "stops": [0, 100]
    }
  }
}
```

---

## 9. Legend

```json
{
  "legend": {
    "show": true,
    "position": "bottom",
    "horizontalAlign": "center",
    "fontSize": "13px",
    "markers": { "width": 12, "height": 12 },
    "onItemClick": { "toggleDataSeries": true }
  }
}
```

---

## 10. Tooltip

```json
{
  "tooltip": {
    "enabled": true,
    "shared": true,
    "followCursor": false,
    "x": { "show": true, "format": "dd MMM" },
    "y": { "formatter": null }
  }
}
```

---

## 11. Grid

```json
{
  "grid": {
    "show": true,
    "borderColor": "#e0e0e0",
    "strokeDashArray": 0,
    "xaxis": { "lines": { "show": false } },
    "yaxis": { "lines": { "show": true } }
  }
}
```

---

## 12. PlotOptions (chart-type-specific settings)

`plotOptions` holds settings unique to a specific chart type — only the block matching `chart.type` is used.

### Bar / Column
```json
{
  "plotOptions": {
    "bar": {
      "horizontal": false,
      "columnWidth": "70%",
      "borderRadius": 4,
      "dataLabels": { "position": "top" }
    }
  }
}
```
<cite index="1-1">In ApexCharts, both bar and column use chart.type: 'bar'. A bar chart sets plotOptions.bar.horizontal: true; a column chart omits it (defaults to false)</cite>.

### Pie / Donut
```json
{
  "plotOptions": {
    "pie": {
      "startAngle": 0,
      "endAngle": 360,
      "donut": { "size": "65%" }
    }
  }
}
```

### RadialBar
```json
{
  "plotOptions": {
    "radialBar": {
      "hollow": { "size": "50%" },
      "track": { "background": "#f2f2f2" },
      "dataLabels": { "name": { "show": true }, "value": { "show": true } }
    }
  }
}
```

### Candlestick
```json
{
  "plotOptions": {
    "candlestick": {
      "colors": { "upward": "#00B746", "downward": "#EF403C" },
      "wick": { "useFillColor": true }
    }
  }
}
```

### Heatmap
```json
{
  "plotOptions": {
    "heatmap": {
      "radius": 2,
      "colorScale": {
        "ranges": [
          { "from": 0, "to": 25, "color": "#00A100" },
          { "from": 26, "to": 50, "color": "#128FD9" },
          { "from": 51, "to": 100, "color": "#FF0000" }
        ]
      }
    }
  }
}
```

---

## 13. Colors

```json
{
  "colors": ["#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0"]
}
```

Array of hex colors, one per series (or per data point for pie/donut/heatmap).

---

## 14. Annotations

```json
{
  "annotations": {
    "yaxis": [
      { "y": 8000, "borderColor": "#00E396", "label": { "text": "Target" } }
    ],
    "xaxis": [
      { "x": "2024-01-15", "borderColor": "#775DD0", "label": { "text": "Launch" } }
    ],
    "points": [
      { "x": "2024-01-10", "y": 8500, "marker": { "size": 6 }, "label": { "text": "Peak" } }
    ]
  }
}
```

---

## 15. Responsive (breakpoint overrides)

```json
{
  "responsive": [
    {
      "breakpoint": 768,
      "options": {
        "chart": { "height": 250 },
        "legend": { "position": "bottom" }
      }
    }
  ]
}
```

---

## 16. Complete Minimal Examples

### Line Chart
```json
{
  "chart": { "type": "line", "height": 350 },
  "series": [{ "name": "sales", "data": [30, 40, 35, 50, 49, 60, 70] }],
  "xaxis": { "categories": [1991, 1992, 1993, 1994, 1995, 1996, 1997] }
}
```
<cite index="8-1">A minimal ApexCharts working example — options passed to new ApexCharts(el, options); chart.render()</cite>.

### Bar Chart
```json
{
  "chart": { "type": "bar", "height": 350 },
  "series": [{ "name": "Revenue", "data": [44, 55, 57, 56, 61, 58] }],
  "xaxis": { "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] }
}
```
<cite index="15-1">var options = { chart: { type: 'bar' }, series: [{ name: 'Revenue', data: [44, 55, 57, 56, 61, 58] }], xaxis: { categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] } }</cite>.

### Pie / Donut Chart
```json
{
  "chart": { "type": "donut", "height": 350 },
  "series": [44, 55, 13, 33],
  "labels": ["Apple", "Mango", "Orange", "Watermelon"]
}
```

### Dual Y-Axis (Bar + Line combo)
```json
{
  "chart": { "type": "line", "height": 350 },
  "series": [
    { "name": "Revenue", "type": "column", "data": [100, 200, 300] },
    { "name": "Growth %", "type": "line", "data": [10, 15, 8] }
  ],
  "xaxis": { "categories": ["Q1", "Q2", "Q3"] },
  "yaxis": [
    { "title": { "text": "Revenue" } },
    { "opposite": true, "title": { "text": "Growth %" } }
  ]
}
```

---

## 17. Chart Types Cheat Sheet

| `chart.type` | `series` shape | `labels` needed? | Common use case |
|---|---|---|---|
| `line` / `area` | `[{ name, data: [numbers] }]` | No (use `xaxis.categories`) | Trends over time |
| `bar` (vertical/horizontal via `plotOptions.bar.horizontal`) | `[{ name, data: [numbers] }]` | No | Comparing categories |
| `pie` / `donut` | flat `[numbers]` | **Yes** | Proportional breakdown |
| `radialBar` / `polarArea` | flat `[numbers]` | **Yes** | Single-value KPIs / proportions |
| `scatter` / `bubble` | `[{ name, data: [[x,y]] or [[x,y,z]] }]` | No | Correlation |
| `heatmap` | `[{ name, data: [{x,y}] }]` per row | No | Density/intensity matrix |
| `candlestick` | `[{ data: [{x, y:[O,H,L,C]}] }]` | No | Financial OHLC |
| `boxPlot` | `[{ data: [{x, y:[min,Q1,med,Q3,max]}] }]` | No | Statistical distribution |
| `radar` | `[{ name, data: [numbers] }]` | No (use `xaxis.categories`) | Multi-variable comparison |

---

## 18. Reference URLs

| Resource | URL |
|----------|-----|
| Full docs | `https://apexcharts.com/docs/` |
| First chart guide | `https://apexcharts.com/docs/creating-first-javascript-chart/` |
| Installation | `https://apexcharts.com/docs/installation/` |
| Chart type option | `https://apexcharts.com/docs/options/chart/type/` |
| Series option | `https://apexcharts.com/docs/options/series/` |
| X-axis options | `https://apexcharts.com/docs/options/xaxis/` |
| Chart type guides (per-type series formats) | `https://apexcharts.com/docs/chart-types/` |
| Methods (updateOptions, updateSeries) | `https://apexcharts.com/docs/methods/` |
| GitHub source | `https://github.com/apexcharts/apexcharts.js` |

> **Note:** Unlike Plotly, ApexCharts has no separate `config` or `frames` top-level objects — chart interactivity settings live inside `chart` (toolbar, zoom, animations), and there's no built-in frame-based animation API; live updates instead use `chart.updateSeries()`/`chart.updateOptions()` at runtime.
