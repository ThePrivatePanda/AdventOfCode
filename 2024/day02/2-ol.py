lines = [list(map(int, line.strip().split())) for line in open('input.txt')]

is_safe_report = lambda levels: (
    (lambda diffs: diffs and all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)))
)([b - a for a, b in zip(levels, levels[1:])])

perfectly_safe_reports = sum(is_safe_report(levels) for levels in lines)

safe_reports = sum(
    1 for levels in lines if is_safe_report(levels) or any(
        is_safe_report(levels[:i] + levels[i+1:]) for i in range(len(levels))
    )
)

print(perfectly_safe_reports)
print(safe_reports)
