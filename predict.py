"""Classify network-traffic records with the trained model.

Usage:
    python predict.py path/to/records.csv            # writes predictions to records_predictions.csv
    python predict.py                                 # runs on two built-in example records
"""
import sys
from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path(__file__).parent / "model" / "intrusion_model.joblib"
LABELS = {"A": "Anomaly", "S": "Signature", "SS": "Synthetic signature"}
RENAME = {"Protcol": "Protocol", "SeddAddress": "SeedAddress"}  # original UGRansome column spellings

EXAMPLES = pd.DataFrame([
    {"Time": 50, "Protocol": "TCP", "Flag": "A", "Family": "WannaCry", "Clusters": 1, "SeedAddress": "1DA11mPS",
     "ExpAddress": "1BonuSr7", "BTC": 1, "USD": 500, "Netflow_Bytes": 5, "IPaddress": "A", "Threats": "Bonet", "Port": 5061},
    {"Time": 26, "Protocol": "UDP", "Flag": "APS", "Family": "Locky", "Clusters": 2, "SeedAddress": "1SYSTEMQ",
     "ExpAddress": "1SYSTEMQ", "BTC": 20, "USD": 8000, "Netflow_Bytes": 1500, "IPaddress": "C", "Threats": "Scan", "Port": 5062},
])


def predict(records: pd.DataFrame, model=None) -> pd.DataFrame:
    model = model or joblib.load(MODEL_PATH)
    records = records.rename(columns=RENAME)
    features = records.drop(columns=["Prediction"], errors="ignore")
    proba = model.predict_proba(features)
    out = records.copy()
    out["predicted"] = model.classes_[proba.argmax(axis=1)]
    out["predicted_label"] = out["predicted"].map(LABELS)
    out["confidence"] = proba.max(axis=1).round(4)
    return out


def main(args):
    if args:
        path = Path(args[0])
        result = predict(pd.read_csv(path))
        out_path = path.with_name(f"{path.stem}_predictions.csv")
        result.to_csv(out_path, index=False)
        print(result["predicted_label"].value_counts().to_string())
        print(f"Saved {len(result):,} predictions to {out_path}")
    else:
        print(predict(EXAMPLES)[["Family", "Threats", "Flag", "predicted", "predicted_label", "confidence"]].to_string(index=False))


if __name__ == "__main__":
    main(sys.argv[1:])
