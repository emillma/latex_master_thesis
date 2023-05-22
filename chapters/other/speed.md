```
nvidia@gjest-10-53-58-89:/mnt/tmpmount/home$ sudo hdparm -Ttv /dev/mmcblk0

/dev/mmcblk0:
 HDIO_DRIVE_CMD(identify) failed: Invalid argument
 readonly      =  0 (off)
 readahead     = 4096 (on)
 HDIO_DRIVE_CMD(identify) failed: Invalid argument
 geometry      = 954368/4/16, sectors = 61079552, start = 0
 Timing cached reads:   9854 MB in  1.97 seconds = 5003.30 MB/sec
 HDIO_DRIVE_CMD(identify) failed: Invalid argument
 Timing buffered disk reads: 856 MB in  3.01 seconds = 284.68 MB/sec
 ```
 ```
 nvidia@gjest-10-53-58-89:/mnt/tmpmount/home$ sudo hdparm -Ttv /dev/nvme0n1

/dev/nvme0n1:
 HDIO_DRIVE_CMD(identify) failed: Inappropriate ioctl for device
 readonly      =  0 (off)
 readahead     = 256 (on)
 HDIO_DRIVE_CMD(identify) failed: Inappropriate ioctl for device
 geometry      = 488386/64/32, sectors = 1000215216, start = 0
 Timing cached reads:   11054 MB in  1.97 seconds = 5621.85 MB/sec
 HDIO_DRIVE_CMD(identify) failed: Inappropriate ioctl for device
 Timing buffered disk reads: 3040 MB in  3.00 seconds = 1012.84 MB/sec
 ```

 ```
nvidia@gjest-10-53-58-89:/mnt/tmpmount/home$ sudo dd if=/dev/zero of=./testfile bs=8k count=100k
102400+0 records in
102400+0 records out
838860800 bytes (839 MB, 800 MiB) copied, 3.31799 s, 253 MB/s
```
```
nvidia@gjest-10-53-58-89:/mnt/tmpmount/home$ sudo dd if=/dev/zero of=./testfile bs=8k count=100k conv=fdatasync
102400+0 records in
102400+0 records out
838860800 bytes (839 MB, 800 MiB) copied, 10.588 s, 79.2 MB/s
```

```
nvidia@gjest-10-53-58-89:/home$ sudo dd if=/dev/zero of=./testfile bs=8k count=100k
102400+0 records in
102400+0 records out
838860800 bytes (839 MB, 800 MiB) copied, 2.92271 s, 255 MB/s
```
```
nvidia@gjest-10-53-58-89:/home$ sudo dd if=/dev/zero of=./testfile bs=8k count=100k conv=fdatasync
102400+0 records in
102400+0 records out
838860800 bytes (839 MB, 800 MiB) copied, 3.38935 s, 250 MB/s
```