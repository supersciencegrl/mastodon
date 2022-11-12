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


mastodon.log_in(
    'methionine57@gmail.com',
    r"O<lE@c+`rn,>,D8*",
    scopes = ['write', 'follow', 'push'],
    to_file = 'pytooter_usercred.secret'
    )

# Create API instance

mastodon = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'https://toot.cat'
    )

#mastodon.toot('Test toot using Python with #mastodonpy! If you can read this, I was successful :D')

user = r"drlabratory@mastodon.social"
#user_dict = mastodon.account_follow(user, reblogs=True)

