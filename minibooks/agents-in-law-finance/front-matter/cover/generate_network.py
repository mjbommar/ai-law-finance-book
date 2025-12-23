#!/usr/bin/env python3
"""
Generate network graph coordinates for book cover visualization.
Outputs TikZ code that can be included in the cover.

Two networks:
1. Modular "brain-like" network - organic, clustered (foreground)
2. MLP/Transformer-style layered network - structured (background, more transparent)
"""

import networkx as nx
import numpy as np
from pathlib import Path


def create_mlp_network(layer_sizes=[4, 8, 6, 3], connection_prob=0.7, skip_connections=True):
    """
    Create a multi-layer perceptron style network with optional skip connections.

    Args:
        layer_sizes: List of node counts per layer [input, hidden1, hidden2, ..., output]
        connection_prob: Probability of connection between adjacent layer nodes
        skip_connections: Whether to add residual/skip connections

    Returns:
        G: NetworkX graph
        layer_assignments: dict mapping node to layer index
        nodes_by_layer: list of lists of node names per layer
    """
    G = nx.Graph()
    layer_assignments = {}

    node_id = 0
    nodes_by_layer = []

    # Create nodes for each layer
    for layer_idx, size in enumerate(layer_sizes):
        layer_nodes = []
        for i in range(size):
            node_name = f"L{layer_idx}_{i}"
            G.add_node(node_name, layer=layer_idx)
            layer_assignments[node_name] = layer_idx
            layer_nodes.append(node_name)
            node_id += 1
        nodes_by_layer.append(layer_nodes)

    # Connect adjacent layers (feed-forward connections)
    for layer_idx in range(len(layer_sizes) - 1):
        current_layer = nodes_by_layer[layer_idx]
        next_layer = nodes_by_layer[layer_idx + 1]

        for n1 in current_layer:
            for n2 in next_layer:
                if np.random.random() < connection_prob:
                    G.add_edge(n1, n2)

    # Add skip connections (residual connections spanning 2 layers)
    if skip_connections and len(layer_sizes) > 2:
        for layer_idx in range(len(layer_sizes) - 2):
            current_layer = nodes_by_layer[layer_idx]
            skip_layer = nodes_by_layer[layer_idx + 2]

            # Sparse skip connections (15% probability)
            for n1 in current_layer:
                for n2 in skip_layer:
                    if np.random.random() < 0.15:
                        G.add_edge(n1, n2)

    return G, layer_assignments, nodes_by_layer


def compute_mlp_layout(G, layer_assignments, nodes_by_layer, radius=2.0, center_x=4.25, center_y=7.0):
    """
    Compute layout for MLP-style network - nodes arranged in vertical layers.

    Args:
        G: NetworkX graph
        layer_assignments: dict mapping node to layer index
        nodes_by_layer: list of lists of node names per layer
        radius: Radius of containing circle
        center_x, center_y: Center position

    Returns:
        dict: Node positions {node: (x, y)}
    """
    n_layers = len(nodes_by_layer)
    pos = {}

    # Distribute layers horizontally within the circle
    # Leave margin at edges
    usable_width = radius * 1.6  # Slightly less than diameter
    layer_spacing = usable_width / (n_layers - 1) if n_layers > 1 else 0

    for layer_idx, layer_nodes in enumerate(nodes_by_layer):
        # X position for this layer
        x = center_x - usable_width/2 + layer_idx * layer_spacing

        # Distribute nodes vertically within layer
        n_nodes = len(layer_nodes)
        max_height = radius * 1.4  # Vertical span

        if n_nodes > 1:
            node_spacing = max_height / (n_nodes - 1)
            start_y = center_y - max_height/2
        else:
            node_spacing = 0
            start_y = center_y

        for i, node in enumerate(layer_nodes):
            y = start_y + i * node_spacing
            pos[node] = (x, y)

    return pos


