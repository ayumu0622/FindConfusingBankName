# FindSimilarBankName Project
<img width="260" alt="Screen Shot 2023-10-09 at 12 26 59 AM" src="https://github.com/ayumu0622/FindConfusingBankName/assets/67722808/9968e7ad-a8b2-4d89-880d-9b6a25e0f95d">


## Overview

"FindSimilarBankName" addresses the challenge of different banks having similar name in a 2.5 million-row dataset. Leveraging Polars, it identifies and resolves similar names, ensuring precise matching for users comparing bank data with resumes.

## Project Structure

- **asset_class.py**: Manages data manipulation tasks.
- **main.py**: Orchestrates the project execution.
- **non_distinct_name.csv**: Lists non-distinct bank names in the top 50 assets.
- **top_50_bank.csv**: Provides a list of the top 50 banks by assets.

## Tools and Libraries

The project relies on Polars for handling large datasets.

## Similarity Detection

Levenshtein distance is used to detect subtle character-level differences in bank names.

## Implementation

The code is organized in an object-oriented manner for modularity and maintainability.

## Conclusion

"FindSimilarBankName" ensures accurate handling of similar or confusing bank names. Output files offer insights into non-distinct bank names and the top 50 banks by assets.

