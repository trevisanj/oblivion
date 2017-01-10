# Notes on how to operate a magnetic tape device (Linux)

## Find out which package to install

```shell
cd /usr/ports
make search key=mt
```

## Prof. BLB's instructions

Possible device names: /dev/tape/tape0 or tape0_d4, tape0c, tape0_d0, tape0_d7

Shell commands:

```shell
mt -f /dev/tape0 rewind
mt -f /dev/tape0 fsf 1  # it was necessary to skip the end-of-file
mt -f /dev/tape0 offline
```

Also:

```
vrestore -i (fita - disco)
```

Tar commands:

```shell
tar  xvf /dev/tape0 
tar tvf /dev/tape0 para listar
```

## Bit of reference on `mt`

```
mt -f [device]
offline: Rewind the tape and, if applicable, unload the tape
fsf: Forward space count files.  The tape is positioned on the first block of the next file.
```


## Notes from website

(http://www.cyberciti.biz/faq/linux-tape-backup-with-mt-and-tar-command-howto/)

Rewind tape drive:

```shell
mt -f /dev/st0 rewind
```

Backup directory /www and /home with tar command (z – compressed):

```shell
tar -czf /dev/st0 /www /home
```

Find out what block you are at with mt command:

```shell
mt -f /dev/st0 tell
```

Display list of files on tape drive:

```shell
tar -tzf /dev/st0
```

Restore /www directory:

```shell
cd /
mt -f /dev/st0 rewind
tar -xzf /dev/st0 www
```

Unload the tape:

```shell
mt -f /dev/st0 offline
```

Display status information about the tape unit:

```shell
mt -f /dev/st0 status
```

Erase the tape:

```shell
mt -f /dev/st0 erase
```

You can go BACKWARD or FORWARD on tape with mt command itself:

**(a)** Go to end of data:
```shell
mt -f /dev/nst0 eod
```

**(b)** Goto previous record:
```shell
mt -f /dev/nst0 bsfm 1
```

**(c)** Forward record:
```shell
mt -f /dev/nst0 fsf 1
```
