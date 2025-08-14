MASTER_URL = "https://raw.githubusercontent.com/USERNAME/REPO/BRANCH/MasterSeriesHistory.xlsx"
RULES_URL = "https://raw.githubusercontent.com/USERNAME/REPO/BRANCH/SampleSeriesRules.xlsx"

def compare_requested_series_from_github(comparison_path, top_n=2):
    df_master = load_file(MASTER_URL)
    df_rules = load_file(RULES_URL)
    df_comparison = load_file(comparison_path)

    results = []
    for idx, row in df_comparison.iterrows():
        comparison_series = normalize_series(row["Series"])
        matches = []
        for _, master_row in df_master.iterrows():
            master_series = normalize_series(master_row["Series"])
            ratio = similarity_ratio(comparison_series, master_series)
            matches.append((master_series, ratio))
        matches.sort(key=lambda x: x[1], reverse=True)
        top_matches = matches[:top_n]
        results.append({"Requested": comparison_series, "Matches": top_matches})

    return pd.DataFrame(results)
