from mastodon import Mastodon

# Create app
''' You only need to do this once! After that point, comment out this function. '''

'''Mastodon.create_app(
    'pytooterapp',
    api_base_url = 'https://toot.cat',
    to_file = 'pytooter_clientcred.secret'
    )
    '''

# Log in
mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'https://toot.cat'
    )

with open('userinfo.dat', 'r') as fin:
    USER, PASSWORD = fin.readlines().replace('\r', '').replace('\n', '')

mastodon.log_in(
    USER,
    PASSWORD,
    scopes = ['write', 'follow', 'push'],
    to_file = 'pytooter_usercred.secret'
    )

# Create API instance

mastodon = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'https://toot.cat'
    )

#mastodon.toot('Test toot using Python with #mastodonpy! If you can read this, I was successful :D')

user = r"drlabratory@mastodon.social" # #Testing follows
#user_dict = mastodon.account_follow(user, reblogs=True)

