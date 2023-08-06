# Python stuff that I keep forgetting

## Snippets

### Set matplotlib's "Save the figure" path

```
import matplotlib.pyplot as plt, os
plt.rcParams["savefig.directory"] = os.getcwd()
```

### Setting 

## Operational

### Uninstalling previous versions of packages

```shell 
cd /usr/local/lib/pythonxxxx/dist-packages
sudo rm -rf package-name*
```

If you have local installations, repeat for `/home/j/.local/lib/pythonxxxx`

### When it says that a property does not exist

The getter is possibly raising an exception
