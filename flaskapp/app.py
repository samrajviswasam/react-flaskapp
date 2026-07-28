import logging
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)


# Enable Prometheus metrics
metrics = PrometheusMetrics(app)


logging.basicConfig(level=logging.INFO)


@app.route("/")
def home():

    app.logger.info("Home endpoint accessed")

    return "Flask App Running"


@app.route("/test")
def test():

    app.logger.info("Test API called")

    return "Testing"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
