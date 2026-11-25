"""
News Image Entrypoint - Wednesday 25 November 2026 (Classical Ceramic Art Edition)

Deterministic submission entrypoint for make.fun competition news-image-20261125.
Validates the canonical visual news chronicle (entry.png), outputs it atomically
to the target directory (/output, $MAKEFUN_OUTPUT_DIR, or ./output), and verifies
that the destination file exactly matches the source image byte-for-byte.
"""

import hashlib
import os
import shutil
import sys

# Supported image headers (PNG and JPEG/JFIF)
VALID_IMAGE_PREFIXES = (
    b"\x89PNG\r\n\x1a\n",  # PNG
    b"\xff\xd8\xff",        # JPEG
)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MiB safety upper bound; submission is under 1 MiB


def validate_source(src_path: str) -> None:
    """
    Validate that the source image exists, is a regular file, is non-empty,
    does not exceed size limits, and contains a valid image header signature.

    :param src_path: Absolute path to the source entry image.
    :raises FileNotFoundError: If src_path does not exist.
    :raises ValueError: If src_path is not a valid or non-empty image file.
    """
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source file not found: {src_path}")
    if not os.path.isfile(src_path):
        raise ValueError(f"Source path is not a regular file: {src_path}")

    size = os.path.getsize(src_path)
    if size == 0:
        raise ValueError(f"Source file is empty: {src_path}")
    if size > MAX_FILE_SIZE:
        raise ValueError(f"Source file exceeds maximum size limit ({size} > {MAX_FILE_SIZE} bytes)")

    with open(src_path, "rb") as f:
        header = f.read(8)
        if not any(header.startswith(prefix) for prefix in VALID_IMAGE_PREFIXES):
            raise ValueError(f"Invalid or unrecognized image signature in {src_path}: {header[:4]!r}")


def get_output_dir(base_dir: str) -> str:
    """
    Determine and validate the target output directory.
    Priority:
      1. $MAKEFUN_OUTPUT_DIR if specified in the environment.
      2. /output if it exists and is writable.
      3. ./output relative to this script.

    :param base_dir: Base directory containing main.py.
    :return: Absolute path to the validated output directory.
    :raises PermissionError: If the target output directory cannot be written to.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_dir = os.path.abspath(out_dir)
    elif os.path.exists("/output") and os.access("/output", os.W_OK):
        out_dir = "/output"
    else:
        out_dir = os.path.join(base_dir, "output")

    os.makedirs(out_dir, exist_ok=True)
    if not os.access(out_dir, os.W_OK):
        raise PermissionError(f"Output directory is not writable: {out_dir}")
    return out_dir


def compute_sha256(filepath: str) -> str:
    """
    Compute the hexadecimal SHA-256 digest of a file.

    :param filepath: Path to file.
    :return: 64-character lowercase hex digest string.
    """
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_output(src_path: str, dest_path: str) -> None:
    """
    Verify that destination file exists, matches source size, and matches
    source SHA-256 hash byte-for-byte.

    :param src_path: Source canonical image path.
    :param dest_path: Output written image path.
    :raises FileNotFoundError: If destination file does not exist.
    :raises ValueError: If size or hash verification fails.
    """
    if not os.path.exists(dest_path):
        raise FileNotFoundError(f"Destination file was not created: {dest_path}")

    src_size = os.path.getsize(src_path)
    dest_size = os.path.getsize(dest_path)
    if src_size != dest_size:
        raise ValueError(
            f"Size mismatch: source ({src_size} bytes) vs destination ({dest_size} bytes)"
        )

    src_hash = compute_sha256(src_path)
    dest_hash = compute_sha256(dest_path)
    if src_hash != dest_hash:
        raise ValueError(
            f"Hash mismatch: source ({src_hash}) vs destination ({dest_hash})"
        )


def main() -> None:
    """
    Main entrypoint: validates source image, copies atomically to destination,
    and asserts cryptographic match.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(base_dir, "entry.png")

    try:
        # Step 1: Input validation
        validate_source(src)

        # Step 2: Determine output directory
        out_dir = get_output_dir(base_dir)
        dest = os.path.join(out_dir, "entry.png")

        # Step 3: Atomic write
        tmp_dest = dest + ".tmp"
        shutil.copyfile(src, tmp_dest)
        os.replace(tmp_dest, dest)

        # Step 4: Verification
        verify_output(src, dest)

        sys.stdout.write(
            f"Verified entry: {dest} ({os.path.getsize(dest)} bytes, SHA-256: {compute_sha256(dest)})\n"
        )
        sys.exit(0)
    except Exception as exc:
        sys.stderr.write(f"Error: {exc}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
