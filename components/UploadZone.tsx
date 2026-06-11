"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabase";

export default function UploadZone() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files?.length) return;

    const selectedFile = e.target.files[0];

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleUpload = async () => {
    if (!file) return;

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      alert(
  `Text: ${data.extracted_text}

Score: ${data.deception_score}

Risk: ${data.risk_level}

Patterns: ${data.patterns.join(", ")}`
);

     const { error } = await supabase
  .from("audits")
  .insert([
    {
      image_url: file.name,
      deception_score: data.deception_score,
      risk_level: data.risk_level,
    },
  ]);

      if (error) {
        console.error(error);
      }
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
  };

  return (
    <div className="border-2 border-dashed rounded-lg p-8 text-center">
      <input
        type="file"
        accept="image/*,video/*"
        onChange={handleChange}
        className="mb-4"
      />

      {file && (
        <div className="mt-4">
          <p className="font-semibold">{file.name}</p>
          <p>{(file.size / 1024).toFixed(2)} KB</p>
        </div>
      )}

      {preview && file?.type.startsWith("image") && (
        <img
          src={preview}
          alt="Preview"
          className="mt-4 max-h-64 mx-auto rounded"
        />
      )}

      {preview && file?.type.startsWith("video") && (
        <video
          controls
          className="mt-4 max-h-64 mx-auto rounded"
        >
          <source src={preview} />
        </video>
      )}

      <button
        onClick={handleUpload}
        disabled={!file}
        className="mt-4 border px-4 py-2 rounded"
      >
        Upload
      </button>
    </div>
  );
}