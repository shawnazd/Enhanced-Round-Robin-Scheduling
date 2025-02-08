class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1


def calculate_time_quantum(process, initial_quantum):
    # Dynamic adjustment of time quantum based on remaining burst time
    return max(2, min(initial_quantum, process.remaining_time // 2))


def enhanced_rr(processes, initial_time_quantum):
    time = 0
    completed_processes = 0
    n = len(processes)

    total_turnaround_time = 0
    total_waiting_time = 0
    total_response_time = 0

    queue = []

    while completed_processes < n:
        # Add processes to the queue that have arrived by the current time
        for p in processes:
            if p.arrival_time <= time and p.remaining_time > 0:
                queue.append(p)

        if not queue:
            time += 1
            continue

        current_process = queue.pop(0)

        # Update response time if it's the first time the process is being executed
        if current_process.response_time == -1:
            current_process.response_time = time - current_process.arrival_time

        # Calculate the time quantum dynamically based on remaining burst time
        time_quantum = calculate_time_quantum(current_process, initial_time_quantum)

        # Execute the process for the calculated time quantum or until it finishes
        execution_time = min(current_process.remaining_time, time_quantum)
        time += execution_time
        current_process.remaining_time -= execution_time

        # If the process has finished, calculate turnaround and waiting times
        if current_process.remaining_time == 0:
            completed_processes += 1
            current_process.turnaround_time = time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time

            total_turnaround_time += current_process.turnaround_time
            total_waiting_time += current_process.waiting_time
            total_response_time += current_process.response_time
        else:
            # If not finished, push it back to the queue
            queue.append(current_process)

    # Calculate average metrics
    print("\nEnhanced RR Metrics:")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.4f}")
    print(f"Average Waiting Time: {total_waiting_time / n:.4f}")
    print(f"Average Response Time: {total_response_time / n:.4f}")


def take_input():
    processes = []
    num_processes = int(input("Enter the number of processes: "))

    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append(Process(i + 1, arrival_time, burst_time))

    initial_time_quantum = int(input("Enter the initial time quantum: "))
    
    return processes, initial_time_quantum


if __name__ == "__main__":
    # Take input for processes and initial time quantum
    processes, initial_time_quantum = take_input()

    # Run the enhanced round robin scheduling
    enhanced_rr(processes, initial_time_quantum)
