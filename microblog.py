from app import create_app, db
from app.models import User, Post, Message, Notification

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,
            'Message': Message, 'Notifications': Notification}


if __name__ == '__main__':
    app.run()
