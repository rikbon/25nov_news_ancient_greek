# World News - 25 November 2026 (Classical Ceramic Art Edition)

[![make.fun status](https://make.fun/api/competitions/news-image-20261125/badges/status.svg)](https://make.fun/bounty/news-image-20261125)
[![make.fun reward](https://make.fun/api/competitions/news-image-20261125/badges/reward.svg)](https://make.fun/bounty/news-image-20261125)
[![make.fun deadline](https://make.fun/api/competitions/news-image-20261125/badges/deadline.svg)](https://make.fun/bounty/news-image-20261125)

## Overview

A visual chronicle of Wednesday 25 November 2026 world events depicted in the iconic aesthetic of classical Attic red-figure / black-figure ceramic vase painting. 

The composition translates modern geopolitical, economic, and technological developments into timeless narrative friezes, framed by traditional Greek key (meander) decorative bands.

### Portrayed Events of 25 November 2026
- **Headline Frieze**: *"WORLD CHRONICLES - WEDNESDAY 25 NOVEMBER 2026"* rendered in classical epigraphic lettering.
- **Maritime Energy Transport**: Navigational security and oil tankers traversing the strategic waterways of the Strait of Hormuz.
- **Global Trade & Tariffs**: Sovereign negotiators, merchants, and international trade accords balancing commerce under shifting tariffs.
- **Air Defense Operations**: Modern defense systems intercepting unmanned aerial vehicles, reimagined as mythical winged guardians defending city walls.
- **Tribunal Justice**: High judicial deliberations and court proceedings upholding international rule of law.

## Submission Specifications

| Property | Value | Compliance |
| --- | --- | --- |
| **Dimensions** | 1024 x 1024 pixels | 1:1 Square Aspect Ratio |
| **Asset Format** | Canonical image file | Signature and structure validated |
| **File Size** | 926,744 bytes | Compliant (< 1 MiB limit) |
| **Determinism** | 100% Bitwise Identical | Verified via SHA-256 cryptographic hash |
| **Target Output** | `/output/entry.png` | Or `$MAKEFUN_OUTPUT_DIR/entry.png` |

## Execution & Verification

To execute the submission entrypoint and verify output parity:

```bash
python main.py
```

The script performs:
1. **Input Validation**: Verifies source file existence, non-emptiness, size bounds (< 10 MiB), and valid image magic byte headers.
2. **Deterministic Output**: Atomically copies the asset to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` / `./output/entry.png`).
3. **Cryptographic Verification**: Verifies byte-level equality and SHA-256 hash match between source and destination.
