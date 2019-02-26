from tracer import app


config = {
    "development": "config.Development"
}

if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()