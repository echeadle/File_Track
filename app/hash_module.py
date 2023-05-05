import hashlib

# Define hash function
def hash_file(filename, hash_type='sha256'):
    hasher = hashlib.new(hash_type)
    with open(filename, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

# Guard clause for testing/debugging
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: hash_module.py filename [hash_type]")
        sys.exit(1)
    filename = sys.argv[1]
    hash_type = sys.argv[2] if len(sys.argv) > 2 else 'sha256'
    hash_value = hash_file(filename, hash_type)
    print(f"{hash_type} hash of {filename}: {hash_value}")

