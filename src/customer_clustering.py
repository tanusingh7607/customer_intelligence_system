import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def apply_clustering(rfm):
    """  
    Parameters:
    -----------
    rfm : DataFrame
        RFM data with Recency, Frequency, Monetary columns
    
    Returns:
    --------
    rfm : DataFrame
        RFM data with added Cluster column
    """
    # Prepare data for clustering
    rfm_for_clustering = rfm[['Recency', 'Frequency', 'Monetary']].copy()
    
    # Log transform to handle skewness
    rfm_for_clustering['Monetary'] = rfm_for_clustering['Monetary'].apply(lambda x: np.log1p(x) if x > 0 else 0)
    rfm_for_clustering['Frequency'] = rfm_for_clustering['Frequency'].apply(lambda x: np.log1p(x) if x > 0 else 0)
    
    # Standardize the data
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_for_clustering)
    
    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)
    
    return rfm