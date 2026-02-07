from extractors.pdf_extractor import extract_text_from_pdf
from extractors.text_extractor import extract_text_from_txt
from cleaner import clean_text
from chunker import chunk_text
from compressor import compress_chunks
from qa_engine import answer_question
from output_builder import build_final_output
from loss_estimator import estimate_loss
from loss_estimator import estimate_loss

import os

def extract_document(path):
    if path.endswith(".pdf"):
        return extract_text_from_pdf(path)
    elif path.endswith(".txt"):
        return extract_text_from_txt(path)
    else:
        raise ValueError("Unsupported file format")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "data", "sample.txt")

    raw_text = extract_document(file_path)
    print("TXT LENGTH:", len(raw_text))

    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text, chunk_size=300, overlap=50)

    compressed_data = compress_chunks(chunks)

    # ---------- LOSS REPORT ----------
    loss_report = estimate_loss(raw_text, compressed_data)

    # ---------- QA ----------
    summaries = [s["summary"] for s in compressed_data["section_summaries"]]

    question = input("\nAsk a question about the document:\n> ")
    qa_result = answer_question(question, summaries)

    # ---------- TERMINAL OUTPUT ----------
    print("\n--- ANSWER ---")
    print("Q:", question)
    print("A:", qa_result["answer"])
    print("Why:", qa_result["why"])
    print("Source chunk:", qa_result["source_chunk"])
    print("Confidence:", qa_result["confidence"])

    print("\n--- COMPRESSION EXPLANATION ---")
    print("Why included:", "High-signal content (definitions, risks, safeguards)")
    print("What removed:", loss_report["loss_reasoning"])
    print("Traceability:", "Yes, via source_chunk IDs")
    print("Compression ratio:", loss_report["compression_ratio"])
    print("Retention:", round(1 - loss_report["compression_ratio"], 2))

    # ---------- METADATA ----------
    metadata = {
        "source_file": "sample.txt",
        "document_type": "text",
        "total_chunks": len(chunks)
    }

    qa_block = {
        "question": question,
        "answer": qa_result["answer"],
        "why": qa_result["why"],
        "source_chunk": qa_result["source_chunk"],
        "confidence": qa_result["confidence"]
    }

    final_output = build_final_output(
        metadata=metadata,
        compressed_data=compressed_data,
        qa_block=qa_block,
        loss_report=loss_report
    )

    print("\nOutput written to compressed_output.json")
