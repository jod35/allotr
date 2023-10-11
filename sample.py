def create_app():
    app = Flask(__name__)

    # this will read all your env variables without you having to create many classes
    app.config.from_prefixed_env()

    # all you need is a .env file with you env vars with FLASK_<name of env variable>
    pass
