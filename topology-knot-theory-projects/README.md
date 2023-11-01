# Morphing 3D Shapes: Cube to Sphere

This project demonstrates the transition between a cube and a sphere using a morphing technique. Through an interactive slider, users can adjust the morph level between the two shapes, visualizing each intermediate state.

## Overview

Starting with the 8 vertices of a cube, this script uses a combination of the cube's vertices and those of a sphere to compute the morphed coordinates. The morphing is controlled by a parameter which varies between 0 and 1. 0 represents the cube shape, while 1 represents the sphere shape. Intermediate values provide the various morphed states between the cube and the sphere.

## Visualization

This project uses `plotly.graph_objects` to render the 3D shapes and provides an interactive experience for the user. The interactive slider at the bottom allows the user to see the morphed shape in real-time.

## Usage

1. Ensure you have the necessary libraries installed:
    ```bash
    pip install requirements.txt
    ```

2. Run the script to see the 3D visualization with the interactive morphing slider.

3. Adjust the slider to see the transformation from the cube to the sphere and vice versa.


