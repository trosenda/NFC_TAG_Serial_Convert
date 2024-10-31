# NFC_TAG_Serial_Convert
Using a couple of Wiegand Readers to read NFC Tags for Access Control.
The Readers output the # in Decimal over Wiegand like "3081086628"
Now adding some custom readers, made of PN532 where the serial is (more close to the standard) being presented as HEX, like "a4:a6:a5:b7"
To update the central DB, but not have a hundred TAGs re-reread I had to understand the logic behind.

Wiegand readers typically present the least significant byte first, while NFC tags store the serial number with the most significant byte first. 
This means you need to reverse the byte order of the hexadecimal serial number.
Developed a Python script that takes a command-line argument and performs either hex to decimal conversion (if the argument contains a colon) or decimal to hex conversion (if it doesn't contain a colon).

```
python3 nfc_serial.py a4:a6:a5:b7
Decimal: 3081086628
```

```
python3 nfc_serial.py 3081086628
Hexadecimal: A4:A6:A5:B7
```

