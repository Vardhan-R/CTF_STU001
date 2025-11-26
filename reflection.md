# How I solved the CTF_STU001 challenge

## FLAG1
- Computed the SHA256 hash of the string "STU001".
- Took the first 8 characters of the resulting hash to get `to_find`.
- Read the `reviews.csv` file using the pandas library.
- Filtered the reviews to find the one where the `text` column contains `to_find`.
- Obtained the `title` column of that review.
- Ignored spaces in the title and took the first 8 characters.
- Computed the SHA-256 hash of these 8 characters to get FLAG1.

## FLAG2
- Used the previously computed `to_find` value (first 8 characters of the SHA-256 hash of "STU001").
- Converted `to_find` to uppercase.
- Formatted FLAG2 as `FLAG2{TO_FIND}` where `TO_FIND` is the uppercase version of `to_find`.
