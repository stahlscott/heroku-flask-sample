import sys
from app import *
from app.models.post import Post


def initdb():
    db.create_all()
    new_post = Post(title='Hello World!',
                    body='This is my hello world post! As you can see, it\'s truly wonderful and groundbreaking. At '
                         'vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium '
                         'voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint '
                         'occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt '
                         'mollitia animi, id est laborum et dolorum fuga.')
    db.session.add(new_post)
    new_post = Post(title='Hello World Again!', body='This is my *NEW* hello world post. Isn\'t Flask great? At'
                                                     ' vero eos et accusamus et iusto odio dignissimos ducimus qui'
                                                     ' blanditiis praesentium voluptatum deleniti atque corrupti quos'
                                                     ' dolores et quas molestias excepturi sint occaecati cupiditate'
                                                     ' non provident, similique sunt in culpa qui officia deserunt'
                                                     ' mollitia animi, id est laborum et dolorum fuga.')
    db.session.add(new_post)
    db.session.commit()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'initdb':
        initdb()
    else:
        app.run()
