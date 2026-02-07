import json
import os

def build_final_output(metadata, compressed_data, qa_block=None, loss_report=None, file_path=None):
    if file_path is None:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "compressed_output.json")

    final_output = {
        "metadata": metadata,
        "compressed_representation": compressed_data,
        "explainability": {
            "why_included": "High-signal sections containing definitions, risks, safeguards, or governance-related rules were retained.",
            "what_was_removed": loss_report["loss_reasoning"] if loss_report else "Descriptive and repetitive text removed.",
            "traceability": "Each summary and risk item is traceable using source_chunk identifiers."
        },
        "compression_metrics": {
            "original_chars": loss_report["original_chars"] if loss_report else None,
            "compressed_chars": loss_report["compressed_chars"] if loss_report else None,
            "compression_ratio": loss_report["compression_ratio"] if loss_report else None,
            "retention": round(1 - loss_report["compression_ratio"], 2) if loss_report else None
        }
    }

    if qa_block:
        final_output["qa"] = qa_block

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=4)

    return final_output
