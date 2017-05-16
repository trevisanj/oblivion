# USB stick shows only 2 MB

This is a fix to be performed in Windows. It uses the command-line tool `diskpart`

```shell
diskpart
```

Will open another window

```
DISKPART> list disk

Disk ### Status Size Free Dyn Gpt
-------- ------------- ------- ------- --- ---
Disk 0 Online 298 GB 0 B
Disk 1 Online 7509 MB 6619 MB

DISKPART> select disk 1

Disk 1 is now the selected disk.

DISKPART> clean

DiskPart succeeded in cleaning the disk.

DISKPART> create partition primary

DiskPart succeeded in creating the specified partition.

DISKPART> exit
```

The above was copied from http://www.tomshardware.com/answers/id-2085142/fix-usb-pen-drive-16gb-shows.html
