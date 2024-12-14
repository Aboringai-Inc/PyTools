def calculate_duration(start_time, end_time):
    """Calculates the duration between two times."""
    return (end_time - start_time).total_seconds()

def transpose_matrix(matrix):
    """Transposes a 2D matrix."""
    return list(map(list, zip(*matrix)))
