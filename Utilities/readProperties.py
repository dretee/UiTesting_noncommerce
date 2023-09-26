import configparser


configs = configparser.RawConfigParser()
configs.read(".\\Configurations\\config.ini")


class Readconfig:

    @staticmethod
    def GetApplicationURL():
        URL = configs.get('common info', 'test_site_URL')
        return URL

    @staticmethod
    def ApplicationEmail():
        email = configs.get('common info', 'useremail')
        return email

    @staticmethod
    def Applicationpassword():
        password = configs.get('common info', 'password')
        return password
