# FindSimilarBankName Project

## Overview

The "FindSimilarBankName" project, designed for a dataset of 2 million rows, focuses on identifying and resolving cases where different banks share the same "rssdid" due to similar or confusing bank names. The project utilizes the Polars library for efficient data manipulation and employs the Levenshtein distance algorithm for accurate similarity detection.

## Project Structure

- **asset_class.py**: This module is dedicated to data manipulation. It encapsulates functions and classes responsible for handling and processing the dataset, emphasizing modularity and clarity in data-related tasks.

- **main.py**: The main script orchestrating the entire project. It coordinates the execution of different modules and ensures the seamless flow of data processing.

- **non_distinct_name.csv**: This output file contains the names of banks within the top 50 assets that are deemed non-distinct due to similar or confusing names. The Levenshtein distance algorithm is applied to identify such cases accurately.

- **top_50_bank.csv**: This output file provides a list of the top 50 banks based on their asset amounts. The Polars library is leveraged for efficient data handling to determine and extract this essential information.

## Tools and Libraries

The project's backbone is the Polars library, chosen for its efficiency in handling large datasets. This library plays a crucial role in the data manipulation tasks performed in the "asset_class.py" module.

## Similarity Detection

To address the intricacies of bank name similarity, the project uses the Levenshtein distance algorithm. This character-based similarity measure is adept at detecting subtle differences between bank names, minimizing false positives, and ensuring accurate matching.

## Choice of Similarity Algorithm

The decision to favor Levenshtein distance over alternative methods, such as TF-IDF + cosine similarity, is driven by the need to capture character-level differences. This choice aligns with the project's objective of identifying non-similarities, particularly those arising from spelling mistakes in bank names.

## Implementation

The code is organized in an object-oriented fashion to enhance modularity and maintainability. This design choice ensures readability and facilitates future modifications or enhancements to the project.

## Conclusion

The "FindSimilarBankName" project, with its structured approach to data manipulation, efficient use of the Polars library, and precise similarity detection using the Levenshtein distance algorithm, stands as a robust solution to handling similar or confusing bank names. The output files, "non_distinct_name.csv" and "top_50_bank.csv," provide valuable insights into non-distinct bank names and the top 50 banks based on asset amounts, respectively.

