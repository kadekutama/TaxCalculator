CONFIG = {
    "DEBUG": False,
    "APP_NAME": "TaxCalculator",
    "REQUEST_MAX_SIZE": 100000000,
    "REQUEST_BUFFER_QUEUE_SIZE": 100,
    "REQUEST_TIMEOUT": 60,
    "RESPONSE_TIMEOUT": 60,
    "KEEP_ALIVE": True,
    "KEEP_ALIVE_TIMEOUT": 5,
    "GRACEFUL_SHUTDOWN_TIMEOUT": 15.0,
    "HOST": "0.0.0.0"
}

if CONFIG["DEBUG"]:
    CONFIG["PORT"] = 5000
    CONFIG["WORKERS"] = 1
    CONFIG["ACCESS_LOG"] = True
    CONFIG["DB_HOST"] = "127.0.0.1"
    CONFIG["DB_PORT"] = 5432
    CONFIG["DB_USER"] = "postgres"
    CONFIG["DB_PASSWORD"] = "haido"
    CONFIG["DB_DATABASE"] = "taxcalculator"
else:
    CONFIG["PORT"] = 6000
    CONFIG["WORKERS"] = 4
    CONFIG["ACCESS_LOG"] = False
    CONFIG["DB_HOST"] = "postgresql"
    CONFIG["DB_PORT"] = 5432
    CONFIG["DB_USER"] = "postgres"
    CONFIG["DB_PASSWORD"] = "haido"
    CONFIG["DB_DATABASE"] = "taxcalculator"