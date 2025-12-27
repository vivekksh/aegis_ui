export default function PredictionForm({
  formData,
  setFormData,
  onSubmit,
  loading,
  disabled,
}) {
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const inputClass =
    "p-3 rounded-lg border " +
    "bg-white dark:bg-gray-800 " +
    "text-gray-900 dark:text-white " +
    "border-gray-300 dark:border-gray-700 " +
    "placeholder-gray-400 " +
    "focus:outline-none focus:ring-2 focus:ring-sky-500";

  return (
    <div className="mt-6 p-6 rounded-xl shadow-lg
                    bg-white dark:bg-gray-900">
      <h2 className="text-lg font-semibold text-gray-900 dark:text-white">
        Forecast Inputs
      </h2>
      <p className="text-sm text-gray-600 dark:text-gray-400 mb-6">
        Provide recent energy usage and time context
      </p>

      {/* Time Context */}
      <div className="mb-6">
        <h3 className="text-sm text-gray-700 dark:text-gray-300 mb-2">
          Time Context
        </h3>
        <div className="grid grid-cols-3 gap-4">
          <input
            type="number"
            min="0"
            max="23"
            name="hour"
            value={formData.hour}
            onChange={handleChange}
            placeholder="Hour (0–23)"
            className={inputClass}
          />

          <select
            name="day_of_week"
            value={formData.day_of_week}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="">Day of Week</option>
            <option value="0">Monday</option>
            <option value="1">Tuesday</option>
            <option value="2">Wednesday</option>
            <option value="3">Thursday</option>
            <option value="4">Friday</option>
            <option value="5">Saturday</option>
            <option value="6">Sunday</option>
          </select>

          <select
            name="month"
            value={formData.month}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="">Month</option>
            {Array.from({ length: 12 }).map((_, i) => (
              <option key={i} value={i + 1}>
                {new Date(0, i).toLocaleString("default", { month: "long" })}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Energy Context */}
      <div className="mb-6">
        <h3 className="text-sm text-gray-700 dark:text-gray-300 mb-2">
          Recent Energy Usage (kW)
        </h3>
        <div className="grid grid-cols-3 gap-4">
          <input
            type="number"
            step="0.1"
            name="lag_1"
            value={formData.lag_1}
            onChange={handleChange}
            placeholder="1 hour ago"
            className={inputClass}
          />
          <input
            type="number"
            step="0.1"
            name="lag_24"
            value={formData.lag_24}
            onChange={handleChange}
            placeholder="24 hours ago"
            className={inputClass}
          />
          <input
            type="number"
            step="0.1"
            name="rolling_24h"
            value={formData.rolling_24h}
            onChange={handleChange}
            placeholder="Avg last 24h"
            className={inputClass}
          />
        </div>
      </div>

      <button
        onClick={onSubmit}
        disabled={loading || disabled}
        className="w-full py-3 rounded-lg font-semibold
                   bg-sky-500 hover:bg-sky-600
                   text-black disabled:opacity-40"
      >
        {loading ? "Generating forecast..." : "Generate Forecast"}
      </button>
    </div>
  );
}
