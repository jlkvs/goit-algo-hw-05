import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return -1

    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += skip.get(text[i], m)
    
    return -1

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0

    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                return i - m + 1
                j = lps[j - 1]
    
    return -1

def rabin_karp(text, pattern, prime=101):
    m = len(pattern)
    n = len(text)
    d = 256
    hpattern = 0
    htext = 0
    h = 1
    
    if m > n:
        return -1
    
    for i in range(m - 1):
        h = (h * d) % prime
    
    for i in range(m):
        hpattern = (d * hpattern + ord(pattern[i])) % prime
        htext = (d * htext + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            htext = (d * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            if htext < 0:
                htext += prime
    
    return -1

with open('one.txt', 'r') as file:
    text1 = file.read()

with open('two.txt', 'r') as file:
    text2 = file.read()


existing_substring1 = "ВИКОРИСТАННЯ"
nonexistent_substring1 = "вигаданий_пошук"
existing_substring2 = "Методи та структури"
nonexistent_substring2 = "невідомий_пошук"

results = {}

for name, func, text, substring in [
    ('Boyer-Moore on text1 (existing)', boyer_moore, text1, existing_substring1),
    ('Boyer-Moore on text1 (nonexistent)', boyer_moore, text1, nonexistent_substring1),
    ('KMP on text1 (existing)', kmp_search, text1, existing_substring1),
    ('KMP on text1 (nonexistent)', kmp_search, text1, nonexistent_substring1),
    ('Rabin-Karp on text1 (existing)', rabin_karp, text1, existing_substring1),
    ('Rabin-Karp on text1 (nonexistent)', rabin_karp, text1, nonexistent_substring1),
    ('Boyer-Moore on text2 (existing)', boyer_moore, text2, existing_substring2),
    ('Boyer-Moore on text2 (nonexistent)', boyer_moore, text2, nonexistent_substring2),
    ('KMP on text2 (existing)', kmp_search, text2, existing_substring2),
    ('KMP on text2 (nonexistent)', kmp_search, text2, nonexistent_substring2),
    ('Rabin-Karp on text2 (existing)', rabin_karp, text2, existing_substring2),
    ('Rabin-Karp on text2 (nonexistent)', rabin_karp, text2, nonexistent_substring2),
]:
    time_taken = timeit.timeit(lambda: func(text, substring), number=100)
    results[name] = time_taken

for key, value in results.items():
    print(f"{key}: {value:.6f} seconds")

text1_results = {k: v for k, v in results.items() if 'text1' in k}
text2_results = {k: v for k, v in results.items() if 'text2' in k}

fastest_text1 = min(text1_results, key=text1_results.get)
fastest_text2 = min(text2_results, key=text2_results.get)
overall_fastest = min(results, key=results.get)

print(f"\nНайшвидший алгоритм для тексту 1: {fastest_text1}")
print(f"Найшвидший алгоритм для тексту 2: {fastest_text2}")
print(f"Загалом найшвидший алгоритм: {overall_fastest}")

