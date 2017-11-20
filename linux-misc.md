# Linux Command Cheat Sheet

## CRLF :arrow_right: LF

```
dos2unix <input> <output>
```

## Rename many files at once

```
mmv "flux.*" "flux_opa.#1"
```

:notes: don't forget the quotes

## Create PDF poster

```
pdfposter -p a2 <input> <output>
```

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
