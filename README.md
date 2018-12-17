# Finite State Automaton Log Analyzer
This is a simple python program that checks logs from multiple instances in a system, to see if their behavior matches a state table.

# Output
For the sample .log files, this is the output:
```
23.log is stuck on state D. However, this is an accepting state.
24.log is stuck on state C.
25.log is stuck on state C.
Finished:
         23.log finished with state D, line 8
Stuck:
         24.log stuck at state C, line 14
                Bad transition in 24.log at line 8. [C -> A]
         25.log stuck at state C, line 21
                Bad transition in 25.log at line 10. [C -> A]
                Bad transition in 25.log at line 18. [C -> A]
```

