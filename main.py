"""
News Image Entrypoint - Wednesday 25 November 2026 (Ancient Greek Style)
Copies the bundled image entry.png to the target evaluation directory (/output/entry.png).
"""

import os
import shutil
import sys

def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entry.png')
    if not os.path.exists(src):
        sys.stderr.write(f"Error: {src} not found\n")
        sys.exit(1)

    # Determine destination directory: /output if accessible, or MAKEFUN_OUTPUT_DIR, or ./output
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR')
    if not out_dir:
        if os.path.exists('/output') and os.access('/output', os.W_OK):
            out_dir = '/output'
        else:
            out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, 'entry.png')

    # Atomic write to guarantee determinism
    tmp_dest = dest + '.tmp'
    shutil.copyfile(src, tmp_dest)
    os.replace(tmp_dest, dest)
    sys.stdout.write(f"Wrote {dest} ({os.path.getsize(dest)} bytes)\n")
    sys.exit(0)

if __name__ == '__main__':
    main()
