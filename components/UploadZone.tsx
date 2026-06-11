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
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const { error } = await supabase
      .from("audits")
      .insert([
        {
          image_url: file.name,
          deception_score: 0,
          risk_level: "Pending",
        },
      ]);

    if (error) {
      console.error(error);
      alert(error.message);
      return;
    }

    alert("Audit created successfully");
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
        <video controls className="mt-4 max-h-64 mx-auto rounded">
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