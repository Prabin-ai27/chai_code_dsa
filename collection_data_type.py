from collections import deque
# Deque: Double-ended queue with O(1) appends/pops on both ends
queue = deque(["task1", "task2"])
queue.appendleft("urgent_task")
print("Deque:", queue)