# Linux Command Cheat Sheet

## Dismember PDF into a series of PNG files

```
pdftoppm input.pdf outputprefix -png
```

## Create timelapse from photos

```
ffmpeg -framerate 12 -pattern_type glob -i "./*.JPG" -s:v 720x540 -c:v libx264 -crf 17 -pix_fmt yuv420p bacha-comedor.mp4

ffmpeg -framerate 7 -pattern_type glob -i "./*.JPG" -s:v 480x320 -c:v libx264 -crf 17 -pix_fmt yuv420p my-timelapse.mp4
```

## Bluetooth: annoying "obex 0x53" error

```
systemctl --user start obex
sudo systemctl --global enable obex
```

## USB mount point

```/run/user/1000/gvfs```[...]

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

## Convert Markdown to ...

First:

```
sudo apt-get install pandoc texlive-latex-base lmodern texlive-fonts-recommended
```


Then:

```
pandoc MANUAL.md -o example13.pdf
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
