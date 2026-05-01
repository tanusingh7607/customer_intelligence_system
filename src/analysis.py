import matplotlib.pyplot as plt
import os

def label_clusters(rfm):
    print("\nCluster Summary:\n")
    print(rfm.groupby('Cluster').mean())


def assign_labels(rfm):
    def label(row):
        if row['Monetary'] > 1000 and row['Frequency'] > 5:
            return 'High Value'
        elif row['Monetary'] > 300:
            return 'Medium Value'
        else:
            return 'Low Value'

    rfm['CustomerSegment'] = rfm.apply(label, axis=1)
    return rfm


def plot_clusters(rfm):
    os.makedirs("outputs/charts", exist_ok=True)

    rfm['CustomerSegment'].value_counts().plot(kind='bar')
    plt.title("Customer Segments Distribution")

    plt.savefig("outputs/charts/customer_segments.png")
    plt.close()