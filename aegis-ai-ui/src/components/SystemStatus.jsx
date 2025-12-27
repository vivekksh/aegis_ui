export default function SystemStatus() {
  return (
    <div className="mt-12 p-6 rounded-xl
                    bg-white dark:bg-gray-900">
      <h3 className="text-lg font-semibold
                     text-gray-900 dark:text-white">
        System Status
      </h3>
      <p className="text-sm mb-4
                    text-gray-600 dark:text-gray-400">
        Operational state of the forecasting system
      </p>

      <ul className="space-y-3 text-sm">
        <li className="text-gray-700 dark:text-gray-300">
          🟢 Forecast engine active
        </li>
        <li className="text-gray-700 dark:text-gray-300">
          🔵 Confidence estimation enabled
        </li>
        <li className="text-gray-700 dark:text-gray-300">
          🟡 Monitoring enabled
        </li>
      </ul>
    </div>
  );
}
