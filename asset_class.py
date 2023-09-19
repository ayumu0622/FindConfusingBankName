import pandas as pd
import polars as pl
from itertools import combinations
from Levenshtein import distance

class AssetClass:

    def __init__(self, file_location, year=2020, top_k=50, levenshtein_degree=3):
        self.file_location = file_location
        self.top_k = top_k
        self.year = year
        self.levenshtein_degree = levenshtein_degree
        self.df = None
        pl.Config.set_tbl_rows(top_k)
    
    def read_csv(self):
        df = pl.read_csv(self.file_location, columns = ['year', 'rssdid', 'namefull', 'asset'])
        df = df.filter(pl.col('year') == self.year)
        return df
    
    def ordering(self, df):
        ranked_df = df.sort('asset', descending=True)
        ranked_df = ranked_df.unique(subset = ['rssdid'], keep = 'first')
        ranked_df = ranked_df.sort('asset', descending=True)
        return ranked_df
    
    def output_file(self, df, file_name):
        print(df)
        df.write_csv(f"{file_name}")
        return None
    
    def find_two_combination(self, top_k):
        return list(combinations(top_k, 2))

    def similarity(self, topk_df):
        topk_list = topk_df.select('namefull').to_series().to_list()
        topk_comb_list = self.find_two_combination(topk_list)
        output = []
        for bank1, bank2 in topk_comb_list:
            if distance(bank1, bank2) >= 0 and distance(bank1, bank2) < self.levenshtein_degree:
                print(f"{bank1} and {bank2} are similar name and non-distict pair")
                output.append([bank1, bank2])
        
        distinct = topk_df.clone()

        for bank1, bank2 in output:
            distinct = distinct.filter((pl.col("namefull") != bank1) & (pl.col("namefull") != bank2))
        
        non_distinct = pl.DataFrame()
        for bank1, bank2 in output:
            temp_df = topk_df.filter((pl.col("namefull") == bank1) | (pl.col("namefull") == bank2))
            non_distinct = pl.concat([non_distinct, temp_df])

        return distinct, non_distinct
    
    def find_topk(self, df):
        df = self.ordering(df)
        return df.head(self.top_k).select('rssdid', 'namefull')

    
    def main(self):
        self.df = self.read_csv()
        top_k_frame = self.find_topk(self.df)
        self.output_file(top_k_frame, 'Deliverable1.csv')
        distinct, non_distinct = self.similarity(top_k_frame)
        self.output_file(distinct, 'Deliverable2.csv')
        self.output_file(non_distinct, 'Deliverable3.csv')

