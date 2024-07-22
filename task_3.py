import sys

def parse_log_line(line: str) -> dict:
    line = line.strip()
    if not line:
        return {}
    date, time, level, info = line.split(' ', maxsplit=3)
    return {"date": date, "time": time, "level": level, "info": info}

def load_logs(file_path: str) -> list:
    list_of_logs = []
    with open(file_path, 'r') as input_file:
        for line in input_file:
            list_of_logs.append(parse_log_line(line))
    return list_of_logs

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log["level"] == level.upper()]
    return [f"{log['date']} {log['time']} - {log['info']}" for log in filtered_logs]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts

def display_log_counts(counts: dict):
        return [f"{count} : {counts[count]}" for count in counts]


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python main.py <path_to_log_file> [<log_level>]")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        level = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        for count in display_log_counts(counts):
            print(count)
        if len(sys.argv) > 2:
            for filter in filter_logs_by_level(logs, level):
                print(filter)
    except FileNotFoundError:
        print("File was not found")
    except ValueError:
        print("Wrong format of data in file")
    