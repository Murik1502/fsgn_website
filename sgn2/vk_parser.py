import requests


def get_posts():
    token = '603aed97603aed97603aed97a96322eb886603a603aed97061beb966131cab53dc6e923'
    version = 5.92
    domain = 'fsgn_bmstu'
    all_posts = []
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': 3,
                            }
                            )
    data = response.json()['response']['items']
    all_posts.extend(data)
    return all_posts
