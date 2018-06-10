Python 3.6.4 |Anaconda custom (64-bit)| (default, Dec 21 2017, 21:42:08) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0b1011010
90
>>> ord('Z')
90
>>> chr(90)
'Z'
>>> exit()


========================================================================================


Python 3.6.4 |Anaconda custom (64-bit)| (default, Dec 21 2017, 21:42:08) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
>>> utf_string = '文言'
>>> raw_bytes.decode()
'文言'
>>> utf_string.encode()
b'\xe6\x96\x87\xe8\xa8\x80'
>>> raw_bytes == utf_string.encode()
True
>>> utf_string == raw_bytes.decode()
True
>>> quit()


========================================================================================


**utf-8* -> *Unicode Transformation Format 8 Bits*
