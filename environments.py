class Environments:
    qa = {
        'base_url': 'https://sandbox-dashboard.primer.io/',
        'login_url': 'https://sandbox-dashboard.primer.io/login',
        'forgot_pass_url': 'https://sandbox-dashboard.primer.io/forgot-password',
        'valid_username': 'valid@mail.com',
        'valid_password': 'goodpass123',
        'invalid_username': 'invalid@mail.com',
        'invalid_password': 'badpass123',
        'page_title': 'Dashboard | Primer',
    }

    dev = {
        'base_url': 'https://www.jenkins.io/',
        'login_url': '',
        'forgot_pass_url': '',
        'valid_username': '',
        'valid_password': '',
        'invalid_username': '',
        'invalid_password': '',
        'page_title': '',
    }
