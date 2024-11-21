import re
from statistics import mean, stdev

def analyze_metrics_file(filename):
    frequencies = []
    latencies = []
    freq_pattern = r'frequency_hz":(\d+\.\d+)'
    latency_pattern = r'latency_ms":(\d+)'

    try:
        with open(filename, 'r') as file:
            for line in file:
                freq_match = re.search(freq_pattern, line)
                latency_match = re.search(latency_pattern, line)
                if freq_match:
                    frequency = float(freq_match.group(1))
                    frequencies.append(frequency)
                if latency_match:
                    latency = float(latency_match.group(1))
                    latencies.append(latency)
    except FileNotFoundError:
        print(f"Couldn't find file {filename}")
        return None
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")
        return None
    
    if not frequencies or not latencies:
        print("`frequencies` or `latencies` was empty")
        return None
        
    freq_stats = {
        'count': len(frequencies),
        'mean': mean(frequencies),
        'min': min(frequencies),
        'max': max(frequencies),
        'std_dev': stdev(frequencies)
    }
    
    latency_stats = {
        'count': len(latencies),
        'mean': mean(latencies),
        'min': min(latencies),
        'max': max(latencies),
        'std_dev': stdev(latencies)
    }
    
    return freq_stats, latency_stats

def main():
    files = ['feat.txt', 'main.txt']
    print("Analyzing metrics data per file...\n")
    for filename in files:
        result = analyze_metrics_file(filename)
        if result:
            freq_stats, latency_stats = result
            print(f"Statistics for '{filename}':")
            print("  Frequency:")
            print(f"    Num measurements: {freq_stats['count']}")
            print(f"    Average frequency: {freq_stats['mean']:.2f} Hz")
            print(f"    Minimum frequency: {freq_stats['min']:.2f} Hz")
            print(f"    Maximum frequency: {freq_stats['max']:.2f} Hz")
            print(f"    Standard deviation: {freq_stats['std_dev']:.2f} Hz")
            print("  Latency:")
            print(f"    Num measurements: {latency_stats['count']}")
            print(f"    Average latency: {latency_stats['mean']:.2f} ms")
            print(f"    Minimum latency: {latency_stats['min']:.2f} ms")
            print(f"    Maximum latency: {latency_stats['max']:.2f} ms")
            print(f"    Standard deviation: {latency_stats['std_dev']:.2f} ms")
        else:
            print(f"No valid data found for '{filename}'")

if __name__ == "__main__":
    main()
