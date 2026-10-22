# Dataset

This project uses the **UGRansome** dataset by Mike Nkongolo, a network-traffic dataset built for ransomware and zero-day attack detection.

- Kaggle: https://www.kaggle.com/datasets/nkongolo/ugransome-dataset
- 149,043 records, 13 features, and 3 target classes: `A` (anomaly), `S` (signature), `SS` (synthetic signature)

## Setup

1. Download the dataset CSV from the Kaggle page (you need a free Kaggle account).
2. Save it in this folder as **`data/ugransome.csv`**.

The notebook renames two misspelled columns from the original file (`Protcol` → `Protocol`, `SeddAddress` → `SeedAddress`).

## Columns

| Column | Description |
|--------|-------------|
| Time | Timestamp of the network event |
| Protocol | TCP, UDP or ICMP |
| Flag | TCP flags seen in the connection |
| Family | Ransomware family (WannaCry, Locky, CryptoLocker, ...) |
| Clusters | Cluster ID of the event |
| SeedAddress / ExpAddress | Bitcoin seed and exploit addresses (anonymised prefixes) |
| BTC / USD | Ransom payment amounts |
| Netflow_Bytes | Bytes transferred in the flow |
| IPaddress | Anonymised IP class |
| Threats | Threat type (DoS, Scan, Spam, Bonet, SSH, ...) |
| Port | Destination port |
| **Prediction** | Target: `A`, `S` or `SS` |

## Citation

Nkongolo, M., van Deventer, J. P., & Kasongo, S. M. (2021). *UGRansome1819: A novel dataset for anomaly detection and zero-day threats.* Information, 12(10), 405.