def create_large_radial_network(n_rings=8, nodes_per_ring=12, connection_prob=0.3):
    """
    Create a large network arranged in concentric rings (radial layout).

    Args:
        n_rings: Number of concentric rings
        nodes_per_ring: Base number of nodes per ring (varies slightly)
        connection_prob: Probability of connections

    Returns:
        G: NetworkX graph
        ring_assignments: dict mapping node to ring index
    """
    G = nx.Graph()
    ring_assignments = {}
    nodes_by_ring = []

    # Create nodes in concentric rings
    for ring_idx in range(n_rings):
        # Vary nodes per ring - more in outer rings
        n_nodes = nodes_per_ring + ring_idx * 2
        ring_nodes = []

        for i in range(n_nodes):
            node_name = f"R{ring_idx}_{i}"
            G.add_node(node_name, ring=ring_idx)
            ring_assignments[node_name] = ring_idx
            ring_nodes.append(node_name)

        nodes_by_ring.append(ring_nodes)

    # Connect within rings (adjacent nodes)
    for ring_idx, ring_nodes in enumerate(nodes_by_ring):
        n = len(ring_nodes)
        for i in range(n):
            # Connect to next node in ring (circular)
            if np.random.random() < 0.7:
                G.add_edge(ring_nodes[i], ring_nodes[(i + 1) % n])
            # Skip one node occasionally
            if np.random.random() < 0.3:
                G.add_edge(ring_nodes[i], ring_nodes[(i + 2) % n])

    # Connect between adjacent rings (radial connections)
    for ring_idx in range(n_rings - 1):
        inner_ring = nodes_by_ring[ring_idx]
        outer_ring = nodes_by_ring[ring_idx + 1]

        for n1 in inner_ring:
            for n2 in outer_ring:
                if np.random.random() < connection_prob:
                    G.add_edge(n1, n2)

    # Add some long-range skip connections (across 2 rings)
    for ring_idx in range(n_rings - 2):
        inner_ring = nodes_by_ring[ring_idx]
        outer_ring = nodes_by_ring[ring_idx + 2]

        for n1 in inner_ring:
            for n2 in outer_ring:
                if np.random.random() < 0.05:
                    G.add_edge(n1, n2)

    return G, ring_assignments, nodes_by_ring


def compute_radial_layout(G, ring_assignments, nodes_by_ring,
                          center_x=4.25, center_y=6.5,
                          inner_radius=0.5, outer_radius=4.0,
                          spiral_factor=0.3, jitter=0.1):
    """
    Compute radial/spiral layout for the network.

    Args:
        center_x, center_y: Center of the radial layout
        inner_radius: Radius of innermost ring
        outer_radius: Radius of outermost ring
        spiral_factor: How much to spiral (0=concentric circles, 1=strong spiral)
        jitter: Random position jitter
    """
    n_rings = len(nodes_by_ring)
    pos = {}

    # Compute radius for each ring
    if n_rings > 1:
        ring_spacing = (outer_radius - inner_radius) / (n_rings - 1)
    else:
        ring_spacing = 0

    for ring_idx, ring_nodes in enumerate(nodes_by_ring):
        n_nodes = len(ring_nodes)
        radius = inner_radius + ring_idx * ring_spacing

        for i, node in enumerate(ring_nodes):
            # Base angle - distribute evenly around circle
            base_angle = 2 * np.pi * i / n_nodes

            # Add spiral offset based on ring
            spiral_offset = spiral_factor * ring_idx * (2 * np.pi / n_rings)
            angle = base_angle + spiral_offset

            # Add jitter
            angle += np.random.uniform(-jitter, jitter)
            r = radius + np.random.uniform(-jitter, jitter) * ring_spacing * 0.5

            # Convert to cartesian
            x = center_x + r * np.cos(angle)
            y = center_y + r * np.sin(angle)

            pos[node] = (x, y)

    return pos


def generate_radial_tikz(G, pos, ring_assignments, output_path, opacity_scale=0.5):
    """
    Generate TikZ code for radial network.
    """
    lines = []
    lines.append("% Auto-generated radial neural network visualization")
    lines.append("% Do not edit manually - regenerate with generate_network.py")
    lines.append("")

    # Define node coordinates
    lines.append("% Radial network node coordinates")
    for node, (x, y) in pos.items():
        safe_name = node.replace("_", "")
        lines.append(f"\\coordinate ({safe_name}) at ({x:.3f}in, {y:.3f}in);")

    lines.append("")
    lines.append("% Radial network edges")
    edge_opacity = 0.06 * opacity_scale  # 50% more transparent
    lines.append(f"\\begin{{scope}}[EdgeGlow, opacity={edge_opacity:.2f}, line width=0.4pt]")

    for n1, n2 in G.edges():
        safe_n1 = n1.replace("_", "")
        safe_n2 = n2.replace("_", "")
        lines.append(f"  \\draw ({safe_n1}) -- ({safe_n2});")

    lines.append("\\end{scope}")
    lines.append("")

    # Draw nodes - color by ring (inner=warm, outer=cool)
    lines.append("% Radial network nodes")
    n_rings = max(ring_assignments.values()) + 1

    for node, (x, y) in pos.items():
        safe_name = node.replace("_", "")
        ring = ring_assignments[node]

        # Gradient from copper (inner) to blue (outer)
        ring_frac = ring / (n_rings - 1) if n_rings > 1 else 0

        if ring_frac < 0.3:
            color = "CopperGlow"
        elif ring_frac < 0.6:
            color = "CopperLight"
        else:
            color = "EdgeGlow"

        # Smaller nodes for outer rings (depth effect)
        size_factor = 1.0 - ring_frac * 0.4
        outer_size = 5 * size_factor
        inner_size = 2.5 * size_factor
        core_size = 1.2 * size_factor

        outer_op = 0.08 * opacity_scale
        mid_op = 0.25 * opacity_scale
        core_op = 0.7 * opacity_scale

        lines.append(f"  \\fill[{color}, opacity={outer_op:.2f}] ({safe_name}) circle ({outer_size:.1f}pt);")
        lines.append(f"  \\fill[{color}, opacity={mid_op:.2f}] ({safe_name}) circle ({inner_size:.1f}pt);")
        lines.append(f"  \\fill[TextSoft, opacity={core_op:.2f}] ({safe_name}) circle ({core_size:.1f}pt);")

    lines.append("")

    output_path = Path(output_path)
    output_path.write_text("\n".join(lines))
    print(f"Generated {output_path} with {len(G.nodes())} nodes and {len(G.edges())} edges (radial style)")


