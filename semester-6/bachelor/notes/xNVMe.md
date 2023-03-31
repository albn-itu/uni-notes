---
title: XNVMe
tags: [ library ]
date: 2023-03-29
---

# XNVMe
## Quick notes

- Cross platform library for NVMe and other devices
- Can be used with other devices as you can just switch the driver out. It's primarily intended for NVMe drives though.
- Provides a suite of tools to manage NVMe devices
- Provides I/O interface independence defined as "changing I/O interface does not require refactoring the rest of the system"
- Uniform error handling across interfaces
- Provides a queue for writing async. This also makes it easy to manage synchronous interfaces act like they could be parallel.
- Designed with the goal of minimum performance penalty and minimal complexity increase compared to using the underlying I/O interfaces. At the same time the absolute minimum amount of code should be changed to switch to a different I/O interface, in most cases this is actually only one: the config line.
- Everything is handled through `libxnvme`
