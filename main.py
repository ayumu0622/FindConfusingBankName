from asset_class import AssetClass

if __name__ == "__main__":
    year = 2020
    top_k = 200
    #number of changes
    levenshtein_degree = 3
    instance1 = AssetClass("./sod_2020.csv", year, top_k, levenshtein_degree)
    instance1.main()
    
    