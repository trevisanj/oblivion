# Python tips

## Uninstalling previous versions of packages



```shell 
cd /usr/local/lib/pythonxxxx/dist-packages
sudo rm -rf package-name*
```

If you have local installations, repeat for `/home/j/.local/lib/pythonxxxx`

## When it says that a property does not exist

The getter is possibly raising an exception
