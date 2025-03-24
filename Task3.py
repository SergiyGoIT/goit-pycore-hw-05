import sys
from typing import List, Dict

def parse_log_line(line: str) -> Dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[Dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count:<8}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task3.py <path_to_log_file> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
