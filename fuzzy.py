from fuzzywuzzy import process

def fuzzy_match_mpn(input_mpn, valid_mpns, threshold=90):
    """
    Perform fuzzy matching on an input MPN against a list of valid MPNs.
    :param input_mpn: The MPN provided by the user (may contain typos).
    :param valid_mpns: A list of valid MPNs from the database.
    :param threshold: The similarity score threshold (0-100).
    :return: A list of potential matches with their similarity scores.
    """
    matches = process.extract(input_mpn, valid_mpns, limit=5)  # Get top 5 matches
    return [match for match in matches if match[1] >= threshold]

# Example Usage
input_mpn = "TLV2372IDD"  # Typo in the last character
valid_mpns = ["TLV2372IDR", "TLV2372IDT", "TLV2372IDX", "TLV2372IDR-1"]  # Valid MPNs
matches = fuzzy_match_mpn(input_mpn, valid_mpns, threshold=90)
print(matches)  # Output: [('TLV2372IDR', 90)]

######################################################################################################################################
#Your `fuzzy_match_mpn` function is designed to perform fuzzy matching on an input MPN (Manufacturer Part Number) against a list of valid MPNs. 
It uses the `fuzzywuzzy` library's `process.extract` method to get the top 5 matches and then filters them based on the similarity score threshold.
Here's a step-by-step explanation:

1. **Importing the Library**: `from fuzzywuzzy import process`
   - This imports the `process` module from the `fuzzywuzzy` library, which provides functions for fuzzy string matching.

2. **Function Definition**: `def fuzzy_match_mpn(input_mpn, valid_mpns, threshold=90):`
   - Defines the function `fuzzy_match_mpn` with three parameters: `input_mpn` (the input MPN to match), `valid_mpns` (a list of valid MPNs), and `threshold` (the similarity score threshold, default is 90).

3. **Docstring**:
   - Provides a brief explanation of the function's purpose and parameters.

4. **Extract Matches**: `matches = process.extract(input_mpn, valid_mpns, limit=5)`
   - Uses `process.extract` to find the top 5 matches for the input MPN from the list of valid MPNs.

5. **Filter Matches**: `return [match for match in matches if match[1] >= threshold]`
   - Filters the matches to include only those with a similarity score greater than or equal to the threshold.

6. **Example Usage**:
   - Shows an example usage of the `fuzzy_match_mpn` function.

##########################################################
