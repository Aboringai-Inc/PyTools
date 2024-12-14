def progress_bar(iterable, prefix="", size=60):
    """Displays a progress bar for an iterable."""
    total = len(iterable)

    def show(j):
        x = int(size * j / total)
        print(f"{prefix}[{'#' * x}{'.' * (size - x)}] {j}/{total}", end="\r")

    for i, item in enumerate(iterable):
        yield item
        show(i + 1)
    print()
