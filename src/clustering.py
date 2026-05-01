from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def apply_clustering(rfm):
    print("Applying clustering...")

    # Remove any missing values
    rfm = rfm.dropna()

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    kmeans = KMeans(n_clusters=3, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    print("Clustering done")
    return rfm