def compute_mlp_layout_fullpage(G, layer_assignments, nodes_by_layer,
                                 page_width=8.5, page_height=11.0,
                                 x_margin=0.5, y_bottom=2.0, y_top=10.5,
                                 rotation_deg=12, jitter=0.15, curve_amount=0.4):
    """
    Compute layout for MLP-style network with rotation, jitter, and curve.

    Args:
        G: NetworkX graph
        layer_assignments: dict mapping node to layer index
        nodes_by_layer: list of lists of node names per layer
        page_width: Page width in inches
        x_margin: Horizontal margin from edges in inches
        y_bottom: Bottom Y position (above the band)
        y_top: Top Y position (near top of page)
        rotation_deg: Rotation angle in degrees
        jitter: Random position jitter (fraction of spacing)
        curve_amount: How much to curve the layout (0=straight, 1=strong curve)

    Returns:
        dict: Node positions {node: (x, y)}
    """
    n_layers = len(nodes_by_layer)
    pos = {}

    # Center of the layout
    center_x = page_width / 2
    center_y = (y_bottom + y_top) / 2

    # Use full page width minus margins
    usable_width = page_width - 2 * x_margin
    layer_spacing = usable_width / (n_layers - 1) if n_layers > 1 else 0

    # Vertical span
    max_height = y_top - y_bottom

    # Rotation angle in radians
    theta = np.radians(rotation_deg)
    cos_t, sin_t = np.cos(theta), np.sin(theta)

    for layer_idx, layer_nodes in enumerate(nodes_by_layer):
        # Base X position for this layer
        base_x = x_margin + layer_idx * layer_spacing

        # Apply curve - shift Y based on X position (parabolic curve)
        # Layers in the middle are higher/lower
        normalized_x = (layer_idx / (n_layers - 1)) - 0.5  # -0.5 to 0.5
        curve_offset = curve_amount * (1 - 4 * normalized_x * normalized_x) * 1.5  # Inverted parabola

        # Distribute nodes vertically within layer
        n_nodes = len(layer_nodes)

        if n_nodes > 1:
            node_spacing = max_height * 0.85 / (n_nodes - 1)
            start_y = center_y - (max_height * 0.85) / 2
        else:
            node_spacing = 0
            start_y = center_y

        for i, node in enumerate(layer_nodes):
            # Base position
            x = base_x
            y = start_y + i * node_spacing + curve_offset

            # Add jitter
            x += np.random.uniform(-jitter, jitter) * layer_spacing * 0.5
            y += np.random.uniform(-jitter, jitter) * node_spacing * 0.5 if n_nodes > 1 else 0

            # Apply rotation around center
            dx, dy = x - center_x, y - center_y
            rot_x = center_x + dx * cos_t - dy * sin_t
            rot_y = center_y + dx * sin_t + dy * cos_t

            pos[node] = (rot_x, rot_y)

    return pos


