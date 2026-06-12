"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabase";

export default function UploadZone() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [analyzing, setAnalyzing] = useState(false);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    if (!e.target.files?.length) return;

    const selectedFile = e.target.files[0];

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

 const handleUpload = async () => {
  if (!file) return;

  setAnalyzing(true);

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

    const filePath = `${Date.now()}-${file.name}`;

    const { error: uploadError } = await supabase.storage
      .from("evidence")
      .upload(filePath, file);

    if (uploadError) {
      console.error(uploadError);
      alert("Storage upload failed");
      setAnalyzing(false);
      return;
    }

    const { data: publicData } = supabase.storage
      .from("evidence")
      .getPublicUrl(filePath);

    const imageUrl = publicData.publicUrl;

    const { error } = await supabase
      .from("audits")
      .insert([
        {
          image_url: imageUrl,
          deception_score: data.deception_score,
          risk_level: data.risk_level,
        },
      ]);

    if (error) {
      console.error(error);
      alert(error.message);
      setAnalyzing(false);
      return;
    }

    alert(
      `Score: ${data.deception_score}

Risk: ${data.risk_level}

Patterns: ${data.patterns.join(", ")}`
    );
  } catch (error) {
    console.error(error);
    alert("Analysis failed");
  }

  setAnalyzing(false);
};

return (
  <div className="text-center">
    <div className="border-2 border-dashed border-slate-700 rounded-2xl p-10 bg-slate-950">

      <input
        type="file"
        accept="image/*,video/*"
        onChange={handleChange}
        className="mb-6 text-slate-300"
      />

      {file && (
        <div className="mb-6">
          <p className="font-semibold text-white">
            {file.name}
          </p>

          <p className="text-slate-400">
            {(file.size / 1024).toFixed(2)} KB
          </p>
        </div>
      )}

      {preview && file?.type.startsWith("image") && (
        <img
          src={preview}
          alt="Preview"
          className="max-h-80 mx-auto rounded-xl border border-slate-700 mb-6"
        />
      )}

      {preview && file?.type.startsWith("video") && (
        <video
          controls
          className="max-h-80 mx-auto rounded-xl border border-slate-700 mb-6"
        >
          <source src={preview} />
        </video>
      )}

      <button
        onClick={handleUpload}
        disabled={!file || analyzing}
        className="bg-cyan-500 hover:bg-cyan-400 text-black font-bold px-6 py-3 rounded-xl transition disabled:opacity-50"
      >
        {analyzing ? "Analyzing..." : "Analyze Evidence"}
      </button>

    </div>
  </div>
);
}