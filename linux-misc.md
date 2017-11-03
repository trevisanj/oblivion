# Linux Miscellanea

## Change time

1. Change system time:

```
sudo date +%T -s "16:10"
```

2. Write to hardware clock:

```
sudo hwclock --systohc
```

(source: https://www.cyberciti.biz/faq/howto-set-date-time-from-linux-command-prompt/)

## Size of directory

```
du -sh directoryname
```
