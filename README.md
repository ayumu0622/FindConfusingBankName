# FindSimilarBankName
For this task, I'm interested in working exclusively with the "namefull," 
"rssdid," and "asset" columns. I've chosen to utilize Polars over Pandas to 
identify the top 50 assets. Polars, renowned for its superior performance with 
larger datasets, is my preferred choice over pandas in this context.

  
When comparing "American Bank" and "Bank of America," their meaning are nearly identical, 
so if I use word based similarity, probably this pair are detected as non-distinct 
pair even though they are distinct and easily distinguishable. For resumes, most individuals can 
correctly write the bank names, but some might make typographical errors or omit characters. 
In such cases, it is essential to employ a character-based similarity algorithm to detect subtle character-level differences between the two bank names. 
The primary objective of this task is to minimize false positives, ensuring accurate matching and avoiding errors. In this regard,
    TF-IDF + cosine similarity is not an appropriate choice for detecting non-similarity in this case, since it is likely due to its emphasis on matching the meaning 
of the entire sentence rather than differences in the sequence of individual words.


Therefore, I used Levenshtein distance (https://en.wikipedia.org/wiki/Levenshtein_distance) which 
is character based sentence similarity algorithm to see if there are similar bank name which might 
cause spelling mistakes.

##2431459
