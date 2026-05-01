from cleaning import load_data, clean_data
from feature_engineering import feature_engineering
from rfm import create_rfm
from clustering import apply_clustering
from analysis import label_clusters, assign_labels, plot_clusters

def main():
    df = load_data("data/online_retail.xlsx")
    df = clean_data(df)
    df = feature_engineering(df)

    rfm = create_rfm(df)
    rfm = apply_clustering(rfm)

    label_clusters(rfm)

    rfm = assign_labels(rfm)

    plot_clusters(rfm)
    rfm.to_csv("outputs/rfm_clusters.csv", index=False)
    print("RFM clusters saved to outputs/rfm_clusters.csv")

    print("\nFinal Output:\n")
    print(rfm.head())

if __name__ == "__main__":
    main()