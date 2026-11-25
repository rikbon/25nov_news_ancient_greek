import os
import sys
import shutil
import hashlib
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def compute_sha256(path):
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entry.png')
    if not os.path.exists(src):
        logging.error(f"Source file not found: {src}")
        sys.exit(1)

    if os.path.exists('/output') and os.access('/output', os.W_OK):
        dest_dir = '/output'
    elif os.environ.get('MAKEFUN_OUTPUT_DIR'):
        dest_dir = os.environ['MAKEFUN_OUTPUT_DIR']
    else:
        dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, 'entry.png')

    logging.info(f"Copying entry image from {src} to {dest}...")
    shutil.copyfile(src, dest)

    src_hash = compute_sha256(src)
    dest_hash = compute_sha256(dest)

    if src_hash != dest_hash:
        logging.error(f"Integrity check failed! Src: {src_hash} != Dest: {dest_hash}")
        sys.exit(1)

    logging.info(f"Integrity verified (SHA-256: {src_hash}).")
    logging.info("Entry generation completed successfully.")
    sys.exit(0)

if __name__ == '__main__':
    main()
