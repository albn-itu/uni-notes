# 1
## 1.1
```bash
mkdir /tmp/missing
```

## 1.2
```bash
man touch
```

## 1.3
```bash
touch /tmp/missing/semester
```

## 1.4
```bash
echo '#!/bin/sh' > /tmp/missing/semester
echo 'xeyes' >> /tmp/missing/semester
```

## 1.5
```
It wont work because the file is not executable. We can use the interpreter directly to run the file.
```

## 1.6
```bash
sh /tmp/missing/semester
```

## 1.7
```bash
man chmod
```

## 1.8
```bash
chmod u+x /tmp/missing/semster
```

# 2
## 2.1
`a` stands for all, `h` stands for human readable, `--color` stands for color, `l` stands for long listing format.
To sort by recency, we can use `ls -t` or `ls -tr` to reverse the order. Or to be explicit `ls --sort=time`

```bash
ls -alht --color
```

## 2.2
```bash
ls -alht | tee ~/last-modified.txt
ls -alht > ~/last-modified.txt
```

# 3
## 3.1
```bash
mkdir -p answers/number{1,2/number{2.1,2.2},3/number{3.1/number{3.1.1,3.1.2},3.2,3.3}}
```

## 3.2
```bash
cd /tmp/missing
touch file1.txt file2.txt file3.txt file4.txt
cp file*.txt /tmp/missing/answers/number3/number3.1/number3.1.1/
```

## 3.3
```bash
cd /tmp/missing/answers/number3/number3.1/number3.1.1/
nano file1.txt
```

## 3.4
```bash
