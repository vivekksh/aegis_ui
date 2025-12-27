export default function ForecastCards({ data }) {
  if (!data) return null;

  const Card = ({ title, result, highlight }) => {
    const unavailable = result?.error;

    return (
      <div
        className={`p-5 rounded-xl border
          ${highlight ? "border-sky-500" : "border-gray-300 dark:border-gray-700"}
          bg-white dark:bg-gray-900`}
      >
        <h3 className="text-sky-500 dark:text-sky-400 font-semibold">
          {title}
        </h3>

        {unavailable ? (
          <p className="text-sm mt-3 text-yellow-600 dark:text-yellow-400">
            Forecast not available yet
          </p>
        ) : (
          <>
            <p className="text-3xl font-bold mt-3
                          text-gray-900 dark:text-white">
              {result.prediction} kW
            </p>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              Expected range: {result.confidence_interval[0]} –{" "}
              {result.confidence_interval[1]} kW
            </p>
          </>
        )}
      </div>
    );
  };

  return (
    <div className="grid grid-cols-3 gap-6 mt-10">
      <Card title="1 Hour Forecast" result={data["1h"]} highlight />
      <Card title="6 Hour Forecast" result={data["6h"]} />
      <Card title="24 Hour Forecast" result={data["24h"]} />
    </div>
  );
}
