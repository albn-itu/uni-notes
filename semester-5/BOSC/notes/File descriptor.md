---
title: File descriptor
tags: [ term, data ]
---

See also: [[File]]

# File descriptor
A file descriptor is the name of a file, such as `ex1.c`, `File descriptor.md` or `nvim`.

A file descriptor usually consists of 2 parts a name and its suffix. The suffix is known as the file extension. The full file name is there to let humans know what the file contains, and to provide and identifier for the [[Operating system]].

## File extension
File extensions are parts of the file descriptor that descripe what type of file we are dealing with. It exists to make life easier for us as humans, as we know what to expect, and for [[Operating system]]s to know what application should deal with the file when opening it. As it's just part of the name, it can be changed to something completely wrong, which will confuse everyone. Fx a `hello.exe` file could be called `hello.txt` which would make windows open it with notepad, which usually ends with it just showing random garbage.

Examples of file extensions:
- .pdf being opened by Acrobat Reader or Zathura
- .xlsx being opened by Excel or LibreOffice Calc
- .c or .h being opened by a code editor, such as NVIM or Visual Studio (Code)