def create_modular_network(n_modules=4, nodes_per_module=8, p_intra=0.4, p_inter=0.08):
    """
    Create a modular network with brain-like cluster structure.

    Args:
        n_modules: Number of clusters/modules
        nodes_per_module: Nodes in each module
        p_intra: Probability of edge within module
        p_inter: Probability of edge between modules
    """
    G = nx.Graph()

    # Create modules
    for m in range(n_modules):
        # Add nodes for this module
        module_nodes = [f"m{m}_n{i}" for i in range(nodes_per_module)]
        G.add_nodes_from(module_nodes, module=m)

        # Add intra-module edges (dense connections within cluster)
        for i, n1 in enumerate(module_nodes):
            for n2 in module_nodes[i+1:]:
                if np.random.random() < p_intra:
                    G.add_edge(n1, n2, weight=1.0)

    # Add inter-module edges (sparse connections between clusters)
    modules = list(range(n_modules))
    for m1 in modules:
        for m2 in modules[m1+1:]:
            nodes_m1 = [n for n, d in G.nodes(data=True) if d['module'] == m1]
            nodes_m2 = [n for n, d in G.nodes(data=True) if d['module'] == m2]
            for n1 in nodes_m1:
                for n2 in nodes_m2:
                    if np.random.random() < p_inter:
                        G.add_edge(n1, n2, weight=0.5)

    return G


def compute_layout(G, radius=2.0, center_x=4.25, center_y=7.0):
    """
    Compute 2D layout scaled to fit inside a circle.

    Args:
        G: NetworkX graph
        radius: Radius of the containing circle (inches)
        center_x: X center position on cover (inches)
        center_y: Y center position on cover (inches)

    Returns:
        dict: Node positions {node: (x, y)}
    """
    # Use spring layout with some tuning for organic look
    pos = nx.spring_layout(
        G,
        k=2.0/np.sqrt(len(G.nodes())),  # Optimal distance between nodes
        iterations=100,
        seed=42
    )

    # Normalize to fit within unit circle
    # Find the maximum distance from center
    max_dist = 0
    for (x, y) in pos.values():
        dist = np.sqrt(x**2 + y**2)
        if dist > max_dist:
            max_dist = dist

    # Scale all positions to fit within the target radius
    # Leave a small margin (90% of radius) so nodes don't touch the edge
    scale = (radius * 0.9) / max_dist if max_dist > 0 else 1.0

    scaled_pos = {}
    for node, (x, y) in pos.items():
        scaled_x = center_x + x * scale
        scaled_y = center_y + y * scale
        scaled_pos[node] = (scaled_x, scaled_y)

    return scaled_pos


def generate_tikz(G, pos, output_path):
    """
    Generate TikZ code for the network.

    Args:
        G: NetworkX graph
        pos: Node positions {node: (x, y)}
        output_path: Path to output .tex file
    """
    lines = []
    lines.append("% Auto-generated network visualization")
    lines.append("% Do not edit manually - regenerate with generate_network.py")
    lines.append("")

    # Define node coordinates
    lines.append("% Node coordinates")
    for node, (x, y) in pos.items():
        safe_name = node.replace("_", "")
        lines.append(f"\\coordinate ({safe_name}) at ({x:.3f}in, {y:.3f}in);")

    lines.append("")
    lines.append("% Edges")
    lines.append("\\begin{scope}[EdgeGlow, opacity=0.3, line width=0.8pt]")

    for n1, n2, data in G.edges(data=True):
        safe_n1 = n1.replace("_", "")
        safe_n2 = n2.replace("_", "")
        weight = data.get('weight', 1.0)
        lw = 0.6 + weight * 0.8  # Line width based on weight
        lines.append(f"  \\draw[line width={lw:.1f}pt] ({safe_n1}) -- ({safe_n2});")

    lines.append("\\end{scope}")
    lines.append("")

    # Draw nodes by module (different colors/sizes)
    # Using cover's palette: copper accents + slate blues
    lines.append("% Nodes")
    module_colors = ["CopperGlow", "CopperLight", "EdgeGlow", "CircleLight"]

    for node, (x, y) in pos.items():
        safe_name = node.replace("_", "")
        module = G.nodes[node].get('module', 0)
        color = module_colors[module % len(module_colors)]

        # Multi-layer glow effect
        lines.append(f"  \\fill[{color}, opacity=0.12] ({safe_name}) circle (9pt);")
        lines.append(f"  \\fill[{color}, opacity=0.35] ({safe_name}) circle (5pt);")
        lines.append(f"  \\fill[TextSoft, opacity=0.9] ({safe_name}) circle (2pt);")

    lines.append("")

    # Write output
    output_path = Path(output_path)
    output_path.write_text("\n".join(lines))
    print(f"Generated {output_path} with {len(G.nodes())} nodes and {len(G.edges())} edges")


