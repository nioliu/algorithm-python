import statistics

import matplotlib.pyplot as plt


class Process:
    def __init__(self, id, burst_time):
        self.id = id
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.first_time = 0
        self.last_exe_comp_time = 0


def calculate_quantum_time_srrsm(processes):
    return 7


def calculate_quantum_time_brrsm(processes):
    processes.sort(key=lambda p: p.burst_time)
    durations = [p.burst_time for p in processes]
    median = statistics.median(durations)
    avg = statistics.mean(durations)
    return (median + avg) // 2


def calculate_quantum_time_arrsm(processes):
    processes.sort(key=lambda p: p.burst_time)
    if len(processes) % 2 == 0:
        return sum(p.burst_time for p in processes) / len(processes)
    else:
        return processes[len(processes) // 2].burst_time


def calculate_quantum_time_orrsm(processes):
    if len(processes) == 1:
        return processes[0].burst_time
    processes.sort(key=lambda p: p.burst_time)
    return processes[-1].burst_time - processes[0].burst_time


# start processes execution
def round_robin_scheduling(processes, al):
    timeline = []
    first_pro = set()
    time = 0
    switch_context = 0
    res_processes = []

    if not processes:
        return "Ready queue is empty"

    while processes:
        quantum_time = al(processes)

        # statistic all the completed processes
        completed_processes = []

        for i, process in enumerate(processes):
            if process not in first_pro:
                process.first_time = time
                first_pro.add(process)

            switch_context += 1
            process.waiting_time += time - process.last_exe_comp_time  # 等待时间=当前时间减去上一次执行完毕的时间

            execution_time = min(quantum_time, process.burst_time)
            process.burst_time -= execution_time
            timeline.append((process.id, time, time + execution_time))
            time += execution_time

            process.last_exe_comp_time = time + execution_time  # 当前时间+执行任务的时间

            if process.burst_time <= 0:
                # 将完成的进程添加到临时列表中
                process.turnaround_time = process.last_exe_comp_time  # 从到达到完全完成的时间
                completed_processes.append(i)
                res_processes.append(process)

        # 从就绪队列中移除已完成的进程
        for index in reversed(completed_processes):
            processes.pop(index)

    return timeline, switch_context, res_processes, time


# Example usage
process_list = [Process(1, 10), Process(2, 5), Process(3, 8), Process(4, 3), Process(5, 7), Process(6, 6),
                Process(7, 2),
                Process(8, 4), Process(9, 9), Process(10, 50), Process(11, 40)]
# Calculate for each algorithm
algorithms = {
    "SRRSM": calculate_quantum_time_srrsm,
    "ARRSM": calculate_quantum_time_arrsm,
    "BRRSM": calculate_quantum_time_brrsm,
    "ORRSM": calculate_quantum_time_orrsm
}

results = {}

for name, algorithm in algorithms.items():
    processes = [Process(p.id, p.burst_time) for p in process_list]  # Clone processes for each algorithm
    timeline, switch_context_times, res_processes, time = round_robin_scheduling(processes, algorithm)

    # Calculate AWT, ATT, ART
    awt = sum(p.waiting_time for p in res_processes) / len(res_processes)
    att = sum(p.turnaround_time for p in res_processes) / len(res_processes)
    art = sum(p.first_time for p in res_processes) / len(res_processes)

    results[name] = {
        "AWT": awt,
        "ATT": att,
        "ART": art,
        "NCS": switch_context_times,
        "Total Time": time
    }
print(results)

# # Find the maximum time to set the x-axis limit
# max_time = max(end for _, _, end in timeline)
# # Plotting
# fig, ax = plt.subplots()
# for pid, start, end in timeline:
#     duration = end - start
#     ax.broken_barh([(start, duration)], (pid - 0.4, 0.8), facecolors='tab:blue')
#
#     # Adjust text label based on duration
#     if duration >= 5:  # Threshold for displaying label inside the bar
#         mid_point = start + duration / 2
#         ax.text(mid_point, pid, f'P{pid}', ha='center', va='center', color='black', fontsize=8)
#     else:
#         ax.text(end, pid, f'P{pid}', ha='left', va='center', color='black', fontsize=8)
#
# ax.set_xlabel('Time')
# ax.set_ylabel('Process ID')
# ax.set_yticks([p.id for p in processes])
# ax.set_yticklabels([f'P{p.id}' for p in processes])
#
# fig.subplots_adjust(bottom=0.2)
# fig.suptitle('BRRSM Execution Timeline', fontsize=12, y=0.1)
#
# plt.show()
