def is_safe_report(levels):
    if len(levels) < 2:
        return True  # A sequence with less than 2 levels is considered safe.

    diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]

    # Check for zero differences (no equal adjacent levels allowed)
    if any(diff == 0 for diff in diffs):
        return False

    # Check that all differences are between 1 and 3 inclusive (by absolute value)
    if not all(1 <= abs(diff) <= 3 for diff in diffs):
        return False

    # Determine if the sequence is strictly increasing or decreasing
    is_increasing = all(diff > 0 for diff in diffs)
    is_decreasing = all(diff < 0 for diff in diffs)

    # The levels must be all increasing or all decreasing
    if not (is_increasing or is_decreasing):
        return False

    return True

def main():
    safe_reports = 0
    with open('input.txt', 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_safe_report(levels):
                safe_reports += 1
            else:
                # Try removing one level at a time
                for i in range(len(levels)):
                    new_levels = levels[:i] + levels[i+1:]
                    if is_safe_report(new_levels):
                        safe_reports += 1
                        break  # No need to check further if one removal makes it safe
    print(safe_reports)

if __name__ == "__main__":
    main()
