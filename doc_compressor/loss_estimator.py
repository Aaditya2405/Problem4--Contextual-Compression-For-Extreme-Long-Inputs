def estimate_loss(original_text, compressed_data):
    original_chars = len(original_text)

    compressed_chars = 0
    for section in compressed_data.get("section_summaries", []):
        compressed_chars += len(section.get("summary", ""))

    compression_ratio = round(compressed_chars / original_chars, 2)

    return {
        "original_chars": original_chars,
        "compressed_chars": compressed_chars,
        "compression_ratio": compression_ratio,
        "loss_reasoning": "Removed descriptive, redundant, and low-signal text while preserving legal meaning"
    }