def generate_mlp_tikz(G, pos, layer_assignments, output_path, opacity_scale=0.5):
    """
    Generate TikZ code for MLP network with reduced opacity for depth effect.

    Args:
        G: NetworkX graph
        pos: Node positions
        layer_assignments: dict mapping node to layer index
        output_path: Path to output .tex file
        opacity_scale: Scale factor for opacity (0.5 = half opacity for "distant" look)
    """
    lines = []
    lines.append("% Auto-generated MLP/neural network visualization (background layer)")
    lines.append("% Do not edit manually - regenerate with generate_network.py")
    lines.append("")

    # Define node coordinates
    lines.append("% MLP Node coordinates")
    for node, (x, y) in pos.items():
        safe_name = node.replace("_", "")
        lines.append(f"\\coordinate ({safe_name}) at ({x:.3f}in, {y:.3f}in);")

    lines.append("")
    lines.append("% MLP Edges - more transparent for depth")
    edge_opacity = 0.15 * opacity_scale
    lines.append(f"\\begin{{scope}}[EdgeGlow, opacity={edge_opacity:.2f}, line width=0.5pt]")

    for n1, n2 in G.edges():
        safe_n1 = n1.replace("_", "")
        safe_n2 = n2.replace("_", "")
        lines.append(f"  \\draw ({safe_n1}) -- ({safe_n2});")

    lines.append("\\end{scope}")
    lines.append("")

    # Draw nodes - using layer-based coloring
    # Input layer: CircleLight, Hidden: EdgeGlow, Output: CopperGlow
    lines.append("% MLP Nodes - reduced opacity for depth effect")
    n_layers = max(layer_assignments.values()) + 1
    layer_colors = ["CircleLight", "EdgeGlow", "EdgeGlow", "CopperGlow"]

    for node, (x, y) in pos.items():
        safe_name = node.replace("_", "")
        layer = layer_assignments[node]

        # Select color based on layer position
        if layer == 0:
            color = "CircleLight"  # Input
        elif layer == n_layers - 1:
            color = "CopperGlow"   # Output
        else:
            color = "EdgeGlow"     # Hidden

        # Reduced opacity glow effect for "distant" appearance
        outer_op = 0.08 * opacity_scale
        mid_op = 0.20 * opacity_scale
        core_op = 0.6 * opacity_scale

        lines.append(f"  \\fill[{color}, opacity={outer_op:.2f}] ({safe_name}) circle (7pt);")
        lines.append(f"  \\fill[{color}, opacity={mid_op:.2f}] ({safe_name}) circle (4pt);")
        lines.append(f"  \\fill[TextSoft, opacity={core_op:.2f}] ({safe_name}) circle (1.5pt);")

    lines.append("")

    # Write output
    output_path = Path(output_path)
    output_path.write_text("\n".join(lines))
    print(f"Generated {output_path} with {len(G.nodes())} nodes and {len(G.edges())} edges (MLP style)")


def main():
    np.random.seed(42)

    # =========================================================================
    # NETWORK 1: Modular "brain-like" network (foreground, in CircleLight)
    # =========================================================================
    G1 = create_modular_network(
        n_modules=4,
        nodes_per_module=6,
        p_intra=0.5,
        p_inter=0.06
    )

    # Fit inside the CircleLight circle
    # Matches: \fill[CircleLight, opacity=0.12] (4.2in, 6.0in) circle (1.8in);
    pos1 = compute_layout(
        G1,
        radius=1.8,
        center_x=4.2,
        center_y=6.0
    )

    output_path1 = Path(__file__).parent / "network-graph.tex"
    generate_tikz(G1, pos1, output_path1)

    # =========================================================================
    # NETWORK 2: Large radial/spiral network (background, brain-like)
    # =========================================================================
    # Concentric rings with spiral twist - looks like neural pathways
    G2, ring_assignments, nodes_by_ring = create_large_radial_network(
        n_rings=14,           # More concentric rings
        nodes_per_ring=18,    # More nodes per ring
        connection_prob=0.20  # Slightly sparser to avoid clutter
    )

    # Radial layout - start further out to avoid center foreground network
    pos2 = compute_radial_layout(
        G2,
        ring_assignments,
        nodes_by_ring,
        center_x=4.25,
        center_y=6.5,
        inner_radius=2.5,     # Start outside the foreground network area
        outer_radius=6.5,     # Wide outer radius
        spiral_factor=0.5,    # Stronger spiral twist
        jitter=0.12
    )

    output_path2 = Path(__file__).parent / "network-mlp.tex"
    generate_radial_tikz(G2, pos2, ring_assignments, output_path2, opacity_scale=0.35)  # More transparent


if __name__ == "__main__":
    main()
