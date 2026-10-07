#!/usr/bin/env python3
"""Read-only reporting probes over the bundled frozen JSON artifacts."""
from __future__ import annotations
import argparse, json
from pathlib import Path

DATA = Path(__file__).parent / "data"
SPINE = DATA / "spine_results.json"
WHY5 = DATA / "why5_analysis.json"

def load():
    return json.loads(SPINE.read_text())

def floor():
    d = load(); out = {}
    for part, s in d["summary"].items():
        out[part] = {
            "n": s["n_windows"],
            "floor_median": s["toll"]["median"],
            "target_edit_distance_median": s["edit_amplitude"]["median"],
            "oracle_endpoint_median": s["exact_construction"]["median"],
            "no_op_median": s["do_nothing"]["median"],
            "endpoint_gain_median": s["advantage_ratio"]["median"],
            "target_below_floor": s["assertions"]["target_vs_toll_fail_count"] if "assertions" in s else s["target_vs_toll_fail_count"],
        }
    print(json.dumps(out, indent=2, sort_keys=True))

def oracle():
    d = load(); out = {}
    for part, s in d["summary"].items():
        out[part] = {
            "oracle_endpoint_median": s["exact_construction"]["median"],
            "latent_no_op_baseline_median": s["do_nothing"]["median"],
            "endpoint_gain_median": s["advantage_ratio"]["median"],
        }
    print(json.dumps(out, indent=2, sort_keys=True))

def strata():
    d = json.loads(WHY5.read_text())
    out = {
        "flac_wavpack_spearman": d["pairwise_correlations"]["flac5 vs wavpack"]["spearman"],
        "heldout_flac_spearman": {k: v["spearman"] for k, v in d["heldout_anchor_error_correlations"]["flac5"].items()},
        "r2": {
            "content_only": d["regression"]["flac5"]["content_only_R2"],
            "content_plus_codec": d["regression"]["flac5"]["content_plus_codec_R2"],
            "percentage_points": (d["regression"]["flac5"]["content_plus_codec_R2"] - d["regression"]["flac5"]["content_only_R2"]) * 100,
        },
        "flac_strata": {
            band: {
                "n": row["n"],
                "mean_error": row["mean_error"],
                "winner_counts": row["winner_counts"],
            } for band, row in d["strata"]["flac5"].items()
        },
        "codec_mean_error": d["codec_mean_error"],
    }
    print(json.dumps(out, indent=2, sort_keys=True))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["floor", "oracle", "strata"])
    a = p.parse_args()
    {"floor": floor, "oracle": oracle, "strata": strata}[a.command]()

if __name__ == "__main__":
    main()
