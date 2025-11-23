# Minard figure - brought to life

## Overview

Here is an interactive visualisation of Minard's famous map of Napoleon's Russian Campaign, 1812. The presentation is a flow map with continuous bars where width represents troop numbers, oriented perpendicular to the direction of travel.

## Historical Context

### Charles Joseph Minard's Map

Charles Joseph Minard (1781–1870) was a French civil engineer and pioneer in the field of information graphics. His 1869 map of Napoleon's Russian campaign is widely regarded as one of the best statistical graphics ever created. The map elegantly displays six types of information: geography (rivers and cities), the army's direction (advance and retreat paths), the number of troops (bar width), location names, temperature during the retreat, and time (dates).

Edward Tufte, the renowned statistician and information designer, described Minard's map as "probably the best statistical graphic ever drawn" in his book *The Visual Display of Quantitative Information*.

### Napoleon's Russian Campaign, 1812

Napoleon Bonaparte's invasion of Russia in 1812 was one of the most catastrophic military campaigns in history. Beginning on 24 June 1812, Napoleon's Grande Armée crossed the Niemen River with approximately 422,000 soldiers. The campaign saw several major battles including:

- **Battle of Vitebsk** (27–28 July): A French victory that cost significant casualties
- **Battle of Smolensk** (16–18 August): Another French victory, but with heavy losses
- **Battle of Maloyaroslavets** (24 October): A tactical French victory during the retreat
- **Battle of Berezina** (26–29 November): A desperate crossing of the Berezina River during the retreat

Despite reaching Moscow on 14 September 1812, Napoleon found the city largely abandoned and set ablaze. The harsh Russian winter, combined with supply shortages, disease, and constant harassment by Russian forces, decimated the Grande Armée. By the time the remnants of the army crossed back over the Niemen River on 6 December 1812, only approximately 10,000 soldiers remained—a staggering loss of over 97% of the original force.

The campaign marked a turning point in the Napoleonic Wars and contributed significantly to Napoleon's eventual downfall.

## Technical Details

### Implementation

This visualisation recreates Minard's map using Python and matplotlib, bringing the historical data to life through both static and animated representations.

**Key Features:**

- Flow map visualisation with continuous trapezoidal bars representing troop numbers
- Perpendicular bar orientation relative to the direction of travel
- Animated GIF showing Napoleon's progress along the campaign route
- Temperature graph showing the harsh winter conditions during the retreat
- Battle markers indicating key engagements along the route
- Geographic features including major rivers (Niemen, Dnieper, and Berezina)

### Technology Stack

- **Python 3**: Core programming language
- **matplotlib**: Primary plotting and animation library
  - `matplotlib.pyplot`: Plotting functionality
  - `matplotlib.patches`: Custom shapes (Polygon, Circle, Arc, etc.)
  - `matplotlib.animation.FuncAnimation`: Animation support
- **numpy**: Numerical computations for coordinate calculations
- **cartopy** (optional): Geographic projections and map backgrounds
- **imageio** (optional): Enhanced GIF creation support

### Technical Approach

The visualisation uses a custom `draw_flow_segment()` function that creates trapezoidal polygons perpendicular to the direction of travel. Each segment's width is proportional to the number of troops at that point, creating a smooth, continuous flow map.

**Key Algorithms:**

- **Flow segment calculation**: Uses vector mathematics to calculate perpendicular offsets for bar width
- **Coordinate interpolation**: Smooth animation between waypoints using linear interpolation
- **Scale factor calculation**: Dynamically scales troop numbers to visual width in degrees

The animation features a caricature of Napoleon that moves along the route, with different expressions for the advance (confident) and retreat (sad) phases. The animation consists of 400 frames rendered at 10 frames per second.

### Output Files

- `minard_plot.png`: High-resolution static image (300 DPI)
- `minard_animation.gif`: Animated GIF showing Napoleon's journey (400 frames, 10 fps)
- `minard.mmd`: Mermaid diagram file representing the campaign flow

### Mermaid Visualisation

In addition to the Python-generated visualisations, this project includes a [Mermaid](https://mermaid.live) diagram file (`minard.mmd`) that provides an alternative flowchart representation of Napoleon's campaign.

**What is Mermaid?**

Mermaid is a text-based diagramming and charting tool that allows you to create diagrams using simple markdown-like syntax. It supports a wide variety of diagram types including flowcharts, sequence diagrams, Gantt charts, and more. Mermaid diagrams can be rendered in many platforms including GitHub, GitLab, documentation sites, and the [Mermaid Live Editor](https://mermaid.live).

The `minard.mmd` file contains a flowchart visualisation that shows:

- The advance path from Kowno to Moscow with troop numbers at each location
- The retreat path from Moscow back to Kowno, showing the devastating troop losses
- Temperature data during the retreat phase
- Geographic coordinates and dates for key waypoints
- Visual styling that matches the original Minard colour scheme (beige for advance, dark for retreat)

You can view and edit the Mermaid diagram by:

1. Opening the file in the [Mermaid Live Editor](https://mermaid.live)
2. Copying the contents of `minard.mmd` and pasting it into the editor
3. The diagram will render automatically, and you can export it as PNG or SVG

This provides a complementary view of the campaign data that emphasises the flow and sequence of events, making it easy to understand the progression of the campaign and the relationship between locations, troop numbers, and temperature.

### Dependencies

**Required:**

```bash
pip install matplotlib numpy
```

**Optional (for enhanced features):**

```bash
pip install cartopy  # For geographic map backgrounds
pip install imageio  # For improved GIF creation
```

## Usage

Run the script to generate both static and animated visualisations:

```bash
python plot_minard.py
```

The script will generate `minard_plot.png` and `minard_animation.gif` in the current directory.

## License

This project is for educational purposes. Please ensure you have appropriate permissions for any external data sources used.

## Author

**S. Hallett**  
Course: MK:U, Big Data and Visualisation  
Date: 23/11/2025

---

*This project uses UK spelling conventions throughout and follows PEP 8 coding standards for Python code.*
