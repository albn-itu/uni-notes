# IFC
```
Step 1:
l = h;

Step 2:
l = false;
if (h) x = true; else skip;
if (x) l = true; else skip;

Step 3:
hatch = h;
l = declassify(hatch);

Step 4:
let (x = h) in { l = x; }
```
