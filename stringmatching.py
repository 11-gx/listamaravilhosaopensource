def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101  # A prime number for hash calculation
    pat_hash = 0
    txt_hash = 0
    h = 1

    # Calculate the hash value of the pattern and the first substring of the text
    for i in range(m-1):
        h = (h * 256) % prime
    for i in range(m):
        pat_hash = (256 * pat_hash + ord(pattern[i])) % prime
        txt_hash = (256 * txt_hash + ord(text[i])) % prime

    # Slide the pattern over the text and compare hash values
    for i in range(n - m + 1):
        if pat_hash == txt_hash:
            if pattern == text[i:i + m]:
                return i
        if i < n - m:
            txt_hash = (256 * (txt_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if txt_hash < 0:
                txt_hash += prime

    return -1
