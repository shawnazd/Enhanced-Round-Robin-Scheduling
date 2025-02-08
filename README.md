

# Enhanced Round Robin Scheduling Algorithm 🚀

This repository contains an implementation of the **Enhanced Round Robin Scheduling Algorithm** in Python. The algorithm dynamically adjusts the time quantum for each process based on its remaining burst time.

## Features ✨
- **Dynamic Time Quantum**: Adjusts time quantum based on the remaining burst time.
- **Performance Metrics**: Computes:
  - Average Turnaround Time (TT)
  - Average Waiting Time (WT)
  - Average Response Time (RT).
- **Efficient Process Scheduling**: Ensures fair CPU allocation.

---

## 📌 How It Works  

1️⃣ **Input Process Details**  
   - Enter the number of processes.  
   - Provide **arrival time (AT)** and **burst time (BT)** for each process.  
   - Set the **initial time quantum** for scheduling.  

2️⃣ **Scheduling Execution**  
   - Processes are added to the queue based on arrival time.  
   - Each process executes for a dynamically calculated time quantum.  
   - If unfinished, the process re-enters the queue.  

3️⃣ **Output Results**  
   - The program calculates and displays:  
     ✅ Average **Turnaround Time (TT)**  
     ✅ Average **Waiting Time (WT)**  
     ✅ Average **Response Time (RT)**  

---

## 📥 Example Usage  

### ✅ **Input Example:**
The program will prompt you to enter the number of processes, arrival time, burst time, and the initial time quantum. Here's an example:

```
Enter the number of processes: 5
Enter arrival time for process 1: 1
Enter burst time for process 1: 2
Enter arrival time for process 2: 3
Enter burst time for process 2: 4
Enter arrival time for process 3: 5
Enter burst time for process 3: 6
Enter arrival time for process 4: 7
Enter burst time for process 4: 8
Enter arrival time for process 5: 9
Enter burst time for process 5: 10
Enter the initial time quantum: 3
```

---

### 📤 **Output Example:**
After entering the input, the program will compute and display the following:

```
Enhanced RR Metrics:
Average Turnaround Time: 6.8000
Average Waiting Time: 2.4000
Average Response Time: 0.8000
```

---

### 📊 **Detailed Process Table**  

| Process ID (PID) | Arrival Time (AT) | Burst Time (BT) | Completion Time (CT) | Turnaround Time (TT) | Waiting Time (WT) | Response Time (RT) |
|------------------|-------------------|-----------------|----------------------|----------------------|-------------------|--------------------|
| 1                | 1                 | 2               | 3                    | 2                    | 0                 | 0                  |
| 2                | 3                 | 4               | 9                    | 6                    | 2                 | 2                  |
| 3                | 5                 | 6               | 15                   | 10                   | 4                 | 4                  |
| 4                | 7                 | 8               | 22                   | 15                   | 7                 | 6                  |
| 5                | 9                 | 10              | 32                   | 23                   | 13                | 7                  |

---


## 💡 Why Use Enhanced Round Robin?  

- **Optimized Scheduling**: Reduces process starvation.  
- **Fair CPU Distribution**: Ensures equal execution chances.  
- **Better Performance**: Reduces waiting time.  

---

💻 **Happy Coding!** 😎✨
```
