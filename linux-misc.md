# Linux Command Cheat Sheet

## Dismember PDF into a series of PNG files

```
pdftoppm input.pdf outputprefix -png
```

## Create PDF from a series of PNG files

```
convert ... output.pdf
```

## Compress PDF file

Using Ghostscript.

```
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
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

Here are two ways. The new way is to replace the other one, which didn't work for me today (20211119).

### New way

This is a very interesting way: instead of specifying the page size, one specifies how many times to split "x-wise" and
"y-wise".

```
mutool poster -x 2 -y 2 borderline0.pdf borderline0-x2-y2.pdf
```

### Not working as of 20211119
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

## List processes

Of certain user:

```
ps -u username
```

Showing command line:

```
ps -c
```
