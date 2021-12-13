
def check_status_code(res):
        if (res.status_code != 200):
            print (res.status_code)
            print(res.reason)
            return False
        return True