#!/usr/bin/env python3
"""
Plot of Minard's Map of Napoleon's Russian Campaign, 1812
Flow map with continuous bars where width represents troop numbers,
oriented perpendicular to the direction of travel.

HOW TO RUN:
-----------
1. Install required dependencies:
   pip install matplotlib numpy
   (Optional, for map background: pip install cartopy)
   (Optional, for better animated GIF support: pip install imageio)

2. Run the script:
   python plot_minard.py

3. The script will generate 'minard_plot.png' and 'minard_animation.gif' 
   in the current directory. The animated GIF will show Napoleon moving
   along the campaign route when viewed in an image viewer that supports
   animated GIFs (most web browsers and image viewers).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon, FancyBboxPatch, Arc
from matplotlib.patches import ConnectionPatch
from matplotlib.animation import FuncAnimation
import numpy as np

# Try to import cartopy for map background, fallback to simple if not available
try:
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    HAS_CARTOPY = True
except ImportError:
    HAS_CARTOPY = False
    print("Note: cartopy not available, using simple background")

# Advance path data (West to East)
advance = [
    {"name": "Kowno (Kaunas)", "lat": 54.9, "lon": 24.0, "troops": 422000, "date": "June 24", "battle": False},
    {"name": "Wilna (Vilnius)", "lat": 54.7, "lon": 25.3, "troops": 400000, "battle": False},
    {"name": "Witebsk (Vitebsk)", "lat": 55.2, "lon": 30.2, "troops": 175000, "battle": True, "battle_name": "Battle of Vitebsk"},
    {"name": "Smolensk", "lat": 54.8, "lon": 32.0, "troops": 145000, "battle": True, "battle_name": "Battle of Smolensk"},
    {"name": "Dorogobouge", "lat": 54.9, "lon": 33.2, "troops": 127000, "battle": False},
    {"name": "Moscou (Moscow)", "lat": 55.8, "lon": 37.6, "troops": 100000, "date": "Sept 14", "battle": False},
]

# Retreat path data (East to West, more southerly)
retreat = [
    {"name": "Moscou (Moscow)", "lat": 55.8, "lon": 37.6, "troops": 100000, "battle": False},
    {"name": "Malo-Jaroslavetz", "lat": 55.0, "lon": 36.5, "troops": 96000, "battle": True, "battle_name": "Battle of Maloyaroslavets"},
    {"name": "Mojaisk (Mozhaysk)", "lat": 55.5, "lon": 36.0, "troops": 87000, "battle": False},
    {"name": "Smolensk", "lat": 54.8, "lon": 32.0, "troops": 50000, "battle": False},
    {"name": "Orscha (Orsha)", "lat": 54.5, "lon": 30.4, "troops": 37000, "battle": False},
    {"name": "Studienska (Studenka)", "lat": 54.4, "lon": 30.0, "troops": 24000, "battle": True, "battle_name": "Battle of Berezina"},
    {"name": "Minsk", "lat": 53.9, "lon": 27.6, "troops": 20000, "battle": False},
    {"name": "Wilna (Vilnius)", "lat": 54.7, "lon": 25.3, "troops": 12000, "battle": False},
    {"name": "Kowno (Kaunas)", "lat": 54.9, "lon": 24.0, "troops": 10000, "date": "Dec 6", "battle": False},
]

# Temperature data during retreat
temperatures = [
    {"date": "Oct 18", "temp": 0, "lon": 37.6},
    {"date": "Nov 9", "temp": -9, "lon": 36.0},
    {"date": "Nov 14", "temp": -21, "lon": 32.0},
    {"date": "Nov 28", "temp": -26, "lon": 30.0},
    {"date": "Dec 7", "temp": -30, "lon": 24.0},
]


def draw_flow_segment(ax, x1, y1, x2, y2, width1, width2, color, alpha=1.0):
    """
    Draw a flow segment as a trapezoid (rhomboid) perpendicular to the direction of travel.
    Creates smooth transitions between segments.
    width1: width at start point
    width2: width at end point
    """
    # Calculate direction vector
    dx = x2 - x1
    dy = y2 - y1
    length = np.sqrt(dx**2 + dy**2)
    
    if length == 0:
        return
    
    # Normalise direction vector
    dx_norm = dx / length
    dy_norm = dy / length
    
    # Perpendicular vector (rotate 90 degrees counterclockwise)
    perp_x = -dy_norm
    perp_y = dx_norm
    
    # Half-widths in coordinate units (degrees)
    half_width1 = width1 / 2
    half_width2 = width2 / 2
    
    # Calculate the four corners of the trapezoid
    # Start point offsets
    p1 = (x1 + perp_x * half_width1, y1 + perp_y * half_width1)
    p2 = (x1 - perp_x * half_width1, y1 - perp_y * half_width1)
    # End point offsets
    p3 = (x2 - perp_x * half_width2, y2 - perp_y * half_width2)
    p4 = (x2 + perp_x * half_width2, y2 + perp_y * half_width2)
    
    # Create polygon with no border (edgecolor matches facecolor for seamless look)
    if HAS_CARTOPY and hasattr(ax, 'projection'):
        # For cartopy, we need to specify the transform
        polygon = Polygon([p1, p2, p3, p4], closed=True, 
                          facecolor=color, edgecolor=color, 
                          linewidth=0, alpha=alpha, zorder=2,
                          transform=ccrs.PlateCarree())
    else:
        polygon = Polygon([p1, p2, p3, p4], closed=True, 
                          facecolor=color, edgecolor=color, 
                          linewidth=0, alpha=alpha, zorder=2)
    
    ax.add_patch(polygon)


# Create figure with main map emphasised and minimal temperature chart
fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(10, 1, hspace=0.05)  # Reduced spacing to bring temperature graph closer

# Create main map axis with or without cartopy
if HAS_CARTOPY:
    ax1 = fig.add_subplot(gs[0:9, 0], projection=ccrs.PlateCarree())
else:
    ax1 = fig.add_subplot(gs[0:9, 0])  # Main map - takes 9/10 of space

ax2 = fig.add_subplot(gs[9, 0])   # Temperature - minimal, takes 1/10

# Extract coordinates and troop numbers
advance_lons = [p["lon"] for p in advance]
advance_lats = [p["lat"] for p in advance]
advance_troops = [p["troops"] for p in advance]

retreat_lons = [p["lon"] for p in retreat]
retreat_lats = [p["lat"] for p in retreat]
retreat_troops = [p["troops"] for p in retreat]

# Scale factor for width (troops to visual width in degrees)
# The coordinate system spans ~13.6 degrees longitude and ~1.9 degrees latitude
# Increased width to make bars chunkier and more visible
max_troops = max(max(advance_troops), max(retreat_troops))
desired_max_width = 0.8  # degrees - increased from 0.25 for chunkier bars
scale_factor = desired_max_width / max_troops

print(f"Scale factor: {scale_factor:.2e}")
print(f"Max troops: {max_troops:,}")
print(f"Max bar width: {max_troops * scale_factor:.4f} degrees")

# Draw advance path as continuous bars with smooth transitions (trapezoids)
for i in range(len(advance) - 1):
    width1 = advance_troops[i] * scale_factor
    width2 = advance_troops[i + 1] * scale_factor
    draw_flow_segment(
        ax1,
        advance_lons[i], advance_lats[i],
        advance_lons[i + 1], advance_lats[i + 1],
        width1, width2,
        "#d4a574",
        alpha=1.0
    )

# Draw retreat path as continuous bars with smooth transitions (trapezoids)
for i in range(len(retreat) - 1):
    width1 = retreat_troops[i] * scale_factor
    width2 = retreat_troops[i + 1] * scale_factor
    draw_flow_segment(
        ax1,
        retreat_lons[i], retreat_lats[i],
        retreat_lons[i + 1], retreat_lats[i + 1],
        width1, width2,
        "#2c3e50",
        alpha=1.0
    )

# Add annotations for all locations with leader lines
all_points = advance + retreat
seen_locations = set()

for point in all_points:
    loc_key = (point["lon"], point["lat"])
    if loc_key in seen_locations:
        continue
    seen_locations.add(loc_key)
    
    # Extract location name
    name_parts = point["name"].split("(")
    city_name = name_parts[0].strip()
    country = name_parts[1].strip(")") if len(name_parts) > 1 else ""
    
    # Build label without coordinates (remove battle info from text - shown as marker)
    label_parts = [city_name]
    if country:
        label_parts.append(f"({country})")
    if "date" in point:
        label_parts.append(point["date"])
    # Battle info removed - will be shown as marker at location with label
    
    label = "\n".join(label_parts)
    
    # Position annotation offset based on location (further away to avoid covering plot)
    offset_x = 50 if point["lon"] < 30 else -50
    offset_y = 50 if point["lat"] < 55 else -50
    
    # No background or border for annotations
    ax1.annotate(
        label,
        (point["lon"], point["lat"]),
        xytext=(offset_x, offset_y),
        textcoords="offset points",
        fontsize=9,
        bbox=None,  # No box
        zorder=5,
        ha="left" if offset_x > 0 else "right",
        color="red" if point.get("battle", False) else "black",
        weight="bold" if point.get("battle", False) else "normal"
    )
    
    # Add leader line from annotation to location
    # Draw a line from the location to near the annotation
    line_end_x = point["lon"] + offset_x * 0.4
    line_end_y = point["lat"] + offset_y * 0.4
    
    if HAS_CARTOPY:
        # For cartopy, we need to use transform
        ax1.plot(
            [point["lon"], line_end_x],
            [point["lat"], line_end_y],
            color="gray",
            linestyle="--",
            linewidth=0.8,
            alpha=0.6,
            transform=ccrs.PlateCarree(),
            zorder=3
        )
    else:
        ax1.plot(
            [point["lon"], line_end_x],
            [point["lat"], line_end_y],
            color="gray",
            linestyle="--",
            linewidth=0.8,
            alpha=0.6,
            zorder=3
        )

# Add battle markers at exact locations
def draw_battle_marker(ax, x, y, battle_name=None, transform=None):
    """Draw crossed swords marker at battle location with label"""
    marker_size = 0.15  # Size in degrees
    
    # Draw crossed swords (X shape) - brighter red
    bright_red = "#ff0000"  # Bright red
    if HAS_CARTOPY and transform:
        # Diagonal line 1 (top-left to bottom-right)
        ax.plot([x - marker_size, x + marker_size], 
                [y + marker_size, y - marker_size],
                color=bright_red, linewidth=3, transform=transform, zorder=6)
        # Diagonal line 2 (top-right to bottom-left)
        ax.plot([x + marker_size, x - marker_size], 
                [y + marker_size, y - marker_size],
                color=bright_red, linewidth=3, transform=transform, zorder=6)
        # Add a small circle at center
        center = mpatches.Circle((x, y), radius=marker_size * 0.15,
                                facecolor=bright_red, edgecolor="#000",
                                linewidth=1, transform=transform, zorder=7)
        ax.add_patch(center)
        
        # Add battle label next to the marker (no background or border)
        if battle_name:
            ax.text(x + marker_size * 1.5, y, battle_name, 
                   fontsize=8, color="#8b0000", weight="bold",
                   transform=transform, zorder=8)
    else:
        # Diagonal line 1
        ax.plot([x - marker_size, x + marker_size], 
                [y + marker_size, y - marker_size],
                color=bright_red, linewidth=3, zorder=6)
        # Diagonal line 2
        ax.plot([x + marker_size, x - marker_size], 
                [y + marker_size, y - marker_size],
                color=bright_red, linewidth=3, zorder=6)
        # Add a small circle at center
        center = mpatches.Circle((x, y), radius=marker_size * 0.15,
                                facecolor=bright_red, edgecolor="#000",
                                linewidth=1, zorder=7)
        ax.add_patch(center)
        
        # Add battle label next to the marker (no background or border)
        if battle_name:
            ax.text(x + marker_size * 1.5, y, battle_name, 
                   fontsize=8, color="#8b0000", weight="bold",
                   zorder=8)

# Draw battle markers at exact battle locations with labels
for point in all_points:
    if point.get("battle", False) and "battle_name" in point:
        battle_name = point["battle_name"]
        if HAS_CARTOPY:
            draw_battle_marker(ax1, point["lon"], point["lat"], 
                             battle_name=battle_name, transform=ccrs.PlateCarree())
        else:
            draw_battle_marker(ax1, point["lon"], point["lat"], battle_name=battle_name)

# Set axis limits with some padding
all_lons = advance_lons + retreat_lons
all_lats = advance_lats + retreat_lats
lon_min, lon_max = min(all_lons), max(all_lons)
lat_min, lat_max = min(all_lats), max(all_lats)

# Add padding
lon_padding = (lon_max - lon_min) * 0.15
lat_padding = (lat_max - lat_min) * 0.15

# Calculate plot edges
plot_lon_min = lon_min - lon_padding
plot_lon_max = lon_max + lon_padding
plot_lat_min = lat_min - lat_padding
plot_lat_max = lat_max + lat_padding

# Define the three major rivers with extended paths to plot edges
# 1. Niemen/Neman River (flows from south to north, crossed at Kowno ~24.0°E, 54.9°N)
niemen_river = [
    (24.0, plot_lat_min),  # Start at southern edge
    (23.8, 54.2),
    (23.9, 54.5),
    (24.0, 54.7),
    (24.0, 54.9),  # Kowno crossing point
    (24.1, 55.1),
    (24.2, 55.3),
    (24.3, 55.5),
    (24.4, plot_lat_max),  # Extend to northern edge
]

# 2. Dnieper River (flows from north to south, through the region)
dnieper_river = [
    (30.5, plot_lat_max),  # Start at northern edge
    (30.4, 55.8),
    (30.3, 55.6),
    (30.2, 55.4),
    (30.2, 55.2),  # Near Vitebsk
    (30.3, 55.0),
    (30.5, 54.8),
    (31.0, 54.6),  # Near Smolensk
    (31.5, 54.4),
    (32.0, 54.2),
    (32.5, 54.0),
    (33.0, 53.8),
    (33.2, plot_lat_min),  # Extend to southern edge
]

# 3. Berezina River (flows from north to south, famous crossing at Studenka ~30.0°E, 54.4°N)
berezina_river = [
    (29.5, plot_lat_max),  # Start at northern edge
    (29.4, 55.5),
    (29.3, 55.2),
    (29.2, 54.9),
    (29.3, 54.6),
    (29.5, 54.4),  # Near Studenka crossing
    (29.7, 54.2),
    (29.9, 54.0),
    (30.0, 53.8),
    (30.1, plot_lat_min),  # Extend to southern edge
]

# Add background map
if HAS_CARTOPY:
    # Set map extent
    ax1.set_extent([lon_min - lon_padding, lon_max + lon_padding,
                    lat_min - lat_padding, lat_max + lat_padding],
                   crs=ccrs.PlateCarree())
    
    # Add map features
    ax1.add_feature(cfeature.COASTLINE, linewidth=0.5, alpha=0.5, zorder=0)
    ax1.add_feature(cfeature.BORDERS, linewidth=0.3, alpha=0.4, zorder=0)
    ax1.add_feature(cfeature.LAND, facecolor="#f5f5dc", alpha=0.5, zorder=0)
    ax1.add_feature(cfeature.OCEAN, facecolor="#e6f3ff", alpha=0.5, zorder=0)
    
    # Draw the three major rivers manually (more visible)
    niemen_lons, niemen_lats = zip(*niemen_river)
    dnieper_lons, dnieper_lats = zip(*dnieper_river)
    berezina_lons, berezina_lats = zip(*berezina_river)
    
    ax1.plot(niemen_lons, niemen_lats, color="#4a90e2", linewidth=2.5, 
             alpha=0.7, label="Niemen River", transform=ccrs.PlateCarree(), zorder=1)
    ax1.plot(dnieper_lons, dnieper_lats, color="#4a90e2", linewidth=2.5, 
             alpha=0.7, label="Dnieper River", transform=ccrs.PlateCarree(), zorder=1)
    ax1.plot(berezina_lons, berezina_lats, color="#4a90e2", linewidth=2.5, 
             alpha=0.7, label="Berezina River", transform=ccrs.PlateCarree(), zorder=1)
    
    # Add river labels (no background or border)
    ax1.text(24.2, 54.6, "Niemen", fontsize=9, color="#2c5aa0", 
             weight="bold", transform=ccrs.PlateCarree(), zorder=2)
    ax1.text(31.5, 54.3, "Dnieper", fontsize=9, color="#2c5aa0", 
             weight="bold", transform=ccrs.PlateCarree(), zorder=2)
    ax1.text(29.5, 54.0, "Berezina", fontsize=9, color="#2c5aa0", 
             weight="bold", transform=ccrs.PlateCarree(), zorder=2)
    
    ax1.gridlines(draw_labels=False, linewidth=0.5, alpha=0.3, linestyle="--", zorder=1)
else:
    # Simple background without cartopy
    ax1.set_xlim(lon_min - lon_padding, lon_max + lon_padding)
    ax1.set_ylim(lat_min - lat_padding, lat_max + lat_padding)
    ax1.set_aspect("equal", adjustable="box")
    ax1.set_facecolor("#f5f5dc")  # Light beige background
    
    # Draw the three major rivers manually
    niemen_lons, niemen_lats = zip(*niemen_river)
    dnieper_lons, dnieper_lats = zip(*dnieper_river)
    berezina_lons, berezina_lats = zip(*berezina_river)
    
    ax1.plot(niemen_lons, niemen_lats, color="#4a90e2", linewidth=2.5, 
             alpha=0.7, label="Niemen River", zorder=1)
    ax1.plot(dnieper_lons, dnieper_lats, color="#4a90e2", linewidth=2.5, 
             alpha=0.7, label="Dnieper River", zorder=1)
    ax1.plot(berezina_lons, berezina_lats, color="#4a90e2", linewidth=2.5, 
             alpha=0.7, label="Berezina River", zorder=1)
    
    # Add river labels (no background or border)
    ax1.text(24.2, 54.6, "Niemen", fontsize=9, color="#2c5aa0", 
             weight="bold", zorder=2)
    ax1.text(31.5, 54.3, "Dnieper", fontsize=9, color="#2c5aa0", 
             weight="bold", zorder=2)
    ax1.text(29.5, 54.0, "Berezina", fontsize=9, color="#2c5aa0", 
             weight="bold", zorder=2)
    
    ax1.grid(True, alpha=0.2, linestyle="--", linewidth=0.5, zorder=0)

# Remove axis labels (no lat/lon on axes)
ax1.set_xlabel("", fontsize=14)
ax1.set_ylabel("", fontsize=14)
ax1.set_title(
    "Minard's Map of Napoleon's Russian Campaign, 1812\n"
    "Bar width represents number of soldiers (perpendicular to direction of travel)",
    fontsize=16,
    fontweight="bold",
    pad=20
)

# Add legend
advance_patch = mpatches.Patch(color="#d4a574", label="Advance to Moscow")
retreat_patch = mpatches.Patch(color="#2c3e50", label="Retreat from Moscow")
ax1.legend(handles=[advance_patch, retreat_patch], loc="upper right", fontsize=10)

# Create list of all path points for animation
all_path_points = []
all_path_troops = []
all_path_is_retreat = []

# Add advance path
for i, point in enumerate(advance):
    all_path_points.append((point["lon"], point["lat"]))
    all_path_troops.append(point["troops"])
    all_path_is_retreat.append(False)

# Add retreat path (skip first Moscow point as it's duplicate)
for i, point in enumerate(retreat[1:], start=1):
    all_path_points.append((point["lon"], point["lat"]))
    all_path_troops.append(point["troops"])
    all_path_is_retreat.append(True)

# Napoleon caricature drawing function
def draw_napoleon_caricature(ax, x, y, size=1.0, is_sad=False, transform=None):
    """Draw a simple caricature of Napoleon with bigger head and hat"""
    scale = size * 0.2  # Increased scale for bigger head
    
    # Head (circle) - bigger
    head = mpatches.Circle((x, y), radius=scale * 1.2, 
                          facecolor="#f4d9a6", edgecolor="#8b6f47", 
                          linewidth=2, zorder=10, transform=transform)
    ax.add_patch(head)
    
    # Add little ears
    # Left ear
    left_ear = mpatches.Ellipse((x - scale * 1.0, y), width=scale * 0.25, 
                                height=scale * 0.4, angle=0,
                                facecolor="#f4d9a6", edgecolor="#8b6f47",
                                linewidth=1.5, zorder=9, transform=transform)
    ax.add_patch(left_ear)
    # Right ear
    right_ear = mpatches.Ellipse((x + scale * 1.0, y), width=scale * 0.25, 
                                 height=scale * 0.4, angle=0,
                                 facecolor="#f4d9a6", edgecolor="#8b6f47",
                                 linewidth=1.5, zorder=9, transform=transform)
    ax.add_patch(right_ear)
    
    # Bicorne hat - small semicircle in front, larger semicircle behind
    # Hat thinner in width, taller in height
    head_radius = scale * 1.2
    hat_width = head_radius * 3.2  # Keep width the same
    hat_height = hat_width * 0.65  # Taller (increased from 0.5)
    hat_y = y + scale * 0.6  # Center further up above the eyes
    
    # Larger mid-grey semicircle behind (back of hat) - slightly wider, same height as front
    hat_back_width = hat_width * 1.15  # Slightly wider
    hat_back = mpatches.Arc((x, hat_y), width=hat_back_width, height=hat_height,
                            angle=0, theta1=0, theta2=180,
                            color="#808080", linewidth=0, zorder=11, transform=transform)
    # Fill the back semicircle with mid grey (no border)
    back_points = []
    for angle in np.linspace(0, 180, 50):
        rad = np.radians(angle)
        px = x + (hat_back_width / 2) * np.cos(rad)
        py = hat_y + (hat_height / 2) * np.sin(rad)
        back_points.append((px, py))
    back_points.append((x - hat_back_width / 2, hat_y))  # Close the shape
    back_points.append((x + hat_back_width / 2, hat_y))
    hat_back_fill = Polygon(back_points, closed=True, 
                           facecolor="#808080", edgecolor="#808080", 
                           linewidth=0, zorder=10, transform=transform)
    ax.add_patch(hat_back_fill)
    ax.add_patch(hat_back)
    
    # Smaller darker grey semicircle in front (front of hat) - perfect semicircle, same height
    hat_front_width = hat_width * 0.65  # Smaller width
    hat_front = mpatches.Arc((x, hat_y), width=hat_front_width, height=hat_height,
                             angle=0, theta1=0, theta2=180,
                             color="#404040", linewidth=0, zorder=12, transform=transform)
    # Fill the front semicircle with darker grey (perfect semicircle - half a circle, no border)
    front_points = []
    for angle in np.linspace(0, 180, 50):
        rad = np.radians(angle)
        px = x + (hat_front_width / 2) * np.cos(rad)
        py = hat_y + (hat_height / 2) * np.sin(rad)
        front_points.append((px, py))
    front_points.append((x - hat_front_width / 2, hat_y))  # Close the shape
    front_points.append((x + hat_front_width / 2, hat_y))
    hat_front_fill = Polygon(front_points, closed=True, 
                            facecolor="#404040", edgecolor="#404040", 
                            linewidth=0, zorder=12, transform=transform)
    ax.add_patch(hat_front_fill)
    ax.add_patch(hat_front)
    
    # Add revolutionary cockade (tricolour: blue, white, red) - bigger, on top of hat
    # Structure: Red (largest) -> White (middle, slightly smaller than red, slightly larger than blue) -> Blue (smallest)
    cockade_x = x + hat_width * 0.3  # Position on the right side of hat
    cockade_y = hat_y + hat_height * 0.3  # Position on top of the hat (moved up)
    cockade_size = scale * 0.22  # Base size
    
    # Red circle (bottom, widest) - make bigger
    cockade_red = mpatches.Circle((cockade_x, cockade_y), radius=cockade_size * 1.5,
                                 facecolor="#ff0000", edgecolor="#ff0000",
                                 linewidth=0, zorder=13, transform=transform)
    ax.add_patch(cockade_red)
    # White circle (middle, slightly smaller than red, slightly larger than blue) - make bigger
    cockade_white = mpatches.Circle((cockade_x, cockade_y), radius=cockade_size * 1.3,
                                   facecolor="#ffffff", edgecolor="#ffffff",
                                   linewidth=0, zorder=14, transform=transform)
    ax.add_patch(cockade_white)
    # Blue circle (top, smallest) - keep same size
    cockade_blue = mpatches.Circle((cockade_x, cockade_y), radius=cockade_size * 0.8,
                                  facecolor="#0000ff", edgecolor="#0000ff",
                                  linewidth=0, zorder=15, transform=transform)
    ax.add_patch(cockade_blue)
    
    # Body (coat)
    body = mpatches.Rectangle((x - scale * 0.6, y - scale * 1.5), 
                             width=scale * 1.2, height=scale * 1.8,
                             facecolor="#1a3a5a", edgecolor="#0a2a4a", 
                             linewidth=2, zorder=9, transform=transform)
    ax.add_patch(body)
    
    # Hand in coat (characteristic pose) - or sad semicircle on way back
    hand_x = x - scale * 0.25
    hand_y = y - scale * 0.4
    if is_sad:
        # Sad semicircle instead of hand on way back
        hand = mpatches.Arc((hand_x, hand_y), 
                           width=scale * 0.4, height=scale * 0.2,
                           angle=0, theta1=180, theta2=360,
                           color="#2a1a0a", linewidth=scale * 2.5, zorder=10, transform=transform)
    else:
        # Normal hand on way out
        hand = mpatches.Ellipse((hand_x, hand_y), width=scale * 0.4, 
                               height=scale * 0.5, angle=45,
                               facecolor="#f4d9a6", edgecolor="#8b6f47", 
                               linewidth=1.5, zorder=10, transform=transform)
    ax.add_patch(hand)
    
    # Eyes - change expression if sad (made larger, spaced further apart)
    eye_size = scale * 0.14  # Increased from 0.1
    eye_spacing = scale * 0.35  # Increased spacing (was 0.25)
    if is_sad:
        # Sad eyes - same as happy eyes (circles), larger, further apart
        left_eye = mpatches.Circle((x - eye_spacing, y + scale * 0.15), 
                                  radius=eye_size, facecolor="#000", zorder=12, transform=transform)
        right_eye = mpatches.Circle((x + eye_spacing, y + scale * 0.15), 
                                   radius=eye_size, facecolor="#000", zorder=12, transform=transform)
        ax.add_patch(left_eye)
        ax.add_patch(right_eye)
        # Sad mouth - brown half circle (downward, sad expression)
        mouth = mpatches.Arc((x, y - scale * 0.12), 
                            width=scale * 0.5, height=scale * 0.15,
                            angle=0, theta1=180, theta2=360,
                            color="#2a1a0a", linewidth=scale * 2.5, zorder=12, transform=transform)
        ax.add_patch(mouth)
    else:
        # Happy/neutral eyes - larger, further apart
        left_eye = mpatches.Circle((x - eye_spacing, y + scale * 0.15), 
                                  radius=eye_size, facecolor="#000", zorder=12, transform=transform)
        right_eye = mpatches.Circle((x + eye_spacing, y + scale * 0.15), 
                                   radius=eye_size, facecolor="#000", zorder=12, transform=transform)
        ax.add_patch(left_eye)
        ax.add_patch(right_eye)
        # Smiling mouth - brown half circle
        mouth = mpatches.Arc((x, y - scale * 0.12), 
                            width=scale * 0.5, height=scale * 0.15,
                            angle=0, theta1=0, theta2=180,
                            color="#2a1a0a", linewidth=scale * 2.5, zorder=12, transform=transform)
        ax.add_patch(mouth)
    
    # No moustache (removed as requested)
    
    # Collect all patches for return
    patches = [head, left_ear, right_ear, hat_back_fill, hat_back, hat_front_fill, hat_front, 
               cockade_red, cockade_white, cockade_blue, body, hand, left_eye, right_eye, mouth]
    return patches

# Store Napoleon patches for animation (will be initialized in animation)
napoleon_patches = []
napoleon_at_moscow = False

# Minimal temperature plot
temp_lons = [t["lon"] for t in temperatures]
temp_temps = [t["temp"] for t in temperatures]

ax2.plot(temp_lons, temp_temps, "-", color="#1976d2", linewidth=1.5, markersize=3)
ax2.fill_between(temp_lons, temp_temps, 0, alpha=0.2, color="#1976d2")
ax2.set_xlabel("", fontsize=9)
ax2.set_ylabel("Temp (°C)", fontsize=9)
ax2.tick_params(labelsize=8)
ax2.grid(True, alpha=0.2, linestyle="--", linewidth=0.5)
ax2.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
ax2.set_ylim(-35, 5)

# Adjust layout - move temperature graph closer to map
fig.tight_layout()
fig.subplots_adjust(hspace=0.05)  # Reduce vertical spacing between subplots

# Save static plot
plt.savefig("minard_plot.png", dpi=300, bbox_inches="tight")
print("Static plot saved as minard_plot.png")

# Create animation
print("Creating animation...")

def animate(frame):
    """Animate Napoleon moving along the route"""
    global napoleon_patches, napoleon_at_moscow
    
    # Calculate position along path - slower animation
    total_frames = 400  # Increased from 200 to slow down Napoleon
    progress = min(frame / total_frames, 0.999)  # Cap at 0.999 to avoid index errors
    
    # Find which segment we're on
    num_points = len(all_path_points)
    if num_points < 2:
        return []
    
    segment_idx = int(progress * (num_points - 1))
    segment_idx = min(segment_idx, num_points - 2)
    
    # Interpolate position within segment
    segment_progress = (progress * (num_points - 1)) - segment_idx
    
    # Get start and end points of current segment
    x1, y1 = all_path_points[segment_idx]
    x2, y2 = all_path_points[segment_idx + 1]
    
    # Interpolate position
    napoleon_x = x1 + (x2 - x1) * segment_progress
    napoleon_y = y1 + (y2 - y1) * segment_progress
    
    # Check if we've reached Moscow (end of advance)
    moscow_idx = len(advance) - 1
    if segment_idx >= moscow_idx:
        napoleon_at_moscow = True
    
    # Remove old patches
    for patch in napoleon_patches:
        try:
            if patch in ax1.patches:
                patch.remove()
        except (ValueError, AttributeError):
            pass
    
    # Clear the list
    napoleon_patches = []
    
    # Draw Napoleon at new position with appropriate expression
    if HAS_CARTOPY:
        napoleon_patches = draw_napoleon_caricature(
            ax1, napoleon_x, napoleon_y, size=1.0, 
            is_sad=napoleon_at_moscow, transform=ccrs.PlateCarree()
        )
    else:
        napoleon_patches = draw_napoleon_caricature(
            ax1, napoleon_x, napoleon_y, size=1.0, is_sad=napoleon_at_moscow
        )
    
    return napoleon_patches

# Create animation - slower
anim = FuncAnimation(fig, animate, frames=400, interval=50, blit=False, repeat=True)

# Save animation as GIF
print("Saving animation (this may take a while)...")
try:
    # Try using imageio for better GIF support if available
    try:
        import imageio
        from io import BytesIO
        print("Using imageio for GIF creation...")
        
        # Render frames to a list
        frames = []
        for i in range(400):
            animate(i)
            fig.canvas.draw()
            # Save frame to buffer
            buf = BytesIO()
            fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
            buf.seek(0)
            # Read image using imageio (try v2 API first, fallback to v1)
            try:
                frame = imageio.v2.imread(buf)
            except AttributeError:
                frame = imageio.imread(buf)
            frames.append(frame)
            if (i + 1) % 50 == 0:
                print(f"Rendered {i + 1}/400 frames...")
        
        # Save as animated GIF (try v2 API first, fallback to v1)
        try:
            imageio.v2.mimsave("minard_animation.gif", frames, fps=10, loop=0)
        except AttributeError:
            imageio.mimsave("minard_animation.gif", frames, fps=10, loop=0)
        print("Animation saved as minard_animation.gif using imageio")
    except ImportError:
        # Fallback to pillow writer with explicit frame rendering
        print("imageio not available, using pillow writer...")
        # Use 'pillow' writer for GIF - ensure frames are properly rendered
        from matplotlib.animation import PillowWriter
        writer = PillowWriter(fps=10)
        anim.save("minard_animation.gif", writer=writer, dpi=100)
        print("Animation saved as minard_animation.gif using pillow")
        
except Exception as e:
    print(f"Error saving animation: {e}")
    import traceback
    traceback.print_exc()
    print("\nTrying to show animation in window instead...")
    # Show the plot with animation
    plt.show()
else:
    # If save succeeded, optionally show the plot
    print("Animation saved successfully!")
    print("You can also view it by running: python plot_minard.py")
    # Uncomment the line below if you want to show the plot after saving
    # plt.show()
