# Helper functions for projection.

def build_segments(segment_height, rumble_length, dark_strip, light_strip):
    segments = []

    for n in range(400):
        segments.append({
          "index":  n,
          "bottom": {"world": {"z": (n * segment_height)}, "camera": {}, "screen": {}},
          "top":    {"world": {"z": ((n + 1) * segment_height)}, "camera": {}, "screen": {}},
          "colour": dark_strip if (n / rumble_length) % 2 == 0 else light_strip})

    return segments

def find_segment(z, segments, segment_length):
    return segments[(z / segment_length) % len(segments)]
