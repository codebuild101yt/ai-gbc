# Counter.py
def get_output():
    with open('/home/gray/Documents/gbc/ai-gbc/pc/Ai/person_count.txt', 'r') as f:
        person_count = int(f.read().strip())

    Count = person_count
    Seconds = 15
    Output = Seconds - Count
    return Output
