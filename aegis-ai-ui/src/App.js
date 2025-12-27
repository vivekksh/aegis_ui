import { useState } from "react";
import Header from "./components/Header";
import PredictionForm from "./components/PredictionForm";
import ForecastCards from "./components/ForecastCards";
import SystemStatus from "./components/SystemStatus";

function App() {
  const [darkMode, setDarkMode] = useState(true);

  const [formData, setFormData] = useState({
    hour: 18,
    day_of_week: 4,
    month: 7,
    lag_1: 3.5,
    lag_24: 3.1,
    rolling_24h: 3.3,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const isFormValid =
    formData.hour !== "" &&
    formData.day_of_week !== "" &&
    formData.month !== "" &&
    formData.lag_1 !== "" &&
    formData.lag_24 !== "" &&
    formData.rolling_24h !== "";

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/predict/multi-horizon",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            hour: Number(formData.hour),
            day_of_week: Number(formData.day_of_week),
            month: Number(formData.month),
            lag_1: Number(formData.lag_1),
            lag_24: Number(formData.lag_24),
            rolling_24h: Number(formData.rolling_24h),
          }),
        }
      );

      if (!response.ok) throw new Error("Backend error");

      const data = await response.json();
      setResult(data);
    } catch {
      setError("Backend is not reachable. Is FastAPI running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={darkMode ? "dark" : ""}>
      <div className="min-h-screen bg-slate-100 dark:bg-slate-900 transition-colors">
        <div className="max-w-5xl mx-auto px-6 pb-12">
          {/* Header + Toggle */}
          <div className="flex justify-between items-center pt-6">
            <Header />
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="text-sm px-4 py-2 rounded-lg 
                         bg-slate-200 dark:bg-slate-800 
                         text-slate-800 dark:text-slate-200"
            >
              {darkMode ? "☀️ Light" : "🌙 Dark"}
            </button>
          </div>

          <PredictionForm
            formData={formData}
            setFormData={setFormData}
            onSubmit={handleSubmit}
            loading={loading}
            disabled={!isFormValid}
          />

          {error && (
            <p className="text-red-500 text-sm mt-4">{error}</p>
          )}

          {result && <ForecastCards data={result} />}

          <SystemStatus />
        </div>
      </div>
    </div>
  );
}

export default App;
