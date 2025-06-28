import { useState } from "react";
import api from "../api/axios";

export default function PitchForm() {
  const [form, setForm] = useState({
    seller_name: "",
    product_name: "",
    pitch_text: ""
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await api.post("/pitch/submit/", form);
      setResult(res.data);
    } catch (err) {
      alert("❌ Error submitting pitch.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-blue-50 to-violet-100 px-4 py-12">
      <div className="w-full max-w-2xl bg-white/80 backdrop-blur-md shadow-xl rounded-2xl p-8 border border-white/30">
        <h1 className="text-3xl font-extrabold text-center text-gray-800 mb-6">🎤 PitchCraft AI</h1>
        <form onSubmit={handleSubmit} className="space-y-6">
          <FloatingInput
            label="Seller Name"
            name="seller_name"
            value={form.seller_name}
            onChange={handleChange}
            required
          />
          <FloatingInput
            label="Product Name"
            name="product_name"
            value={form.product_name}
            onChange={handleChange}
            required
          />
          <FloatingTextarea
            label="Your Pitch"
            name="pitch_text"
            value={form.pitch_text}
            onChange={handleChange}
            required
          />

          <button
            type="submit"
            disabled={loading}
            className={`w-full py-3 rounded-md font-semibold transition text-white text-lg shadow-md ${
              loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            {loading ? "✨ Generating AI Feedback..." : "🚀 Submit Pitch"}
          </button>
        </form>

        {result && (
          <div className="mt-8 bg-white border-l-4 border-blue-600 p-6 rounded-lg shadow-sm">
            <h3 className="text-xl font-bold text-blue-800 mb-2">💡 AI Feedback:</h3>
            <p className="text-gray-700 whitespace-pre-wrap">{result.ai_feedback}</p>
          </div>
        )}
      </div>
    </div>
  );
}

function FloatingInput({ label, name, value, onChange, required }) {
  return (
    <div className="relative">
      <input
        type="text"
        name={name}
        value={value}
        onChange={onChange}
        required={required}
        placeholder=" "
        className="peer w-full border border-gray-300 rounded-md px-4 pt-6 pb-2 text-gray-800 placeholder-transparent focus:outline-none focus:border-blue-600 focus:ring-2 focus:ring-blue-200"
      />
      <label
        htmlFor={name}
        className="absolute left-4 top-2 text-gray-500 text-sm transition-all peer-placeholder-shown:top-3.5 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-focus:top-2 peer-focus:text-sm peer-focus:text-blue-600"
      >
        {label}
      </label>
    </div>
  );
}

function FloatingTextarea({ label, name, value, onChange, required }) {
  return (
    <div className="relative">
      <textarea
        name={name}
        value={value}
        onChange={onChange}
        rows={5}
        required={required}
        placeholder=" "
        className="peer w-full border border-gray-300 rounded-md px-4 pt-6 pb-2 text-gray-800 placeholder-transparent focus:outline-none focus:border-blue-600 focus:ring-2 focus:ring-blue-200"
      ></textarea>
      <label
        htmlFor={name}
        className="absolute left-4 top-2 text-gray-500 text-sm transition-all peer-placeholder-shown:top-3.5 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-focus:top-2 peer-focus:text-sm peer-focus:text-blue-600"
      >
        {label}
      </label>
    </div>
  );
}
