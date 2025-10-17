#  Heap Using Priority Queues Jobs and Interrupts

import heapq as hq, time

jobs = [(2,'task_1'), (5,'task_2'), (1,'task_4'),
        (4,'task_5'), (3,'task_3'), (1,'task_8')]
intr = [(1,'intr_1'), (2,'intr_2'), (13,'intr_3')]
hq.heapify(jobs)
print(jobs, "\n\n")

j = 0
while jobs:
    print("The", jobs[0][1], "with priority", jobs[0][0], "in progress", end="")
    for _ in range(5):
        print(".", end=""); time.sleep(0.5)
    hq.heappop(jobs)
    if j < len(intr):
        hq.heappush(jobs, intr[j])
        print("\n\nNew interrupt arrived!!", intr[j], "\n")
        j += 1
    print("\nJob queue currently:", jobs, "\n")

print("\nAll interrupts and jobs completed!")
