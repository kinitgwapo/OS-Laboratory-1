# OS-Laboratory-1
Operating Systems Laboratory 1 - Process Management

## Part E:

### Python Version: 3.14.2

## Part F:

### PID: 18362

1. Why does the operating system assign a PID to every process?
    - So that every process has an identifier, especially when you need to debug a process that is causing an issue to your platform and there are a ton of processes running simultaneously. It can also help coding be much easier to deal with because you use numbers instead of characters.

## Part G:

| Information | Observation           |
| :---------: | :-------------------: |
| PID         | 25234                 |
| CPU %       | 0.0%                  |
| Memory %    | 0.1%                  |
| User        | codespa+ (codespace)  |
| Command     | python process_lab.py |

## Part H:

How does the grep command help us locate a specific process? The grep command basically filters out the processes instead of being shown the entire processes from the “ps aux” command. It shows the grep and the process of the specified program or file you attached to the “ps aux | grep” command.

## Part I:

|                    |        |
| :----------------: | :----: |
| PID                | 16741  |
| CPU Utilization    | 0.0%   |
| Memory Utilization | 0.1%   |
| Process State      | S      |
| Process name       | python |

## Part K:

Information such as Process ID (PID), Process State, %mem usage, %cpu usage from ps and top can be associated with the information maintained by the operating system in the Process Control Block (PCB).

## Part L:

| Process   | PID   | State | CPU % |
| :-------- | :---- | :---- | :---- |
| Process 1 | 29585 | S+    | 0.0%  |
| Process 2 | 29656 | S+    | 0.2%  |
| Process 3 | 29682 | S+    | 0.0%  |

1. Are the PIDs the same?
    - No, because every Process Identifier is unique to a process.

2. Why are the PIDs different?
    - PIDs are different so that whenever you need to find a specific process, no matter if the processes are all the same program but are different instances, you can accurately navigate the specific process instance and do whatever you want with it.

3. Are the three processes running the same program?
    - They are the same program because the program is run three times, but they are split into three different processes with the same logic, just different PIDs.

4. Can one program create multiple processes?
    - Yes, because a program might create a child process which happens to have what the program needs from that program, leading to a program creating multiple different processes.

5. Who manages these processes?
    - The operating system, storing process information in Process Control Block, and task scheduler which relates to the context switching.

## Images:

### Github Repository:

<img width="1242" height="756" alt="image" src="https://github.com/user-attachments/assets/f045a95d-2243-4235-8225-711c8d6909b7" />

### Github Codespaces environment & Python source code

<img width="1873" height="929" alt="image" src="https://github.com/user-attachments/assets/104d31c4-b1b2-4cb1-b1c6-3256d8a48c3e" />

### Program execution showing PID

<img width="530" height="481" alt="image" src="https://github.com/user-attachments/assets/92528753-fc26-46f7-be77-a95b0bd3504a" />

### ps aux output

<img width="640" height="657" alt="image" src="https://github.com/user-attachments/assets/ac1de226-e21b-4fa9-864d-e73ef68c2230" />

### ps -o pid,stat,cmd output

<img width="518" height="98" alt="image" src="https://github.com/user-attachments/assets/1ee76408-803a-4f75-99a8-9f0c16b93b07" />

### top output

<img width="621" height="724" alt="image" src="https://github.com/user-attachments/assets/b9978c37-a337-4bf6-84d7-1d2e778cb490" />

### Multiple instances of process_lab.py

<img width="696" height="87" alt="image" src="https://github.com/user-attachments/assets/bdf5b8d3-dc13-4e90-8939-5ad85079878a" />
