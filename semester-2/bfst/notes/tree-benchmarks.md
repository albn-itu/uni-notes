Tree benchmarks

## File loading times
| Loading times | Time    |
| ------------- | ------- |
| 10            | 5ms     |
| 100           | 5ms     |
| 1k            | 11ms    |
| 10k           | 31ms    |
| 100k          | 71ms    |
| 1M            | 286ms   |
| 10M           | 2328ms  |
| 100M          | 22355ms |


## Tree building times (file loading not included)
| Tree type     | 10   | 100  | 1k   | 10k  | 100k  | 1M     |
| ------------- | ---- | ---- | ---- | ---- | ----- | ------ |
| R*-tree - nodes (4,8) | 11ms | 1ms | 8ms | 43ms | 1282ms | DNF |
| R*-tree - squares (4,8) | 1ms | 1ms | 6ms | 18ms | 1390ms | DNF |
| R*-tree - nodes (250) | 7ms  | 1ms  | 1ms  | 11ms | 75ms   | 1108ms |
| R*-tree - squares (250) | 0ms  | 0ms  | 0ms  | 10ms | 73ms   | 1094ms |
| R*-tree - nodes (500) | 1ms | 1ms | 3ms | 11ms | 126ms | 1201ms |
| R*-tree - squares (500) | 0ms | 0ms | 1ms | 13ms | 94ms | 1162ms |
| R*-tree - nodes (1k)  | 11ms | 1ms | 3ms | 19ms | 107ms | 905ms |
| R*-tree - squares (1k)  | 0ms | 1ms | 1ms | 15ms | 98ms | 899ms |
| KD-tree       | 4ms  | 5ms  | 7ms  | 64ms | 185ms | 1362ms |

## Query times (file loading and building not included)
### KD-tree
| Dataset | 10   | 100  | 1k   | 10k   |
| ------- | ---- | ---- | ---- | ----- |
| 10      | 2ms  | 1ms  | 5ms  | 5ms   |
| 100     | 0ms  | 0ms  | 5ms  | 5ms   |
| 1k      | 0ms  | 0ms  | 1ms  | 11ms  |
| 10k     | 0ms  | 1ms  | 4ms  | 31ms  |
| 100k    | 1ms  | 1ms  | 10ms | 97ms  |
| 1M      | 1ms  | 3ms  | 35ms | 220ms |

### R*-tree (4,8)
| Type | Dataset | 10   | 100  | 1k   | 10k  |
| ---- | ------- | ---- | ---- | ---- | ---- |
| Node | 10      | 3ms | 1ns | 2ms | 10ms |
| Node | 100     | 1ms | 0ms | 1ms | 5ms |
| Node | 1k      | 0ms | 0ms | 0ms | 4ms |
| Node | 10k     | 0ms | 0ms | 0ms | 3ms |
| Node | 100k    | 0ms | 0ms | 0ms | 2ms |
| Node | 1M      | DNF | DNF | DNF | DNF |
| Square | 10      | 2ms | 1ms | 2ms | 18ms |
| Square | 100     | 0ms | 2ms | 10ms | 67ms |
| Square | 1k      | 1ms | 17ms | 62ms | 532ms |
| Square | 10k     | 10ms | 169ms | 704ms | 6365ms |
| Square | 100k    | 134ms | 938ms | 9199ms | 94902ms |
| Square | 1M      | DNF | DNF | DNF | DNF |

### R*-tree (250)
| Type | Dataset | 10   | 100  | 1k   | 10k  |
| ---- | ------- | ---- | ---- | ---- | ---- |
| Node | 10      | 5ms    | 2ms    | 4ms    | 10ms    |
| Node | 100     | 1ms    | 1ms    | 7ms    | 38ms    |
| Node | 1k      | 0ms    | 0ms    | 0ms    | 2ms     |
| Node | 10k     | 0ms    | 0ms    | 1ms    | 9ms     |
| Node | 100k    | 0ms    | 0ms    | 0ms    | 2ms     |
| Node | 1M      | 0ms    | 0ms    | 1ms    | 11ms    |
| Square | 10      | 1ms    | 0ms    | 2ms    | 8ms     |
| Square | 100     | 0ms    | 0ms    | 5ms    | 36ms    |
| Square | 1k      | 0ms    | 5ms    | 35ms   | 311ms   |
| Square | 10k     | 6ms    | 37ms   | 396ms  | 3031ms  |
| Square | 100k    | 103ms  | 549ms  | 5106ms | 50740ms |
| Square | 1M      | 1478ms | 9470ms | DNF    | DNF     |

### R*-tree (500)
| Type | Dataset | 10   | 100  | 1k   | 10k  |
| ---- | ------- | ---- | ---- | ---- | ---- |
| Node | 10      | 2ms | 2ms | 4ms | 15ms |
| Node | 100     | 1ms | 1ms | 5ms | 53ms |
| Node | 1k      | 0ms | 0ms | 1ms | 3ms |
| Node | 10k     | 0ms | 1ms | 1ms | 6ms |
| Node | 100k    | 0ms | 1ms | 6ms | 80ms |
| Node | 1M      | 0ms | 0ms | 1ms | 16ms |
| Square | 10      | 1ms | 2ms | 2ms | 11ms |
| Square | 100     | 1ms | 1ms | 10ms | 44ms |
| Square | 1k      | 2ms | 8ms | 51ms | 323ms |
| Square | 10k     | 10ms | 42ms | 375ms | 3637ms |
| Square | 100k    | 178ms | 1285ms | 12036ms | 1117439ms |
| Square | 1M      | 1938ms | 18334ms | DNF | DNF |

### R*-tree (1k)
| Type | Dataset | 10   | 100  | 1k   | 10k  |
| ---- | ------- | ---- | ---- | ---- | ---- |
| Node | 10      | 7ms | 4ms | 5ms | 16ms |
| Node | 100     | 1ms | 0ms | 6ms | 46ms |
| Node | 1k      | 0ms | 2ms | 21ms | 211ms |
| Node | 10k     | 0ms | 0ms | 1ms | 4ms |
| Node | 100k    | 0ms | 0ms | 3ms | 40ms |
| Node | 1M      | 1ms | 4ms | 32ms | 325ms |
| Square | 10      | 1ms | 2ms | 2ms | 10ms |
| Square | 100     | 0ms | 1ms | 7ms | 44ms |
| Square | 1k      | 2ms | 7ms | 47ms | 450ms |
| Square | 10k     | 12ms | 81ms | 422ms | 4558ms |
| Square | 100k    | 90ms | 726ms | 5901ms | 49548ms |
| Square | 1M      | 2066ms | 14915ms | DNF | DNF |